import streamlit as st
from agent import smart_agent
from classifier import classify_domain

st.set_page_config(page_title="StudyBBuddy AI", page_icon=":mortar_board:📚")
st.title("📚 StudyBuddy AI Assistant")
st.write("Welcome to StudyBuddy! Ask me anything about education, health, or sustainability, and I'll do my best to help you out.")
user_input = st.text_input("Ask me anything:")
def smart_response(message: str) -> str:
    domain = classify_domain(message)
    prefix = f"[{domain.upper()}] {message}"
    return smart_agent(prefix)
if st.button("Ask"):
    if user_input:
        response = smart_response(user_input)
        st.subheader("StudyBuddy's Response:")
        st.write(response)