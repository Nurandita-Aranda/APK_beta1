import streamlit as st
import random
from PIL import Image

st.markdown("<h1 style='text-align: center; color: raisin black;'>Chimeía Grandprix</h1>", unsafe_allow_html=True)
st.subheader("Siap mengetes kemampuanmu dan menjadi yang terbaik?")


option = st.selectbox(
    "pilih mata kuliah yang kamu inginkan",
    ("--Pilih Mata Kuliah--", "Kimia Dasar","Analisis Jenis","Titrimetri", "Kimia Organik", "Fisika Dasar"))

if option == "Kimia Dasar":
    result = st.select_slider(
        'pilih soal',
        options=['soal 1', 'soal 2', 'soal 3', 'soal 4', 'soal 5', 'soal 6', 'soal 7', "soal 8", "soal 9", "soal 10"])


if option == "Analisis Jenis":
    result = st.select_slider(
        'pilih soal',
        options=['soal 1', 'soal 2', 'soal 3', 'soal 4', 'soal 5', 'soal 6', 'soal 7', "soal 8", "soal 9", "soal 10"])
if result == "soal 1":
        st.write(
            """
Perhatikan persamaan reaksi kimia berikut.

aAgNO3 + 2H2O → bAg + O2 + cHNO3

agar persamaan diatas dapat setara, maka a, b, dan c adalah

            """)
        col1, col2 = st.columns(2)
        with col1:
            opsi1 = st. button("4,2,dan4")
            opsi2 = st. button("4,4,dan2")
        with col2:
            opsi3 = st. button("4,4,dan4")
            opsi4 = st. button("4,3,dan2")
        if opsi1:
            st.markdown("<h2 style='text-align: center; color: red;'>Salah!!</h2>", unsafe_allow_html=True)
            st.error('Coba lagi!')
        elif opsi2:
            st.markdown("<h2 style='text-align: center; color: red;'>Salah!!</h2>", unsafe_allow_html=True)
            st.error('Coba lagi!')
        elif opsi3:
            st.markdown("<h2 style='text-align: center; color: red;'>Benar!!</h2>", unsafe_allow_html=True)
            st.success("soal selanjutnya!")
            st.balloons()
        elif opsi4:
            st.markdown("<h2 style='text-align: center; color: green;'>Benar!!</h2>", unsafe_allow_html=True)
            st.error('Coba lagi!')
    
if option == "Titrimetri":
    result = st.select_slider(
        'pilih soal',
        options=['soal 1', 'soal 2', 'soal 3', 'soal 4', 'soal 5', 'soal 6', 'soal 7', "soal 8", "soal 9", "soal 10"])
    

if option == "Kimia Organik":
    result = st.select_slider(
        'pilih soal',
        options=['soal 1', 'soal 2', 'soal 3', 'soal 4', 'soal 5', 'soal 6', 'soal 7', "soal 8", "soal 9", "soal 10"])
    if result == "soal 1":
        imageKO1 = Image.open('Resource/image/Quiz_Kimor/Soal_1.png')
        st.image(imageKO1)
        col1, col2 = st.columns(2)
        with col1:
            opsi1 = st.button("2-metil-1,3,5-trinitrobenzena")
            opsi2 = st.button("1,3,5-trinitro-2-metilbenzena")
        with col2:
            opsi3 = st.button("6-metil-1,3,5-trinitrobenzena")
            opsi4 = st.button("1-metil-2,4,6-trinitrobenzena")
        if opsi1:
            st.markdown("<h2 style='text-align: center; color: green;'>Benar!!</h2>", unsafe_allow_html=True)
            st.success("soal selanjutnya!")
            st.balloons()
        elif opsi2:
            st.markdown("<h2 style='text-align: center; color: red;'>Salah!!</h2>", unsafe_allow_html=True)
            st.error('Coba lagi!')
        elif opsi3:
            st.markdown("<h2 style='text-align: center; color: red;'>Salah!!</h2>", unsafe_allow_html=True)
            st.error('Coba lagi!')
        elif opsi4:
            st.markdown("<h2 style='text-align: center; color: red;'>Salah!!</h2>", unsafe_allow_html=True)
            st.error('Coba lagi!')
    if result == "soal 2":
        imageKO2 = Image.open('Resource/image/Quiz_Kimor/Soal_2.png')
        st.image(imageKO2)
        col1, col2 = st.columns(2)
        with col1:
            opsi1 = st. button("3,5-diamino-1-hidroksilbenzena")
            opsi2 = st. button("3,5-diaminofenol")
        with col2:
            opsi3 = st. button("1,3-diaminofenol")
            opsi4 = st. button("1,3-diamino-5-hidroksilbenzena")
        if opsi1:
            st.markdown("<h2 style='text-align: center; color: red;'>Salah!!</h2>", unsafe_allow_html=True)
            st.error('Coba lagi!')
        elif opsi2:
            st.markdown("<h2 style='text-align: center; color: green;'>Benar!!</h2>", unsafe_allow_html=True)
            st.success("soal selanjutnya!")
            st.balloons()
        elif opsi3:
            st.markdown("<h2 style='text-align: center; color: red;'>Salah!!</h2>", unsafe_allow_html=True)
            st.error('Coba lagi!')
        elif opsi4:
            st.markdown("<h2 style='text-align: center; color: red;'>Salah!!</h2>", unsafe_allow_html=True)
            st.error('Coba lagi!')
    if result == "soal 3":
        st.write("Berikut ini yang dapat digunakan untuk membedakan alkohol dan fenol adalah...")
        col1, col2 = st.columns(2)
        with col1:
            opsi1 = st. button("Kanji")
            opsi2 = st. button("KMnO4")
        with col2:
            opsi3 = st. button("Natrium bisulfit")
            opsi4 = st. button("FeCl3")
        if opsi1:
            st.markdown("<h2 style='text-align: center; color: red;'>Salah!!</h2>", unsafe_allow_html=True)
            st.error('Coba lagi!')
        elif opsi2:
            st.markdown("<h2 style='text-align: center; color: red;'>Salah!!</h2>", unsafe_allow_html=True)
            st.error('Coba lagi!')
        elif opsi3:
            st.markdown("<h2 style='text-align: center; color: red;'>Salah!!</h2>", unsafe_allow_html=True)
            st.error('Coba lagi!')
        elif opsi4:
            st.markdown("<h2 style='text-align: center; color: green;'>Benar!!</h2>", unsafe_allow_html=True)
            st.success("soal selanjutnya!")
            st.balloons()
