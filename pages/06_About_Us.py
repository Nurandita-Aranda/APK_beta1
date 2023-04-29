import streamlit as st
from PIL import Image

st.markdown("<h1 style='text-align: center; color: raisin black;'>About Us</h1>", unsafe_allow_html=True)

st.write(" ")

#Nurandita
col1, col2, col3 = st.columns(3)
with col1:
  st.write(" ")
with col2:
  image1 = Image.open('Resource/image/Profile/Nurand.jpg')
  st.image(image1)
with col3:
  st.write(" ")  
st.markdown("<h2 style='text-align: center; color: raisin black;'>Nurandita Aranda Putri</h2>", unsafe_allow_html=True)
st.write("Seorang mahasiswi yang tidak bisa hidup sehari pun tanpa laptopnya")
st.write("email: nuranditaap6@gmail.com")
st.write("instagram: [nurandita_a.p](https://www.instagram.com/nurandita_a.p)")

#Era
st.markdown("<h2 style='text-align: center; color: raisin black;'>Puspita Erawati Surbakti	</h2>", unsafe_allow_html=True)
st.write("blom ada isi")

#Firli
col1, col2, col3 = st.columns(3)
with col1:
  st.write(" ")
with col2:
  image1 = Image.open('Resource/image/Profile/Nabila.jpg')
  st.image(image1)
with col3:
  st.write(" ")
st.markdown("<h2 style='text-align: center; color: raisin black;'>Nabila Firliana Maudy</h2>", unsafe_allow_html=True)
st.write("Tiada hari tanpa musik")
st.write("email: nabilamaudy12345@gmail.com")
st.write("instagram: [nabila_firli1212](https://www.instagram.com/nabila_firli1212)")

#Uswa

#Demas
