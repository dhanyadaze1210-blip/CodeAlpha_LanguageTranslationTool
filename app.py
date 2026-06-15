import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(
    page_title="LinguaX - Language Translator",
    page_icon="🌐",
    layout="centered"
)

st.title("🌐 LinguaX")
st.caption("Translate text instantly across 14 languages")

st.divider()

LANGUAGES = {
    "🇬🇧 English":              "english",
    "🇫🇷 French":               "french",
    "🇪🇸 Spanish":              "spanish",
    "🇩🇪 German":               "german",
    "🇮🇳 Hindi":                "hindi",
    "🇮🇳 Tamil":                "tamil",
    "🇯🇵 Japanese":             "japanese",
    "🇨🇳 Chinese (Simplified)": "chinese (simplified)",
    "🇹🇼 Chinese (Traditional)":"chinese (traditional)",
    "🇰🇷 Korean":               "korean",
    "🇦🇪 Arabic":               "arabic",
    "🇷🇺 Russian":              "russian",
    "🇵🇹 Portuguese":           "portuguese",
    "🇮🇹 Italian":              "italian",
}

display_names = list(LANGUAGES.keys())

col1, col2 = st.columns(2)

with col1:
    source_display = st.selectbox("Source Language", display_names, index=0)

with col2:
    target_display = st.selectbox("Target Language", display_names, index=4)

source_lang = LANGUAGES[source_display]
target_lang = LANGUAGES[target_display]

st.divider()

text = st.text_area(
    "Enter text to translate",
    placeholder="Type something here...",
    height=150
)

col_a, col_b, col_c = st.columns([1, 2, 1])
with col_b:
    translate_clicked = st.button("✨ Translate", use_container_width=True)

st.divider()

if translate_clicked:
    if not text.strip():
        st.warning("⚠️ Please enter some text before translating.")
    elif source_lang == target_lang:
        st.info("💡 Source and target languages are the same!")
    else:
        with st.spinner("Translating..."):
            try:
                translated = GoogleTranslator(
                    source=source_lang,
                    target=target_lang
                ).translate(text)

                st.success("✅ Translation complete!")

                st.subheader(f"Result in {target_display}")
                st.info(translated)

                col_x, col_y = st.columns(2)
                with col_x:
                    st.metric(label="From", value=source_display)
                with col_y:
                    st.metric(label="To", value=target_display)

            except Exception as e:
                st.error(f"❌ Translation failed: {str(e)}")

st.divider()
st.caption("Built with Python & Streamlit · CodeAlpha AI Internship 2026 · Dhanya R")