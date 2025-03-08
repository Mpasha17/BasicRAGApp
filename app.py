import streamlit as st
from qna import get_qa_chain, create_vector_db

# title of the Streamlit app
st.title("Basics Q&A Demo")

# input field for user to enter a question
question = st.text_input("Question: ")

if question:
    chain = get_qa_chain()
    response = chain.invoke(question) 

    # displaying the answer 
    st.header("Answer")
    st.write(response["result"])
