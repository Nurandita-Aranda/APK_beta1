import streamlit as st
import webbrowser
height=720

st.set_page_config(
    page_title="Easy Chemistry"
)

st.markdown("<h1 style='text-align: center; color: raisin black;'>Easy Chemistry</h1>", unsafe_allow_html=True)
st.subheader("Tanya apa saja ke Pollo")

url = 'https://wa.me/message/TULJ2JKFOI4HN1'
if st.button("Curhat boleh?"):
    webbrowser.open_new_tab(url)
url1 = 'https://www.youtube.com/'
if st.button("Kayaknya ada yang nge-bug deh, Fayans"):
    webbrowser.open_new_tab(url1)

st.sidebar.success("Select a page above")
