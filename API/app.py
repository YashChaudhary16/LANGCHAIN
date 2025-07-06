from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_anthropic import ChatAnthropic
from langchain_community.llms import Ollama 
from langserve import add_routes
import uvicorn
import os


from dotenv import load_dotenv
load_dotenv(dotenv_path="API/.env", override=True)

app = FastAPI(
    title="Langchain API",
    description="API for Langchain",
    version="1.0.0"
)

add_routes(
    app, 
    ChatAnthropic(model="claude-3-5-haiku-20241022"), 
    path="/anthropic"
)

add_routes(app, ChatAnthropic(model="claude-3-5-haiku-20241022"), path="/openapi.json")

paid_llm = ChatAnthropic(model="claude-3-5-haiku-20241022")
free_llm = Ollama(model="gemma3")

prompt1 = ChatPromptTemplate.from_template("Explain me {topic} in 1 line.")
prompt2 = ChatPromptTemplate.from_template("Write me a riddle about{topic}.")

add_routes(
    app,
    prompt1 | paid_llm,
    path="/paid"
)

add_routes(
    app,
    prompt2 | free_llm,
    path="/free"
)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)



