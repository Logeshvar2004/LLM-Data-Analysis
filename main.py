import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma  # Updated import
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
import pandas as pd

st.title("Chat Your CSV")  # Updated title for CSV

# Load environment variables from .env file
load_dotenv(r"D:\Coding\python\LLM-Analysis\.env")

# Retrieve API key from environment variable
google_api_key = os.getenv("GEMINI_API_KEY")

# Check if the API key is available
if google_api_key is None:
    st.warning("API key not found. Please set the google_api_key environment variable.")
    st.stop()

# File Upload with user-defined name
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    st.text("CSV File Uploaded Successfully!")

    # CSV Processing (using pandas)
    df = pd.read_csv(uploaded_file)

    # Create Context from the DataFrame
    context = df.to_string(index=False)

    # Split Texts
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=200)
    texts = text_splitter.split_text(context)

    # Chroma Embeddings
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_index = Chroma.from_texts(texts, embeddings).as_retriever()

    # Get User Question
    user_question = st.text_input("Ask a Question:")

    if st.button("Get Answer"):
        if user_question:
            # Get Relevant Documents
            docs = vector_index.get_relevant_documents(user_question)

            # Define Prompt Template
            prompt_template = """
            Answer the question as detailed as possible from the provided context,
            make sure to provide all the details. If the answer is not in
            the provided context, just say, "answer is not available in the context",
            don't provide the wrong answer.\n\n
            Context:\n {context}?\n
            Question: \n{question}\n
            Answer:
            """

            # Create Prompt
            prompt = PromptTemplate(template=prompt_template, input_variables=['context', 'question'])

            # Load QA Chain
            model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3, api_key=google_api_key)
            chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

            # Get Response
            response = chain({"input_documents": docs, "question": user_question}, return_only_outputs=True)

            # Display Answer
            st.subheader("Answer:")
            st.write(response['output_text'])

        else:
            st.warning("Please enter a question.")
