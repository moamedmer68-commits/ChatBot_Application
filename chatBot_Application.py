
import streamlit as st
import google.generativeai as genai
import os
api=AIzaSyC4Y45I9NBNOI5NZXGoOAZq8Y3Ujv4sLUQ
os.system("pip install -U google-generativeai")
api = os.getenv("GOOGLE_API_KEY")

st.title(" Gemini 2.5 ChatBot")

# API Key setup
if api:
    genai.configure(api_key=api)
else:
    st.error("Invalid API Key")

# Text generation function
def Generate_Text(text):
    model = genai.GenerativeModel("models/gemini-2.5-pro")
    response = model.generate_content(text)
    return response.text

# Initialize session state for chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input and model response
if user_input := st.chat_input("Type your question here..."):
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        with st.spinner("⏳ Generating response..."):
            try:
                response_text = Generate_Text(user_input)
            except Exception as e:
                response_text = f" Error: {e}"
        message_placeholder.markdown(response_text)

    st.session_state.messages.append({"role": "assistant", "content": response_text})

