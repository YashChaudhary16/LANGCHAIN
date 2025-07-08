import os
from dotenv import load_dotenv

from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_community.utilities import ArxivAPIWrapper
from langchain_community.tools import ArxivQueryRun
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.tools.retriever import create_retriever_tool
from langchain.agents import initialize_agent, AgentType

# --- Load Environment Variables ---
load_dotenv(dotenv_path="C:/Users/Lenovo/Desktop/LANGCHAIN/.env", override=True)

# --- 1. Wikipedia Tool Setup ---
wiki_api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=250)
wiki_tool = WikipediaQueryRun(api_wrapper=wiki_api_wrapper)

# --- 3. Arxiv Tool Setup ---
arxiv_api_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=250)
arxiv_tool = ArxivQueryRun(api_wrapper=arxiv_api_wrapper)

# --- 4. Define Tool List ---
tools = [wiki_tool, arxiv_tool]

# --- 5. Initialize the LLM ---
llm = ChatOllama(model="llama3")

# --- 6. Create the Agent (ReAct/ZeroShot) ---
agent_executor = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,  # or AgentType.REACT_DESCRIPTION
    verbose=True
)

# --- 7. Invoke the Agent with Queries ---

print("\n" + "="*50)
print("Example 2: Querying Wikipedia...")
response2 = agent_executor.invoke({
    "input": "Who is the CEO of Tesla?"
})
print("\nFinal Answer:", response2["output"])

print("\n" + "="*50)
print("Example 3: Querying Arxiv...")
response3 = agent_executor.invoke({
    "input": "What is the paper 'Attention Is All You Need' about?"
})
print("\nFinal Answer:", response3["output"])
print("\n" + "="*50)