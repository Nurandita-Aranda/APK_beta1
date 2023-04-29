import streamlit as st
height=720

st.set_page_config(
    page_title="Easy Chemistry"
)

st.markdown("<h1 style='text-align: center; color: raisin black;'>Easy Chemistry</h1>", unsafe_allow_html=True)
st.subheader("Tanya apa saja ke Pollo")

Opsi1 = st.button("Curhat boleh?")
if opsi1:
    st.write(
        """
        Wah, boleh banget kak!
        
        kakak bisa langsung chat aja akun Fayans [>disini<](https://wa.me/message/TULJ2JKFOI4HN1). Fayans selalu siap dengerin keluh kesah kakak.
        """)

opsi2 = st.button("Kayaknya ada yang nge-bug deh, Fayans"):
if opsi2:
    st.write(
        """
        Wah, kakak bisa langsung kirim saja keluhan kakak di halaman "report" yang ada di sidebar.
        
        Sini kak, Fayans arahin biar nggak kesasar
        """)

st.sidebar.success("Select a page above")
