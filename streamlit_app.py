import streamlit as st

st.set_page_config(
    page_title="Andrew Wijaya",
    page_icon="🧑‍💻",
    layout="wide"
)

st.title("Andrew Wijaya")

st.subheader("Welcome to website Andrew Wijaya")
st.write("SMAN 20 Bandung")
st.image(
    "https://1.bp.blogspot.com/-lygs2wtQzgk/Ufk2tlT_cOI/AAAAAAAAAGU/duIUyTw3Ues/s1600/troll_face8.png",
    width=200,
    caption="XD.Lmaoo"
)

col1, col2 = st.columns(2)
with col1:
    st.header("About Me?")
    st.write(
        "Greetings Visitor☺️ Lemme introduce myself, my name is Andrew Wijaya. "
        "Currently I am grade 10 studying at SMAN 20 Bandung rn."
    )
with col2:
    st.header("Things I love?")
    st.write(
        "I love sport like karate and learn about cybersecurity because I love it. "
        "It becomes my entertainment compared to playing games, yeah maybe I've played it once.. uhm, lol."
    )

audio_url = "https://j.top4top.io/m_3445t8myu1.mp3"
st.audio(audio_url, format='audio/mp3', start_time=0)
