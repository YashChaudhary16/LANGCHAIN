import requests
import streamlit as st

def get_paid_response(topic):
    response = requests.post(
        "http://localhost:8000/paid/invoke",
        json={"input": {"topic": topic}}
    )
    return response.json()["output"]["content"]

def get_free_response(topic):
    response = requests.post(
        "http://localhost:8000/free/invoke",
        json={"input": {"topic": topic}}
    )
    output = response.json()["output"]
    # If output is a dict with 'content', return it; else, return output directly
    if isinstance(output, dict) and "content" in output:
        return output["content"]
    return output

st.title("Langchain API Client")
topic = st.text_input("Enter a topic:")
if st.button("Get Paid Response"):
    st.write(get_paid_response(topic))
if st.button("Get Free Response"):
    st.write(get_free_response(topic))






