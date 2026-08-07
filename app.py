import streamlit as st
from knowledge import knowledge

st.set_page_config(
    page_title="AI Public Services Assistant",
    page_icon="🏛️",
    layout="centered"
)

# --------------------------------
# Language
# --------------------------------

language = st.radio(
    "🌐 اللغة / Language",
    ["العربية", "English"],
    horizontal=True
)

arabic = language == "العربية"


# --------------------------------
# Header
# --------------------------------

if arabic:

    st.title("🏛️ مساعد الخدمات العمومية")

    st.write(
        "منصة متخصصة للوصول السريع إلى المعلومات المتعلقة "
        "بالوثائق والملفات الإدارية في الجزائر."
    )

else:

    st.title("🏛️ AI Public Services Assistant")

    st.write(
        "A specialized platform for fast access to information "
        "about administrative documents and procedures in Algeria."
    )


# --------------------------------
# Document selector
# --------------------------------

if arabic:
    st.subheader("📄 اختر الوثيقة")
else:
    st.subheader("📄 Select a document")


document_options = [""]

for key, data in knowledge.items():

    if arabic:
        document_options.append(data["title_ar"])
    else:
        document_options.append(data["title_en"])


selected = st.selectbox(
    "document",
    document_options,
    label_visibility="collapsed"
)


# --------------------------------
# Display selected document
# --------------------------------

if selected != "":

    for key, data in knowledge.items():

        title = (
            data["title_ar"]
            if arabic
            else data["title_en"]
        )

        if selected == title:

            if arabic:
                st.header("📄 " + data["title_ar"])
                st.write(data["answer_ar"])
            else:
                st.header("📄 " + data["title_en"])
                st.write(data["answer_en"])

            break


# --------------------------------
# Free search
# --------------------------------

if arabic:

    st.subheader("🔎 البحث الحر")

    question = st.text_input(
        "اكتب اسم الوثيقة أو كلمة تبحث عنها"
    )

    search_button = st.button("🔍 بحث")

else:

    st.subheader("🔎 Free Search")

    question = st.text_input(
        "Enter a document or keyword"
    )

    search_button = st.button("🔍 Search")


# --------------------------------
# Search
# --------------------------------

if search_button:

    q = question.strip().lower()

    if q == "":

        if arabic:
            st.warning("⚠️ يرجى إدخال كلمة للبحث.")
        else:
            st.warning("⚠️ Please enter a search term.")

    else:

        found = False

        for key, data in knowledge.items():

            # Search in document key
            if q in key.lower():

                found = True

            # Search in keywords
            if not found:

                for keyword in data["keywords"]:

                    if keyword.lower() in q or q in keyword.lower():

                        found = True
                        break

            if found:

                if arabic:

                    st.success(
                        "📄 " + data["title_ar"]
                    )

                    st.write(
                        data["answer_ar"]
                    )

                else:

                    st.success(
                        "📄 " + data["title_en"]
                    )

                    st.write(
                        data["answer_en"]
                    )

                break


        # --------------------------------
        # Not found
        # --------------------------------

        if not found:

            if arabic:

                st.info(
                    "ℹ️ عذراً، هذه المعلومة غير متوفرة حالياً."
                )

            else:

                st.info(
                    "ℹ️ Sorry, this information is not available yet."
                )


# --------------------------------
# Footer
# --------------------------------

st.divider()

if arabic:

    st.caption(
        "المعلومات للاستعلام العام. يرجى التحقق من آخر تحديث رسمي قبل إيداع أي ملف."
    )

else:

    st.caption(
        "Information is provided for general guidance. "
        "Please verify the latest official requirements before submitting a file."
    )
