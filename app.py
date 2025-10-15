import streamlit as st
from utils import extract_text_from_pdf, ask_gemini

st.set_page_config(page_title="AI PDF Chatbot with Gemini")
st.title("AI PDF Chatbot with Gemini")

if "pdf_text" not in st.session_state:
    st.session_state["pdf_text"] = ""
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# PDF uploader
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
if uploaded_file:
    st.session_state["pdf_text"] = extract_text_from_pdf(uploaded_file)
    st.success("PDF uploaded and text extracted successfully.")
    st.session_state["chat_history"] = []

# Question input
user_input = st.text_input("Ask a question about the PDF:")

# Handle Send button
if st.button("Send") and user_input.strip():
    if not st.session_state["pdf_text"]:
        st.error("Please upload a PDF first.")
    else:
        answer = ask_gemini(user_input, st.session_state["pdf_text"])
        st.session_state["chat_history"].append(("You", user_input))
        st.session_state["chat_history"].append(("AI", answer))

# Display chat history (after updates)
if st.session_state["chat_history"]:
    st.markdown("### Chat History")
    for speaker, message in st.session_state["chat_history"]:
        if speaker == "You":
            st.markdown(f"**You:** {message}")
        else:
            st.markdown(f"**AI:** {message}")
