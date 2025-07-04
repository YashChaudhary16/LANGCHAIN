import streamlit as st
import os
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

os.environ["ANTHROPIC_API_KEY"] = os.getenv("ANTHROPIC_API_KEY")


os.environ["LANGCHAIN_SMITH_TRACING_V2"] = "true"
os.environ["LANGCHAIN_SMITH_TRACING"] = "true"
os.environ["LANGSMITH_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGSMITH_PROJECT"] = os.getenv("LANGSMITH_PROJECT")
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")

st.title("Claude Chat")

# Create a prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("user", "{input}")
    ]
)

user_input = st.text_input("Ask me anything:")

model = ChatAnthropic(model="claude-3-5-haiku-20241022")
output_parser = StrOutputParser()
    
# Use the prompt template
chain = prompt | model | output_parser

if user_input:
    response = chain.invoke({"input": user_input})
    st.write(response)