import streamlit as st

st.markdown("<h1 style='text-align: center; color: raisin black;'>About Us</h1>", unsafe_allow_html=True)

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
st.write("email    : nuranditaap6@gmail.com")
st.write("instagram: nurandita_a.p")

#Era
