import streamlit as st
from knowledge import knowledge
import unicodedata


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="AI Public Services Assistant",
    page_icon="🏛️",
    layout="centered"
)


# --------------------------------------------------
# TEXT NORMALIZATION
# --------------------------------------------------

def normalize_text(text):
    if text is None:
        return ""

    text = str(text).lower().strip()

    # Normalize Arabic characters
    text = text.replace("أ", "ا")
    text = text.replace("إ", "ا")
    text = text.replace("آ", "ا")
    text = text.replace("ى", "ي")
    text = text.replace("ة", "ه")

    # Remove Arabic diacritics
    text = "".join(
        char
        for char in unicodedata.normalize("NFD", text)
        if unicodedata.category(char) != "Mn"
    )

    return " ".join(text.split())


# --------------------------------------------------
# SEARCH ENGINE
# --------------------------------------------------

def find_service(query):

    q = normalize_text(query)

    if not q:
        return None

    best_service = None
    best_score = 0

    for service_id, service in knowledge.items():

        score = 0

        all_keywords = (
            service.get("keywords_ar", [])
            + service.get("keywords_en", [])
        )

        for keyword in all_keywords:

            k = normalize_text(keyword)

            if not k:
                continue

            # Exact phrase
            if k in q:
                score += len(k)

            # Individual words
            else:
                words = k.split()

                for word in words:
                    if len(word) >= 2 and word in q:
                        score += 1

        if score > best_score:
            best_score = score
            best_service = service

    return best_service


# --------------------------------------------------
# DISPLAY SERVICE
# --------------------------------------------------

def display_service(service, language="ar"):

    if service is None:
        st.info("Sorry, this information is not available yet.")
        return

    if language == "ar":

        title = service.get("title_ar", "وثيقة")
        administration = service.get(
            "administration_ar",
            "غير محدد"
        )
        file_info = service.get(
            "file_ar",
            "المعلومات غير متوفرة حاليا."
        )
        notes = service.get(
            "notes_ar",
            ""
        )

        st.markdown("---")

        st.markdown(
            f"# 📄 {title}"
        )

        st.markdown(
            f"### 🏢 الإدارة المختصة\n"
            f"{administration}"
        )

        st.markdown(
            "### 📋 الملف والوثائق المطلوبة"
        )

        st.markdown(file_info)

        if notes.strip():
            st.markdown("### ℹ️ معلومات إضافية")
            st.markdown(notes)

        st.caption(
            "المصدر: وزارة الداخلية والجماعات المحلية والنقل"
        )

    else:

        title = service.get("title_en", "Document")
        administration = service.get(
            "administration_en",
            "Not specified"
        )
        file_info = service.get(
            "file_en",
            "Information is not currently available."
        )
        notes = service.get(
            "notes_en",
            ""
        )

        st.markdown("---")

        st.markdown(
            f"# 📄 {title}"
        )

        st.markdown(
            f"### 🏢 Competent Administration\n"
            f"{administration}"
        )

        st.markdown(
            "### 📋 Required Documents"
        )

        st.markdown(file_info)

        if notes.strip():
            st.markdown("### ℹ️ Additional Information")
            st.markdown(notes)

        st.caption(
            "Source: Ministry of Interior, Local Authorities and Transport"
        )


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("🏛️ AI Public Services Assistant")

st.write(
    """
منصة متخصصة للوصول السريع إلى المعلومات المتعلقة
بالوثائق والملفات الإدارية في الجزائر.
"""
)

st.write(
    "اختر الوثيقة مباشرة أو استخدم البحث الحر."
)


# --------------------------------------------------
# LANGUAGE
# --------------------------------------------------

language = st.radio(
    "🌐 اللغة / Language",
    ["العربية", "English"],
    horizontal=True
)

current_language = "ar" if language == "العربية" else "en"


# --------------------------------------------------
# DOCUMENT LIST
# --------------------------------------------------

if current_language == "ar":

    document_ids = list(knowledge.keys())

    document_labels = [
        knowledge[item]["title_ar"]
        for item in document_ids
    ]

    selected_label = st.selectbox(
        "📄 اختر الوثيقة",
        ["-- اختر الوثيقة --"] + document_labels
    )

else:

    document_ids = list(knowledge.keys())

    document_labels = [
        knowledge[item]["title_en"]
        for item in document_ids
    ]

    selected_label = st.selectbox(
        "📄 Select a document",
        ["-- Select a document --"] + document_labels
    )


# --------------------------------------------------
# SHOW SELECTED DOCUMENT
# --------------------------------------------------

if selected_label != "-- اختر الوثيقة --" and \
   selected_label != "-- Select a document --":

    selected_service = None

    for service_id in document_ids:

        if current_language == "ar":

            if knowledge[service_id]["title_ar"] == selected_label:
                selected_service = knowledge[service_id]
                break

        else:

            if knowledge[service_id]["title_en"] == selected_label:
                selected_service = knowledge[service_id]
                break

    display_service(
        selected_service,
        current_language
    )


# --------------------------------------------------
# FREE SEARCH
# --------------------------------------------------

st.markdown("---")

if current_language == "ar":

    st.subheader("🔎 البحث الحر")

    question = st.text_input(
        "اكتب اسم الوثيقة أو كلمات مرتبطة بها",
        placeholder="مثال: بطاقة التعريف، residence، id card، جواز السفر..."
    )

    search_button = st.button(
        "🔍 بحث",
        use_container_width=True
    )

else:

    st.subheader("🔎 Free Search")

    question = st.text_input(
        "Enter the document name or related keywords",
        placeholder="Example: passport, residence, id card..."
    )

    search_button = st.button(
        "🔍 Search",
        use_container_width=True
    )


# --------------------------------------------------
# SEARCH RESULT
# --------------------------------------------------

if search_button:

    if not question.strip():

        if current_language == "ar":
            st.warning("يرجى إدخال اسم الوثيقة أو كلمة للبحث.")
        else:
            st.warning("Please enter a document name or keyword.")

    else:

        result = find_service(question)

        if result is None:

            st.info(
                "Sorry, this information is not available yet."
            )

        else:

            display_service(
                result,
                current_language
            )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")

st.caption(
    "AI Public Services Assistant • Administrative Documents & Procedures"
)
