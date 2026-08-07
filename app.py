import streamlit as st

st.set_page_config(
    page_title="AI Public Services Assistant",
    page_icon="🏛️",
    layout="centered"
)

st.title("🏛️ AI Public Services Assistant")

st.write("""
Welcome!

This AI-powered assistant helps citizens find information about public services and administrative procedures.
""")

question = st.text_input("Ask your question")

if question:
    q = question.lower()

    if "passport" in q:
        st.success("To apply for a passport, you need your national ID card, birth certificate, biometric photo, and the required application form.")

    elif "id" in q:
        st.success("To obtain or renew your national ID card, visit your local municipality with the required documents.")

    elif "birth" in q:
        st.success("Birth certificates can be obtained from the civil registry office or through online government services where available.")

    else:
        st.info("Sorry, this prototype currently answers only a limited number of public service questions.")
