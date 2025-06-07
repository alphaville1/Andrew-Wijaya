import streamlit as st

st.set_page_config(
    page_title="Welcome Gentle Man",
    page_icon="🧑‍💻",
    layout="wide"
)

st.title("Welcome to My Websites")
st.image(
    "https://1.bp.blogspot.com/-lygs2wtQzgk/Ufk2tlT_cOI/AAAAAAAAAGU/duIUyTw3Ues/s1600/troll_face8.png",
    width=450,
    caption="welcome gentleman"
)
st.subheader("Andrew Wijaya")
st.write("Learn coding with me🤓")

col1, col2 = st.columns(2)
with col1:
    st.header("About Me?")
    st.write(
        "Greetings Visitor☺️ Lemme introduce myself, my name is Andrew Wijaya 16 y.o , "
        "You wanna asking where I am from? I from ur heart😋 lmaoo. " 
        "Currently I'm grade 10 studying at SMAN 20 Bandung rn."
    )
with col2:
    st.header("Things I love?")
    st.write(
        "I love Mommy ofc😋 lol, I love sport like karate and learn about cybersecurity because I love it becomes my entertainment compared to playing games, yeah maybe I've played it once.. uhm."
    )

st.subheader("Play Music at here⬇️")
audio_url = "https://j.top4top.io/m_3445t8myu1.mp3"
st.audio(audio_url, format='audio/mp3', start_time=0)
