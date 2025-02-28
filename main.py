import uvicorn
from fastapi import FastAPI
from src.llm_utils.pydantic_params.params import UserChatRequest
from src.llm_utils.llm_engine import Bot_Assistant
from fastapi.middleware.cors import CORSMiddleware
import streamlit as st


app = FastAPI(title='AI-Literature')
origins = [
    "*"
]
for i in [app]:
    i.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )
import time




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


@app.post('/user/chat')
def UserChat(userparam:UserChatRequest):
    start = time.time()
    response= Bot_Assistant().prephase_Bot(UserInput=userparam.user_input)
    print("[+]response = ",response)
    print("Time taken to load the model: ",time.time()-start)
    return {'response':response['model_raw_output'],'resposne_time':time.time()-start}




if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, workers=2, reload=True)  