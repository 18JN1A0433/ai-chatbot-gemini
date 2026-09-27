import os
import gradio as gr
from google import genai

# Get API key securely from environment variable
api_key = os.environ.get("Open_ai_api_key")

client = genai.Client(api_key=api_key)

chat = client.chats.create(
    model="gemini-3.5-flash-lite"
)


def chatbot(message, history):
    response = chat.send_message(message)
    return response.text


demo = gr.ChatInterface(
    fn=chatbot,
    title="My Gemini AI Chatbot",
    description="A conversational AI chatbot powered by Google Gemini."
)

demo.launch()
