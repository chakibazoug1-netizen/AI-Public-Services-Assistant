import streamlit as st
from knowledge import knowledge

st.set_page_config(
    page_title="AI Public Services Assistant",
    page_icon="🏛️",
    layout="centered"
)

# =========================
# HEADER
# =========================

st.title("🏛️ AI Public Services Assistant")

st.write(
    """
    منصة متخصصة للوصول السريع إلى المعلومات المتعلقة
    بالوثائق والملفات الإدارية في الجزائر.
    """
)

st.write("اختر الوثيقة مباشرة أو استخدم البحث الحر.")

# =========================
# LANGUAGE
# =========================

language = st.radio(
    "🌐 اللغة / Language",
    ["العربية", "English"],
    horizontal=True
)

# =========================
# DOCUMENT LIST
# =========================

if language == "العربية":
    document_options = ["اختر الوثيقة..."]

    for item in knowledge:
        document_options.append(
            item.get("title_ar", "وثيقة")
        )

else:
    document_options = ["Select a document..."]

    for item in knowledge:
        document_options.append(
            item.get("title_en", "Document")
        )

# =========================
# DOCUMENT SELECTOR
# =========================

selected_document = st.selectbox(
    "📄 اختر الوثيقة",
    document_options
)

# =========================
# SHOW SELECTED DOCUMENT
# =========================

if selected_document not in [
    "اختر الوثيقة...",
    "Select a document..."
]:

    selected_data = None

    for item in knowledge:

        if language == "العربية":

            if item.get("title_ar") == selected_document:
                selected_data = item
                break

        else:

            if item.get("title_en") == selected_document:
                selected_data = item
                break

    if selected_data is not None:

        if language == "العربية":

            st.subheader(
                "📄 " + selected_data.get(
                    "title_ar",
                    "وثيقة"
                )
            )

            st.write(
                selected_data.get(
                    "answer_ar",
                    "المعلومات غير متوفرة حاليا."
                )
            )

        else:

            st.subheader(
                "📄 " + selected_data.get(
                    "title_en",
                    "Document"
                )
            )

            st.write(
                selected_data.get(
                    "answer_en",
                    "Information is not available yet."
                )
            )

# =========================
# FREE SEARCH
# =========================

st.divider()

if language == "العربية":
    st.subheader("🔎 البحث الحر")
    search_placeholder = "اكتب اسم الوثيقة أو كلمة للبحث..."
else:
    st.subheader("🔎 Free Search")
    search_placeholder = "Enter a document or keyword..."

question = st.text_input(
    "البحث",
    placeholder=search_placeholder
)

if st.button("🔍 Search"):

    if question.strip() == "":

        if language == "العربية":
            st.warning("يرجى إدخال كلمة أو اسم الوثيقة.")
        else:
            st.warning("Please enter a document or keyword.")

    else:

        q = question.strip().lower()

        found = False

        for item in knowledge:

            keywords = item.get("keywords", [])

            for keyword in keywords:

                if keyword.lower() in q:

                    found = True

                    if language == "العربية":

                        st.success(
                            item.get(
                                "title_ar",
                                "الوثيقة"
                            )
                        )

                        st.write(
                            item.get(
                                "answer_ar",
                                "المعلومات غير متوفرة حاليا."
                            )
                        )

                    else:

                        st.success(
                            item.get(
                                "title_en",
                                "Document"
                            )
                        )

                        st.write(
                            item.get(
                                "answer_en",
                                "Information is not available yet."
                            )
                        )

                    break

            if found:
                break

        if not found:

            if language == "العربية":

                st.info(
                    "عذرا، هذه المعلومات غير متوفرة حاليا."
                )

            else:

                st.info(
                    "Sorry, this information is not available yet."
                )

# =========================
# FOOTER
# =========================

st.divider()

st.caption(
    "AI Public Services Assistant — معلومات إدارية مبسطة وسريعة"
)
