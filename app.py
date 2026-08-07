import streamlit as st
from knowledge import knowledge
import time


# Page configuration
st.set_page_config(
    page_title="AI Public Services Assistant",
    page_icon="🏛️",
    layout="centered"
)


# Title
st.title("🏛️ AI Public Services Assistant")


# Introduction
st.write("""
Welcome!

This assistant provides information about public services
and administrative procedures.
""")


# Search box
question = st.text_input(
    "Ask your question",
    placeholder="Example: passport, residence certificate, ID card..."
)


# Search button
if st.button("Search"):

    if question.strip() == "":
        st.warning("Please enter a question.")

    else:

        with st.spinner("Searching..."):
            time.sleep(1)

        q = question.lower().strip()

        found = False


        # ---------------------------------
        # Knowledge is a dictionary
        # ---------------------------------

        if isinstance(knowledge, dict):

            for key, answer in knowledge.items():

                if key.lower() in q:

                    st.success(key.title())
                    st.write(answer)

                    found = True
                    break


        # ---------------------------------
        # Knowledge is a list
        # ---------------------------------

        elif isinstance(knowledge, list):

            for service in knowledge:

                for keyword in service.get("keywords", []):

                    if keyword.lower() in q:

                        st.success(service["title"])
                        st.write(service["answer"])

                        found = True
                        break

                if found:
                    break


        # ---------------------------------
        # No result
        # ---------------------------------

        if not found:

            st.info(
                "Sorry, this information is not available yet."
            )
