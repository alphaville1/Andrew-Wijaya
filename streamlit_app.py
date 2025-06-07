import streamlit as st

st.title("Andrew Wijaya")
st.subheader("Welcome to website Andrew Wijaya")
st.write("SMAN 20 Bandung")

st.image("https://ibb.co/1G7BShz0", width=200, caption="XD.Lmaoo")

col1, col2 = st.columns(2)
with col1:
    st.header("About Andrew Wijaya")
    st.write("Greetings Visitor☺️ Lemme introduce myself, my name is Andrew Wijaya currently I am grade 10 studying at SMAN 20 Bandung rn.")
with col2:
    st.header("Things I love?")
    st.write("I love sport like karate and learn about cybersecurity because i love it and becomes my entertainment compared to playing games, yeah maybe i've played it once.. uhm, lol.")

import streamlit as st

audio_url = "https://j.top4top.io/m_3445t8myu1.mp3"
st.audio(audio_url, format='audio/mp3', start_time=0)
