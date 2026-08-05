import streamlit as st

st.set_page_config(page_title="AI Public Services Assistant")

st.title("AI Public Services Assistant")

question = st.text_input("Ask your question")

if question:
    st.success("Demo response")
    st.write("This is a prototype AI assistant designed to help citizens access public service information.")
