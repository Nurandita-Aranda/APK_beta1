import streamlit as st
import webbrowser

st.markdown("<h1 style='text-align: center; color: raisin black;'>Alchemist Diary</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: raisin black;'>Mari berpetualang di kerajaan Chimeía</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.write(" ")
with col2:
    if st.button(st.write("[link](https://drive.google.com/file/d/1Slheotw7HAcpZ-uEzV7PkO1ingI3lATo/view?usp=sharing)"):
        
with col3:
    st.write(" ")
