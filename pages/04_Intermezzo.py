import streamlit as st
from PIL import Image

st.markdown("<h1 style='text-align: center; color: raisin black;'>Intermezzo</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: raisin black;'>Isi waktumu dengan info-info menarik tentang unsur kimia</h2>", unsafe_allow_html=True)


image1 = Image.open('Resource/image/Intermezzo/tabel-periodik.jpg')
st.image(image1,caption = "Sumber: scincenotes.org")

optiongolongan = st.selectbox(
  "Pilih materi yang kamu mau",
  ("--- Pilih Golongan ---", "Golongan I", "Golongan II","Golongan III","Golongan IV","Golongan V","Golongan VI","Golongan VII", "Golongan VIII"))

#Golongan I
if optiongolongan == "Golongan I":
  col1, col2, col3, col4 = st.columns(4)
  with col1:
    opsi1 = st.button("Hidrogen")
    opsi5 = st.button("Rubidium")
  with col2:
    opsi2 = st.button("Litium")
    opsi6 = st.button("Sesium")
  with col3:
    opsi3 = st.button("Natrium")
    opsi7 = st.button("Fransium")
  with col4:
    opsi4 = st.button("Kalium")

    
#Golongan II
if optiongolongan == "Golongan II":
  col1, col2, col3, col4 = st.columns(4)
  with col1:
    opsi1 = st.button("Berilium")
  with col2:
    opsi2 = st.button("Magnesium")
    opsi5 = st.button("Barium")
  with col3:
    opsi3 = st.button("Kalsium")
    opsi6 = st.button("Radium")
  with col4:
    opsi4 = st.button("Stronsium")
