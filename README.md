# BasicRAGApp

This project is a simple Retrieval-Augmented Generation (RAG) application using Mistral AI for answering questions based on a given dataset. The app loads a CSV file, creates a FAISS vector database, and allows users to ask questions using a retrieval-based QA chain.

## Installation

### Prerequisites
- Python 3.8+
- Virtual Environment (Recommended)

### Setup
1. **Clone the Repository**
   ```sh
   git clone https://github.com/Mpasha17/BasicRAGApp.git
   cd BasicRAGApp
   ```

2. **Create and Activate a Virtual Environment**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**
   - Create a `.env` file in the project directory.
   - Add your API keys or other environment variables inside the `.env` file.
   
   Example:
   ```env
   MISTRAL_API_KEY=your_api_key_here
   ```

## Running the Application

1. **Create the Vector Database**
   ```sh
   python -c "from qna import create_vector_db; create_vector_db()"
   ```
   This will generate a FAISS index from the provided CSV dataset.

2. **Start the Streamlit App**
   ```sh
   streamlit run app.py
   ```

## Project Structure
```
BasicRAGApp/
│── app.py              # Streamlit app
│── qna.py              # QA Chain and Vector DB creation
│── requirements.txt    # Required dependencies
│── .env                # Environment variables (ignored in Git)
│── faiss_index/        # FAISS vector database (created after running the script)
│── data/
│   └── Comprehensive_Data_Set_for_COO_Analysis.csv  # CSV dataset
└── README.md          # Project documentation
```

