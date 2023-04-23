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

        agar persamaan diatas dapat setara, maka a, b, dan c adalah...
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
            st.markdown("<h2 style='text-align: center; color: green;'>Benar!!</h2>", unsafe_allow_html=True)
            st.success("soal selanjutnya!")
            st.balloons()
        elif opsi4:
            st.markdown("<h2 style='text-align: center; color: red;'>salah!!</h2>", unsafe_allow_html=True)
            st.error('Coba lagi!')
            
    if result == "soal 2":
        st.write(
            """
        Bila Permanganat dipanasi dengan basa akan terjadi reaksi redoks, persamaan reaksi yang tepat sehingga terbentuk oksigen adalah...
        """)
        col1, col2 = st.columns(2)
        with col1:
            opsi1 = st. button("4MnO4 + 4OH- → 4MnO42- + 2H2O + O2")
            opsi2 = st. button("MnO4 + 4OH → -1MnO2 + 2MnO4 + 2H2O")
        with col2:
            opsi3 = st. button("4MnO4 +2OH- → 4MnO42- + 2H2O + O2")
            opsi4 = st. button("MnO4 +2OH- → MnO42- + 2H2O + O2")
        if opsi1:
            st.markdown("<h2 style='text-align: center; color: green;'>Benar!!</h2>", unsafe_allow_html=True)
            st.success("soal selanjutnya!")
            st.balloons()
        elif opsi2:
            st.markdown("<h2 style='text-align: center; color: red;'>Salah!!</h2>", unsafe_allow_html=True)
            st.error('Coba lagi!')
        elif opsi3:
            st.markdown("<h2 style='text-align: center; color: red;'>salah!!</h2>", unsafe_allow_html=True)
            st.error('Coba lagi!')  
        elif opsi4:
            st.markdown("<h2 style='text-align: center; color: red;'>salah!!</h2>", unsafe_allow_html=True)
            st.error('Coba lagi!')
            
    if result == "soal 3":
        st.write(
            """
        Perak hidroksida akan mengalami disosiasi Ketika dilarutkan dalam air reksi yang tepat adalah...
        """)
        col1, col2 = st.columns(2)
        with col1:
            opsi1 = st. button("AgNO3 + 2H2O → Ag + O2 + HNO3")
            opsi2 = st. button("Ag(OH) + OH → Ag + OH")
        with col2:
            opsi3 = st. button("Ag(OH)2 + OH → Ag + 3OH")
            opsi4 = st. button("2Ag(OH) + 4OH → 2Ag + 3H2O")
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
            
    if result == "soal 4":
        st.write(
            """
        Tuliskan Persamaan reaksi proses pengkaratan pada besi...
        """)
        col1, col2 = st.columns(2)
        with col1:
            opsi1 = st. button("2Fe2O3xH2O → Fe(OH)2+O2+H2O")
            opsi2 = st. button("2Fe+ O2+ 4H- → 2Fe2-+2H2O")
            
    if result == "soal 5":
        st.write(
            """
        Larutan HCL dalam air memiliki kadar 50 %. Hitunglah fraksi mol HCL dalam larutan tersebut (Mr HCL= 36,5)...
        """)
        col1, col2 = st.columns(2)
        with col1:
            opsi1 = st. button("27,4 mol")
            opsi2 = st. button("27,39 mol")
        with col2:
            opsi3 = st. button("25 mol")
            opsi4 = st. button("26 mol")
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
        
    if result == "soal 6":
        st.write(
            """
        Larutan Sorensen 10% b/v, memiliki PPM sebesar...
        """)
        col1, col2 = st.columns(2)
        with col1:
            opsi1 = st. button("1000000 ppm")
            opsi2 = st. button("0,00001 ppm")
        with col2:
            opsi3 = st. button("10000")
            opsi4 = st. button("1000")
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
            
    if result == "soal 7":
        st.write(
            """
        Berapa gram yang di butuhkan untuk membuat larutan NaoH 0,5 mol (Mr= 40)...
        """)
        col1, col2 = st.columns(2)
        with col1:
            opsi1 = st. button("20 g")
            opsi2 = st. button("20,5 g")
        with col2:
            opsi3 = st. button("10,5 g")
            opsi4 = st. button("21 g")
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
            
    if result == "soal 8":
        st.write(
            """
        Larutan 0,2 molal H2SO4 terbuat dari 40 gram H2SO4 dengan...
        """)
        col1, col2 = st.columns(2)
        with col1:
            opsi1 = st. button("2040,83")
            opsi2 = st. button("2140,83")
        with col2:
            opsi3 = st. button("2039,82")
            opsi4 = st. button("2040,82")
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
