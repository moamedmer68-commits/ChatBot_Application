# Gemini 2.5 ChatBot

An advanced yet lightweight chatbot built with **Streamlit** and **Google's Gemini 2.5 Pro** model.  
This project demonstrates how to integrate modern AI models into a simple, interactive web interface using Python.

---

##  Overview

The **Gemini 2.5 ChatBot** allows users to chat directly with Google's **Generative AI** in real-time.  
It’s designed to be clean, minimal, and efficient — perfect for experimenting with AI text generation.

---

##  Features

-  Real-time two-way conversation  
-  Uses **Gemini 2.5 Pro** for intelligent text generation  
-  Keeps chat history within the same session  
-  Lightweight and responsive Streamlit UI  
-  Secure API key handling using environment variables  

---

##  Technologies Used

| Component | Description |
|------------|-------------|
| **Python** | Core programming language |
| **Streamlit** | Web framework for interactive UI |
| **Google Generative AI API** | Provides Gemini 2.5 model for content generation |

---
## Project Structure

```plaintext
Gemini-ChatBot/
│
├── chatBot_Application.py      # Main Streamlit application
│   ├─ Handles UI components and layout
│   ├─ Connects to the Gemini 2.5 model via Google Generative AI API
│   ├─ Maintains chat session history using Streamlit’s session_state
│   └─ Displays user input and AI-generated responses in a chat-like interface
│
├── requirements.txt            # Python dependencies
│   ├─ streamlit: for building the web interface
│   └─ google-generativeai: for connecting to Gemini 2.5 Pro
│
├── README.md                   # Documentation file
│   ├─ Explains project setup, usage, and deployment
│   ├─ Provides examples and structure overview
│   └─ Acts as a main reference for contributors or users
│
└── .streamlit/ (optional)
    ├─ config.toml              # Custom Streamlit configuration (if needed)
    └─ secrets.toml             # Secure place for API keys (optional)

