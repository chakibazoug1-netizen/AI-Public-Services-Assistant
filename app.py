import streamlit as st
from knowledge import knowledge

st.set_page_config(
    page_title="AI Public Services Assistant",
    page_icon="🏛️",
    layout="centered"
)

# -----------------------------
# Language
# -----------------------------

language = st.radio(
    "🌐 اللغة / Language",
    ["العربية", "English"],
    horizontal=True
)

is_arabic = language == "العربية"


# -----------------------------
# Page title
# -----------------------------

if is_arabic:
    st.title("🏛️ مساعد الخدمات العمومية بالذكاء الاصطناعي")

    st.write(
        """
        منصة متخصصة للوصول السريع إلى المعلومات المتعلقة
        بالوثائق والملفات الإدارية في الجزائر.

        اختر الوثيقة مباشرة أو استخدم البحث الحر.
        """
    )

else:
    st.title("🏛️ AI Public Services Assistant")

    st.write(
        """
        A specialized platform for fast access to information
        about administrative documents and procedures in Algeria.

        Select a document directly or use the free search.
        """
    )


# -----------------------------
# Document list
# -----------------------------

document_titles = []

for item in knowledge:
    if is_arabic:
        document_titles.append(item["title_ar"])
    else:
        document_titles.append(item["title_en"])


# -----------------------------
# Document selector
# -----------------------------

if is_arabic:
    st.subheader("📄 اختر الوثيقة")
else:
    st.subheader("📄 Select a document")


selected_document = st.selectbox(
    "Document",
    [""] + document_titles,
    label_visibility="collapsed"
)


# -----------------------------
# Show selected document
# -----------------------------

if selected_document != "":

    selected_item = None

    for item in knowledge:

        current_title = (
            item["title_ar"]
            if is_arabic
            else item["title_en"]
        )

        if current_title == selected_document:
            selected_item = item
            break

    if selected_item is not None:

        if is_arabic:

            st.header(
                "📄 " + selected_item["title_ar"]
            )

            st.write(
                selected_item["answer_ar"]
            )

        else:

            st.header(
                "📄 " + selected_item["title_en"]
            )

            st.write(
                selected_item["answer_en"]
            )


# -----------------------------
# Free search
# -----------------------------

if is_arabic:
    st.subheader("🔎 البحث الحر")

    question = st.text_input(
        "اكتب اسم الوثيقة أو ما تبحث عنه"
    )

    search_button = st.button(
        "🔍 بحث"
    )

else:
    st.subheader("🔎 Free Search")

    question = st.text_input(
        "Enter the document or information you are looking for"
    )

    search_button = st.button(
        "🔍 Search"
    )


# -----------------------------
# Search engine
# -----------------------------

if search_button:

    if question.strip() == "":

        if is_arabic:
            st.warning("⚠️ يرجى إدخال كلمة أو سؤال للبحث.")
        else:
            st.warning("⚠️ Please enter a word or question.")

    else:

        q = question.strip().lower()

        found = False

        for item in knowledge:

            # Search in keywords
            for keyword in item["keywords"]:

                if keyword.lower() in q:

                    found = True

                    if is_arabic:

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

        # -----------------------------
        # Not found
        # -----------------------------

        if not found:

            if is_arabic:
                st.info(
                    "ℹ️ عذراً، هذه المعلومة غير متوفرة حالياً."
                )

            else:
                st.info(
                    "ℹ️ Sorry, this information is not available yet."
                )


# -----------------------------
# Footer
# -----------------------------

st.divider()

if is_arabic:

    st.caption(
        "المعلومات موجهة للاستعلام العام، ويجب التحقق من آخر تحديث رسمي قبل إيداع أي ملف."
    )

else:

    st.caption(
        "Information is provided for general guidance. "
        "Please verify the latest official requirements before submitting an administrative file."
    )
