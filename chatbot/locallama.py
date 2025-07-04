from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import os
import streamlit as st

from dotenv import load_dotenv
load_dotenv(dotenv_path="chatbot/.env", override=True)

os.environ["LANGCHAIN_SMITH_TRACING_V2"] = "true"
os.environ["LANGCHAIN_SMITH_TRACING"] = "true"
os.environ["LANGSMITH_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGSMITH_PROJECT"] = os.getenv("LANGSMITH_PROJECT")
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")


st.title("Local LLM Chatbot")


prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "{input}")
])

user_input = st.text_input("Ask me anything:")

# model = ChatAnthropic(model="claude-3-5-haiku-20241022")
llm = Ollama(model="gemma3")
output_parser = StrOutputParser()
    
# Use the prompt template
chain = prompt | llm | output_parser

if user_input:
    response = chain.invoke({"input": user_input})
    st.write(response)








