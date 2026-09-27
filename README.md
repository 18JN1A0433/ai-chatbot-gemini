# AI Chatbot using Google Gemini

## Overview

A Python-based conversational AI chatbot built using the Google Gemini API.
The chatbot maintains conversation context and uses system instructions to provide
consistent and helpful responses.

## Features

- Conversational interaction with an LLM
- Conversation history and context
- System instructions for chatbot behavior
- Error handling for API requests
- Secure API key management using Google Colab Secrets

## Technologies Used

- Python
- Google Gemini API
- Google GenAI SDK
- Google Colab
- GitHub

## Project Architecture

User
  ↓
Python Chatbot
  ↓
Google GenAI SDK
  ↓
Google Gemini API
  ↓
AI Response

## Project Structure

```text
ai-chatbot-gemini/
│
├── chatbot.ipynb
├── requirements.txt
├── README.md
└── .gitignore

## API Key Security

The Gemini API key is not stored directly in the source code.

The project uses Google Colab Secrets to securely access the API key and avoid exposing sensitive credentials.

## How It Works

1. The user enters a message.
2. The Python chatbot sends the message to the Gemini API.
3. Gemini processes the request.
4. The response is returned to the chatbot.
5. Conversation history allows the chatbot to maintain context across messages.

## Future Enhancements

- PDF document processing
- Retrieval-Augmented Generation (RAG)
- Document embeddings and vector search
- Context-aware question answering
- Web-based chatbot interface
