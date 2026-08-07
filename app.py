import streamlit as st
from knowledge import knowledge
import time


# -----------------------------
# Page configuration
# -----------------------------

st.set_page_config(
    page_title="AI Public Services Assistant",
    page_icon="🏛️",
    layout="centered"
)


# -----------------------------
# Title
# -----------------------------

st.title("🏛️ AI Public Services Assistant")


st.write(
    """
Welcome!

This assistant provides information about public services
and administrative procedures.
"""
)


# -----------------------------
# Search box
# -----------------------------

question = st.text_input(
    "Ask your question",
    placeholder="Example: passport, residence certificate, ID card..."
)


# -----------------------------
# Search button
# -----------------------------

if st.button("Search"):

    # Check empty question
    if question.strip() == "":
        st.warning("Please enter a question.")

    else:

        # Searching animation
        with st.spinner("Searching..."):
            time.sleep(1)

        # Normalize the question
        q = question.lower().strip()

        # Search status
        found = False

        # Search through the knowledge base
        for service in knowledge:

            for keyword in service["keywords"]:

                if keyword.lower() in q:

                    # Display result
                    st.success(service["title"])

                    st.write(service["answer"])

                    found = True

                    break

            if found:
                break

        # No result
        if not found:

            st.info(
                "Sorry, this information is not available yet."
            )
