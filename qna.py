import os
from langchain.chat_models import init_chat_model
from langchain.chains import RetrievalQA
from langchain_mistralai import MistralAIEmbeddings
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

# To Load environment 
load_dotenv()

# Mistral AI model
model = init_chat_model("mistral-large-latest", model_provider="mistralai")

# Mistral embeddings
embeddings = MistralAIEmbeddings(model="mistral-embed")

vectordb_file_path = "faiss_index"

# Creting the vector Database using Faiss
def create_vector_db():

    # loading data
    loader = CSVLoader(file_path='/Users/pasha/Desktop/QandA/Data/Comprehensive_Data_Set_for_COO_Analysis.csv')
    data = loader.load()

    # Creating the Faiss vector database from data
    vectordb = FAISS.from_documents(documents=data, embedding=embeddings)

    # Saving vector database locally
    vectordb.save_local(vectordb_file_path)

def get_qa_chain():
    # Load the vector database from the local folder
    vectordb = FAISS.load_local(vectordb_file_path, embeddings, allow_dangerous_deserialization=True)

    # Creating a retriever for querying the vector database
    retriever = vectordb.as_retriever(score_threshold=0.7)
    # Prompt to displaying the desire output
    prompt_template = """Given the following context and a question, generate an answer based on this context only. 
    In the answer, try to provide as much text as possible from the context without making significant changes. 
    Follow these formatting guidelines:
    1. If the context includes numerical data or metrics, present them in a **table format**.
    2. Include **key insights** in bold text, followed by relevant analysis or suggestions.
    3. Use bullet points for lists or breakdowns.
    4. Add emojis where appropriate to make the response engaging.
    5. Maintain a clear and structured format, similar to the example provided.
    CONTEXT: {context}

    QUESTION: {question}

    Answer:"""

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    # Initializing the retrievalqa chain
    chain = RetrievalQA.from_chain_type(
        llm=model,
        chain_type="stuff",
        retriever=retriever,
        input_key="query",
        return_source_documents=True,
        chain_type_kwargs={"prompt": PROMPT}
    )

    return chain