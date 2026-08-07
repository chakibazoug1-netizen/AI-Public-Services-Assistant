import streamlit as st
from knowledge import knowledge
import time

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="AI Public Services Assistant",
    page_icon="🏛️",
    layout="centered"
)

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🏛️ AI Public Services Assistant")

st.write(
    """
    منصة متخصصة للوصول السريع إلى المعلومات المتعلقة
    بالوثائق والملفات الإدارية في الجزائر.
    """
)

st.write("اختر الوثيقة مباشرة أو استخدم البحث الحر.")

# --------------------------------------------------
# LANGUAGE
# --------------------------------------------------

language = st.radio(
    "🌐 اللغة / Language",
    ["العربية", "English"],
    horizontal=True
)

# --------------------------------------------------
# NORMALIZE KNOWLEDGE DATA
# This section accepts both:
# 1. Dictionary format
# 2. List of dictionaries format
# --------------------------------------------------

documents = []

if isinstance(knowledge, dict):

    for key, value in knowledge.items():

        if isinstance(value, str):

            documents.append(
                {
                    "title_ar": str(key),
                    "title_en": str(key),
                    "keywords": [str(key)],
                    "answer_ar": value,
                    "answer_en": value
                }
            )

        elif isinstance(value, dict):

            title_ar = value.get(
                "title_ar",
                value.get("title", str(key))
            )

            title_en = value.get(
                "title_en",
                value.get("title", str(key))
            )

            keywords = value.get(
                "keywords",
                [str(key)]
            )

            answer_ar = value.get(
                "answer_ar",
                value.get("answer", "")
            )

            answer_en = value.get(
                "answer_en",
                value.get("answer", "")
            )

            documents.append(
                {
                    "title_ar": str(title_ar),
                    "title_en": str(title_en),
                    "keywords": keywords,
                    "answer_ar": str(answer_ar),
                    "answer_en": str(answer_en)
                }
            )

elif isinstance(knowledge, list):

    for item in knowledge:

        if not isinstance(item, dict):
            continue

        title_ar = item.get(
            "title_ar",
            item.get("title", "وثيقة")
        )

        title_en = item.get(
            "title_en",
            item.get("title", "Document")
        )

        keywords = item.get(
            "keywords",
            []
        )

        answer_ar = item.get(
            "answer_ar",
            item.get("answer", "")
        )

        answer_en = item.get(
            "answer_en",
            item.get("answer", "")
        )

        if not isinstance(keywords, list):
            keywords = [str(keywords)]

        documents.append(
            {
                "title_ar": str(title_ar),
                "title_en": str(title_en),
                "keywords": keywords,
                "answer_ar": str(answer_ar),
                "answer_en": str(answer_en)
            }
        )

# --------------------------------------------------
# CHECK KNOWLEDGE
# --------------------------------------------------

if not documents:

    st.warning(
        "لم يتم العثور على بيانات الوثائق في ملف knowledge.py."
    )

    st.stop()

# --------------------------------------------------
# DOCUMENT SELECTOR
# --------------------------------------------------

if language == "العربية":

    document_options = [
        item["title_ar"]
        for item in documents
    ]

    selected_document = st.selectbox(
        "📄 اختر الوثيقة",
        ["-- اختر وثيقة --"] + document_options
    )

else:

    document_options = [
        item["title_en"]
        for item in documents
    ]

    selected_document = st.selectbox(
        "📄 Select a document",
        ["-- Select a document --"] + document_options
    )

# --------------------------------------------------
# DISPLAY SELECTED DOCUMENT
# --------------------------------------------------

if selected_document not in [
    "-- اختر وثيقة --",
    "-- Select a document --"
]:

    selected_data = None

    for item in documents:

        if language == "العربية":

            if item["title_ar"] == selected_document:
                selected_data = item
                break

        else:

            if item["title_en"] == selected_document:
                selected_data = item
                break

    if selected_data is not None:

        if language == "العربية":

            st.subheader(
                "📄 " + selected_data["title_ar"]
            )

            st.write(
                selected_data["answer_ar"]
            )

        else:

            st.subheader(
                "📄 " + selected_data["title_en"]
            )

            st.write(
                selected_data["answer_en"]
            )

# --------------------------------------------------
# FREE SEARCH
# --------------------------------------------------

if language == "العربية":

    search_label = "🔎 البحث الحر"

    search_placeholder = (
        "اكتب اسم الوثيقة أو جزءًا من السؤال..."
    )

    search_button = "بحث"

else:

    search_label = "🔎 Free Search"

    search_placeholder = (
        "Enter the document name or part of your question..."
    )

    search_button = "Search"

st.subheader(search_label)

question = st.text_input(
    search_label,
    placeholder=search_placeholder
)

# --------------------------------------------------
# SEARCH FUNCTION
# --------------------------------------------------

if st.button(search_button):

    if question.strip() == "":

        if language == "العربية":
            st.warning("يرجى إدخال كلمة أو سؤال للبحث.")
        else:
            st.warning("Please enter a question.")

    else:

        with st.spinner(
            "جاري البحث..." if language == "العربية"
            else "Searching..."
        ):

            time.sleep(0.5)

        q = question.lower().strip()

        found = False

        for item in documents:

            keywords = item["keywords"]

            for keyword in keywords:

                if str(keyword).lower() in q:

                    found = True

                    if language == "العربية":

                        st.success(
                            "📄 " + item["title_ar"]
                        )

                        st.write(
                            item["answer_ar"]
                        )

                    else:

                        st.success(
                            "📄 " + item["title_en"]
                        )

                        st.write(
                            item["answer_en"]
                        )

                    break

            if found:
                break

        if not found:

            if language == "العربية":

                st.info(
                    "عذرًا، هذه المعلومة غير متوفرة حاليًا."
                )

            else:

                st.info(
                    "Sorry, this information is not available yet."
                )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

if language == "العربية":

    st.caption(
        "AI Public Services Assistant — منصة متخصصة في المعلومات الإدارية."
    )

else:

    st.caption(
        "AI Public Services Assistant — Administrative information platform."
    )
