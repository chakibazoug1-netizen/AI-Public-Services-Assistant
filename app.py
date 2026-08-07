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

        if "passport" in q:
            st.success("Passport Information")
            st.write("""
• Valid national ID card
• Birth certificate
• Biometric photo
• Payment of required fees
""")

        elif "identity" in q or "id card" in q:
            st.success("National Identity Card")
            st.write("""
• Birth certificate
• Residence certificate
• Biometric photo
""")

        elif "residence" in q:
            st.success("Residence Certificate")
            st.write("""
The residence certificate is issued by the municipality of residence.
""")

        else:
            st.info("Sorry, this information is not available yet.")
