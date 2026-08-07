import streamlit as st
from knowledge import knowledge


st.set_page_config(
    page_title="مساعد الوثائق والخدمات العمومية",
    page_icon="🏛️",
    layout="centered"
)


st.title("🏛️ مساعد الوثائق والخدمات العمومية")

st.write(
    "اختر الوثيقة التي تريد معرفة ملفها الإداري، "
    "أو استخدم البحث الحر."
)


# --------------------------------
# Document selector
# --------------------------------

documents = list(knowledge.keys())

selected_document = st.selectbox(
    "📄 اختر الوثيقة",
    ["-- اختر وثيقة --"] + documents
)


# --------------------------------
# Display selected document
# --------------------------------

if selected_document != "-- اختر وثيقة --":

    data = knowledge[selected_document]

    st.header("📄 " + selected_document)

    st.subheader("🏢 الإدارة المعنية")
    st.write(data["administration"])

    st.subheader("📋 الملف الإداري")

    for item in data["file"]:
        st.write("• " + item)

    st.subheader("ℹ️ ملاحظات")
    st.write(data["notes"])

    st.markdown("---")

    st.caption("المصدر الرسمي: وزارة الداخلية والجماعات المحلية والنقل")

    st.link_button(
        "🔗 فتح المصدر الرسمي",
        data["source"]
    )


# --------------------------------
# Free search
# --------------------------------

st.markdown("---")

st.subheader("🔍 البحث الحر")

question = st.text_input(
    "ابحث عن وثيقة أو خدمة",
    placeholder="مثال: جواز السفر، شهادة الميلاد، بطاقة الإقامة..."
)


if st.button("بحث"):

    q = question.strip().lower()

    if q == "":
        st.warning("يرجى إدخال كلمة أو سؤال.")

    else:

        found = False

        for document, data in knowledge.items():

            # Search document name
            if document.lower() in q:

                st.header("📄 " + document)

                st.subheader("🏢 الإدارة المعنية")
                st.write(data["administration"])

                st.subheader("📋 الملف الإداري")

                for item in data["file"]:
                    st.write("• " + item)

                st.subheader("ℹ️ ملاحظات")
                st.write(data["notes"])

                st.link_button(
                    "🔗 المصدر الرسمي",
                    data["source"]
                )

                found = True
                break


            # Search keywords
            for keyword in data["keywords"]:

                if keyword.lower() in q:

                    st.header("📄 " + document)

                    st.subheader("🏢 الإدارة المعنية")
                    st.write(data["administration"])

                    st.subheader("📋 الملف الإداري")

                    for item in data["file"]:
                        st.write("• " + item)

                    st.subheader("ℹ️ ملاحظات")
                    st.write(data["notes"])

                    st.link_button(
                        "🔗 المصدر الرسمي",
                        data["source"]
                    )

                    found = True
                    break

            if found:
                break


        if not found:

            st.info(
                "Sorry, this information is not available yet."
            )
