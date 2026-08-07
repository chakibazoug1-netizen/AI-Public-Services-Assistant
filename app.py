import streamlit as st
from knowledge import knowledge
import time

st.set_page_config(
    page_title="AI Public Services Assistant",
    page_icon="🏛️",
    layout="centered"
)

st.title("🏛️ AI Public Services Assistant")

st.write("""
Welcome!

This assistant provides information about public services and
administrative procedures.
""")

question = st.text_input("Ask your question")

if st.button("Search"):

    if question == "":
        st.warning("Please enter a question.")

    else:
        with st.spinner("Searching..."):
            time.sleep(1)

        q = question.lower()

found = False

for key, answer in knowledge.items():
    if key in q:
        st.success(key.title())
        st.write(answer)
        found = True
        break

if not found:
    st.info("Sorry, this information is not available yet.")
