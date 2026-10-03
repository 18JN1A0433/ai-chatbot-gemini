import streamlit as st
from google import genai


# Get Gemini API key securely from Streamlit Secrets
api_key = st.secrets["Open_ai_api_key"]


# Create Gemini client
@st.cache_resource
def get_client():
    return genai.Client(api_key=api_key)


client = get_client()


# Create a new chat for this browser session
if "chat" not in st.session_state:
    st.session_state.chat = client.chats.create(
        model="gemini-3.5-flash-lite"
    )


# Store displayed conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Page title
st.title("🤖 Bindu's Gemini AI Chatbot")
st.write("A conversational AI chatbot powered by Google Gemini and created by bindu.")


# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


# Get user input
user_input = st.chat_input("Type your message here...")


if user_input:

    # Display user message
    st.chat_message("user").write(user_input)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Send message to Gemini
    response = st.session_state.chat.send_message(user_input)

    # Display Gemini response
    st.chat_message("assistant").write(response.text)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response.text
        }
    )

