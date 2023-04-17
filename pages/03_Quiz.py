import streamlit as st

st.markdown("<h1 style='text-align: center; color: raisin black;'>Chimeía Grandprix</h1>", unsafe_allow_html=True)
st.subheader("Siap mengetes kemampuanmu dan menjadi yang terbaik?")

option = st.selectbox(
    "pilih mata kuliah yang kamu inginkan",
    ("Kimia Dasar","Analisis Jenis","Titrimetri", "Kimia Organik", "Fisika Dasar"))