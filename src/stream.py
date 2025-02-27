import streamlit as st
import requests

st.header("AI - Literature Chatbot")
st.title("I'm Optimized LLM")

user_id = "123"  # Replace with actual user ID
user_input = st.text_input("Your prompt:", "")

if st.button("call me!"):
    url = "http://localhost:8000/user/chat"
    data = {"user_id": user_id, "user_input": user_input}  # Matches FastAPI schema

    try:
        response = requests.post(url, json=data)  # Ensure JSON format
        if response.status_code == 200:
            Api_Response =  response.json()
            st.success(f"{Api_Response['response']}")
            st.warning(f"Response Time: {Api_Response['resposne_time']}")
            
        else:
            st.error(f"Error {response.status_code}: {response.text}")
    except requests.exceptions.ConnectionError:
        st.error("Failed to connect to FastAPI. Make sure the server is running!")