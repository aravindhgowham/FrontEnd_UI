import streamlit as st
import requests

st.header("AI - Literature Chatbot")
st.title("I'm Optimized LLM")

user_id = "123"  # Replace with actual user ID
user_input = st.text_input("Your prompt:", "")

if st.button("call me!"):
    url = "https://conversational-ai-production.up.railway.app/user/chat"
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


"""Below code is an Websocket"""
# import streamlit as st
# import asyncio
# import websockets
# import json

# st.header("AI - Literature Chatbot")
# st.title("I'm Optimized LLM")

# WS_URL = "ws://127.0.0.1:8000/user"  # Update WebSocket URL
# user_id = "123"  # Replace with actual user ID
# user_input = st.text_input("Your prompt:", "")

# def websocket_chat(user_input):

#     try:
#         with websockets.connect(WS_URL) as websocket:
#             websocket.send(user_input)  # Send user input
#             response = websocket.recv()  # Receive response
#             return json.loads(response)  # Convert JSON to dictionary
#     except websockets.exceptions.ConnectionClosed as E:
#         print(f"handleException: {str(E)}");return {'error':f"Websocket closed: {str(E)}"}
#     except Exception as E:
#         print(f"[-]Exception: {str(E)}");return {'error':str(E)}


# if st.button("call me!"):
#     if user_input:
#         try:
#             response_data = websocket_chat(user_input)  # WebSocket call
            
#             if 'error' in response_data:
#                 st.error(response_data['error'])
            
#             else:
#                 st.success(f"{response_data['response']}")
#                 # st.warning(f"Response Time: {response_data['response_time']} ms")
#         except Exception as e:
#             st.error(f"WebSocket Error: {str(e)}")








