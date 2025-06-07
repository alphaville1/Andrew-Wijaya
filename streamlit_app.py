import streamlit as st

st.title("Andrew Wijaya")
st.subheader("Selamat datang di website Andrew Wijaya")
st.write("SMAN 20 Bandung")

st.image("link", width=300, caption="Persib Juara 2025")

col1, col2 = st.columns(2)
with col1:
    st.header("About Andrew Wijaya")
    st.write("Greetings Visitor☺️ Lemme introduce myself, my name is Andrew Wijaya currently I am studying at SMAN 20 Bandung and sit in class X rn.")
with col2:
    st.header("Things I love?")
    st.write("I love sport like karate and learn about hacking because i love it and it becomes my entertainment compared to playing shit games... uhm.")
