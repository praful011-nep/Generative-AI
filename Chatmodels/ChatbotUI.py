import os
from pathlib import Path
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

load_dotenv(Path(__file__).resolve().parents[1] / ".env", override=True)

# Initialize model from API
model = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
    timeout=40,
)

st.title("Chatbot")
st.caption("Welcome (Type 0 to exit)")

# Stores all the prompts and responses from user and Bot side (short term memory)
# st.session_state keeps it alive across Streamlit reruns
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are a Data Science Tutor.")
    ]
if "ended" not in st.session_state:
    st.session_state.ended = False

# Show conversation so far (skip the system message)
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

if st.session_state.ended:
    st.info("Conversation ended. Refresh the page to start again.")
else:
    prompt = st.chat_input("You: ")
    if prompt:
        # Message given by user is stored
        st.session_state.messages.append(HumanMessage(content=prompt))
        if prompt == "0":
            st.session_state.ended = True
            st.rerun()
        else:
            with st.chat_message("user"):
                st.write(prompt)
            response = model.invoke(st.session_state.messages)  # Store response from model
            st.session_state.messages.append(AIMessage(content=response.content))
            with st.chat_message("assistant"):
                st.write(response.content)