import streamlit as st

st.title("Andrew Wijaya")
st.subheader("Welcome to website Andrew Wijaya")
st.write("SMAN 20 Bandung")

st.image("https://i.ibb.co/0STQbRr/7149e6635fef.jpg", width=300, caption="XD.Lmaoo")

col1, col2 = st.columns(2)
with col1:
    st.header("About Andrew Wijaya")
    st.write("Greetings Visitor☺️ Lemme introduce myself, my name is Andrew Wijaya currently I am grade 10 studying at SMAN 20 Bandung rn.")
with col2:
    st.header("Things I love?")
    st.write("I love sport like karate and learn about cybersecurity because i love it and it becomes my entertainment compared to playing games, yeah maybe i've played it once.. uhm, lol.")
