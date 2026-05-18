import streamlit as st
from agent import smart_agent
from classifier import classify_domain

st.set_page_config(page_title="StudyBBuddy AI", page_icon=":mortar_board:📚")
st.title("📚 StudyBuddy AI Assistant")
st.write("Welcome to StudyBuddy! Ask me anything about education, health, or sustainability, and I'll do my best to help you out.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.text_input("Ask me anything:")
def smart_response(message, history):
    domain = classify_domain(message)
    formatted_message = f"[{domain.upper()}] {message}" 
    response = smart_agent(formatted_message, history)
    return response
if st.button("Ask"):
    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)
            response = smart_response(user_input, st.session_state.chat_history)
            with st.chat_message("assistant"):
                st.markdown(response)
            st.session_state.chat_history.append({
                "role": "assistant",
                "content": response
            })