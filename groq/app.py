import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
import time



from dotenv import load_dotenv
load_dotenv(dotenv_path="C:/Users/Lenovo/Desktop/LANGCHAIN/.env", override=True)

if "vectorstore" not in st.session_state:
    st.session_state.embeddings = OllamaEmbeddings(model="llama3")

    st.session_state.loader = WebBaseLoader(
        web_paths=["https://docs.langsmith.com/"]
    )

    st.session_state.docs = st.session_state.loader.load()

    st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

    st.session_state.final_docs = st.session_state.text_splitter.split_documents(
        st.session_state.docs[:20], 
        embedding=st.session_state.embeddings
    )

    st.session_state.vectorstore = FAISS.from_documents(
        st.session_state.final_docs
    )

    # st.session_state.retriever = st.session_state.vectorstore.as_retriever()

st.title("ChatGroq Demo")

llm = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct", temperature=0)

prompt = ChatPromptTemplate.from_template(
    """
    You are a helpful assistant that can answer questions.
    Only provide most accurate answer to the questions using the following context:
    <context>
    {context}
    </context>
    Question: {input}
    """
)

document_chain = create_stuff_documents_chain(llm, prompt)

retriever = st.session_state.vectorstore.as_retriever()

retrieval_chain = create_retrieval_chain(
    retriever,
    document_chain
)

prompt = st.text_input("Enter your query/question:")

if prompt:
    st.write("Thinking...")
    start_time = time.time()
    response = retrieval_chain.invoke({"input": prompt})
    end_time = time.time()
    st.write(f"Answer: {response['answer']}")
    st.write(f"Time taken: {end_time - start_time:.2f} seconds")






