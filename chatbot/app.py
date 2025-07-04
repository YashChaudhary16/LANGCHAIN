import streamlit as st
import os
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

os.environ["ANTHROPIC_API_KEY"] = os.getenv("ANTHROPIC_API_KEY")

from dotenv import load_dotenv
load_dotenv(dotenv_path="chatbot/.env", override=True)

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