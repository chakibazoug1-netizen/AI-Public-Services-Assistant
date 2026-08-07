import streamlit as st
import time

st.set_page_config(
    page_title="AI Public Services Assistant",
    page_icon="🏛️",
    layout="centered"
)

st.title("🏛️ AI Public Services Assistant")

st.markdown("""
Welcome!

This assistant helps citizens obtain information about public services and administrative procedures.

Type your question below.
""")

question = st.text_input("Ask your question")

if st.button("Search"):
    if question == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Searching..."):
            time.sleep(2)

        st.success("Answer found!")

        st.info(f"""
You asked:

{question}

This is still a prototype.

Soon this assistant will provide real answers using Artificial Intelligence.
""")
