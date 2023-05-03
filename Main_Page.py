import streamlit as st
from PIL import Image
height=720

st.set_page_config(
    page_title="Easy Chemistry"
)

st.markdown("<h1 style='text-align: center; color: raisin black;'>Easy Chemistry</h1>", unsafe_allow_html=True)
st.subheader("Tanya apa saja ke Fayans")


col1, col2 = st.columns(2)

with col1:
  image1 = Image.open('Resource/image/Main/Fayans.png')
  st.image(image1)
with col2:
    opsi1 = st.button("Asal mula nama Fayans dari mana?")
    opsi2 = st.button("Curhat boleh?")
    opsi3 = st.button("Kayaknya ada yang nge-bug deh, Fayans")
    opsi4 = st.button("Disini ada fitur apa aja, Fayans?")
if opsi2:
    st.write(
        """
        Wah, boleh banget kak!
        
        kakak bisa langsung chat aja akun Fayans [disini](https://wa.me/message/TULJ2JKFOI4HN1). Fayans selalu siap dengerin keluh kesah kakak.
        """)
elif opsi3:
    st.write(
        """
        Wah, kakak bisa langsung kirim saja keluhan kakak di halaman "Report" yang ada di sidebar.
        
        Sini kak, Fayans arahin biar nggak kesasar
        """)
    image2 = Image.open('Resource/image/Main/Tutor1_1.png')
    st.image(image2)
    image2 = Image.open('Resource/image/Main/Tutor1_2.png')
    st.image(image2)
elif opsi4:
    st.write(
        """
        Kakak punya mata, kan? Usaha dikit napa, cari! Bocah-bocah kelompok 4nya udah capek nih //nggak2 canda, nanti ini gw ketik besok
        """)

st.sidebar.success("Select a page above")
