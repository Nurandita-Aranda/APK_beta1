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
            st.markdown("<h2 style='text-align: center; color: red;'>Salah!!</h2>", unsafe_allow_html=True)
            st.error('Coba lagi!')
            
    if result == "soal 2":
        st.write("Bila Permanganat dipanasi dengan basa akan terjadi reaksi redoks, persamaan reaksi yang tepat sehingga terbentuk oksigen adalah...")
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
            st.markdown("<h2 style='text-align: center; color: red;'>Salah!!</h2>", unsafe_allow_html=True)
            st.error('Coba lagi!')  
        elif opsi4:
            st.markdown("<h2 style='text-align: center; color: red;'>Salah!!</h2>", unsafe_allow_html=True)
            st.error('Coba lagi!')
            
    if result == "soal 3":
        st.write("Perak hidroksida akan mengalami disosiasi Ketika dilarutkan dalam air reksi yang tepat adalah...")
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
        st.write("Tuliskan Persamaan reaksi proses pengkaratan pada besi...")
        col1, col2 = st.columns(2)
        with col1:
            opsi1 = st. button("2Fe2O3xH2O → Fe(OH)2+O2+H2O")
            opsi2 = st. button("2Fe+ O2+ 4H- → 2Fe2-+2H2O")
        with col2:
            opsi3 = st. button("2Fe+ O2+ 4H- → 2Fe^2-  +2H2O")
            opsi4 = st. button("Fe+ H2O → Fe+2H2O")
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
            st.markdown("<h2 style='text-align: center; color: red;'>Salah!!</h2>", unsafe_allow_html=True)
            st.error('Coba lagi!')
            
    if result == "soal 5":
        st.write("Larutan HCL dalam air memiliki kadar 50 %. Hitunglah fraksi mol HCL dalam larutan tersebut (Mr HCL= 36,5)...")
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
        st.write("Larutan Sorensen 10% b/v, memiliki PPM sebesar...")
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
        st.write("Berapa gram yang di butuhkan untuk membuat larutan NaoH 0,5 mol (Mr= 40)...")
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
        st.write("Larutan 0,2 molal H2SO4 terbuat dari 40 gram H2SO4 dengan...")
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
            
    if result == "soal 9":
        st.write("Suatu unsur ketika diuji dengan uji nyala menghasilkan nyala api berwarna hijau, unsur tersebut adalah...")
        col1, col2 = st.columns(2)
        with col1:
            opsi1 = st. button("Berilium")
            opsi2 = st. button("Barium")
        with col2:
            opsi3 = st. button("Magnesium")
            opsi4 = st. button("Litium")
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
            
    if result == "soal 10":
        st.write(
            """
        seorang mahasiswa berencana untuk melakukan percobaan pemisahan kation golongan I-V, ia memiliki sebuah sampel yang tidak diketahui golongannya,
        ia pun berinisiatif untuk menambahkan HCl kedalam sampel tersebut, terjadilah pembentukan endapan putih ketika sampel tersebut ditambahkan dengan HCL,
        ia pun berniat untuk memanaskan sampel tersebut setelah ia cuci namun ketika dipanaskan tidak terjadi perubahan,
        lalu terakhir ia menambahkan senyawa K2CrO4 kedalam sampel, lalu sampel tersebut pun membentuk endapan kuning,
        berdasarkan percobaan tersebut, sampel yang di uji oleh mahasiswa itu adalah...
        """)
        col1, col2 = st.columns(2)
        with col1:
            opsi1 = st. button("Fe ^3+")
            opsi2 = st. button("Al ^3+")
        with col2:
            opsi3 = st. button("Hg ^2+")
            opsi4 = st. button("Pb ^2+")
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
    if result == "soal 1":
        st.write(
            """
        Hitunglah pH dari larutan berikut:
        
        60 mL CH3COOH 0,12 M +  40 mL NaOH 0,090 M  (Ka = 1,8 x10-5)
        """)
        col1, col2 = st.columns(2)
        with col1:
            opsi1 = st. button("4,70")
            opsi2 = st. button("4,74")
        with col2:
            opsi3 = st. button("4,78")
            opsi4 = st. button("4,80")
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
            
    if result == "soal 2":
        st.write("Berapa garam asam oksalat (H2C2O4.2H2O) yang harus ditimbang untuk membuat larutan asam oksalat 0,1 N sebanyak 500 mL (BE= 63 g/grek)")
        col1, col2 = st.columns(2)
        with col1:
            opsi1 = st. button("3,10")
            opsi2 = st. button("3,12")
        with col2:
            opsi3 = st. button("3,15")
            opsi4 = st. button("3,14")
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
            st.markdown("<h2 style='text-align: center; color: red;'>Salah!!</h2>", unsafe_allow_html=True)
            st.error('Coba lagi!')
            
    if result == "soal 3":
        st.write(
            """
        Suatu sampel yang mengandung asam asetat diencerkan sebanyak 4x. sebanyak 10 mL dari larutan tersebut dititrasi dengan NaOH 0,1025 N sampai titik akhir diperoleh 15,27 mL.
            
        Hitunglah berapa persen kadar asam asetat dalam sampel.
        """)
        col1, col2 = st.columns(2)
        with col1:
            opsi1 = st. button("1,49%")
            opsi2 = st. button("1,50%")
        with col2:
            opsi3 = st. button("1,51%")
            opsi4 = st. button("1,52%")
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
        Ditimbang boraks (Na2B4O7. 10H2O) sebanyak  1500 mg kemudian dilarutkan ke dalam labu takar 100 mL dan tepatkan sampai tanda garis, lalu homogenkan. Larutan dipipet sebanyak 25 mL ke dalam Erlenmeyer, ditambahkan 2 tetes indikator MM kemudian dititrasi dengan larutan HCl 0,1 N sampai larutan berubah warna menjadi merah. Volume titik akhir diperoleh 21,10 mL. 
        
        Berapakah normalitas HCl
        """)
        col1, col2 = st.columns(2)
        with col1:
            opsi1 = st. button("0,0933 N")
            opsi2 = st. button("0,0932 N")
        with col2:
            opsi3 = st. button("0,0930 N")
            opsi4 = st. button("0,0931 N")
        if opsi1:
            st.markdown("<h2 style='text-align: center; color: red;'>Salah!!</h2>", unsafe_allow_html=True)
            st.error('Coba lagi!')
        elif opsi2:
            st.markdown("<h2 style='text-align: center; color: red;'>salah!!</h2>", unsafe_allow_html=True)
            st.error('Coba lagi!')
        elif opsi3:
            st.markdown("<h2 style='text-align: center; color: green;'>Benar!!</h2>", unsafe_allow_html=True)
            st.success("soal selanjutnya!")
            st.balloons()
        elif opsi4:
            st.markdown("<h2 style='text-align: center; color: red;'>Salah!!</h2>", unsafe_allow_html=True)
            st.error('Coba lagi!')
            
    if result == "soal 5":
        st.write(
            """
        Suatu sampel campuran Na2CO3 dan NaOH dititrasi dengan menggunakan cara dua indicator. Sampel seberat 0,8432 g memerlukan 28,56 mL HCl 0,1206 M untuk mencapai titik akhir dengan indicator pp. Ke dalam larutan ditambahkan indicator metil jingga dan titrasi dilanjutkan sampai titik akhir sehingga volume HCl akhir yang diperoleh adalah 40,74 mL (sebagai volume total) untuk mencapai titik akhir dengan indicator metil orange.
         
        Tentukan kadar masing-masing komponen dalam sampel
        """)
        col1, col2 = st.columns(2)
        with col1:
            opsi1 = st. button("Na2CO3 : 18,47% dan NaOH : 9,37%")
            opsi2 = st. button("Na2CO3 : 9,37% dan NaOH : 18,47%")
        with col2:
            opsi3 = st. button("Na2CO3 : 23,17% dan NaOH : 18,77%")
            opsi4 = st. button("Na2CO3 : 18,77% dan NaOH : 23,17%")
        if opsi1:
            st.markdown("<h2 style='text-align: center; color: green;'>Benar!!</h2>", unsafe_allow_html=True)
            st.success("soal selanjutnya!")
            st.balloons()
        elif opsi2:
            st.markdown("<h2 style='text-align: center; color: red;'>salah!!</h2>", unsafe_allow_html=True)
            st.error('Coba lagi!')
        elif opsi3:
            st.markdown("<h2 style='text-align: center; color: red;'>Salah!!</h2>", unsafe_allow_html=True)
            st.error('Coba lagi!')
        elif opsi4:
            st.markdown("<h2 style='text-align: center; color: red;'>Salah!!</h2>", unsafe_allow_html=True)
            st.error('Coba lagi!')
            
    if result == "soal 6":
        st.write("Zat yang digunakan untuk mengetahui pada saat titrasi harus dihentikan (titik akhir titrasi)disebut...")
        col1, col2 = st.columns(2)
        with col1:
            opsi1 = st. button("Indikator ")
            opsi2 = st. button("Asam Sulfat")
        with col2:
            opsi3 = st. button("Karbon Aktif")
            opsi4 = st. button("Natrium Hidroksida")
        if opsi1:
            st.markdown("<h2 style='text-align: center; color: green;'>Benar!!</h2>", unsafe_allow_html=True)
            st.success("soal selanjutnya!")
            st.balloons()
        elif opsi2:
            st.markdown("<h2 style='text-align: center; color: red;'>salah!!</h2>", unsafe_allow_html=True)
            st.error('Coba lagi!')
        elif opsi3:
            st.markdown("<h2 style='text-align: center; color: green;'>Benar!!</h2>", unsafe_allow_html=True)
            st.error('Coba lagi!')
        elif opsi4:
            st.markdown("<h2 style='text-align: center; color: red;'>Salah!!</h2>", unsafe_allow_html=True)
            st.error('Coba lagi!')
            
    if result == "soal 7":
        st.write(
            """
        Hitunglah pH dari larutan berikut:
        
        100 mL NH3 0,14 M + 50 mL HCl 0,1 M , (Kb = 1,8 x 10-5)
        """)
        col1, col2 = st.columns(2)
        with col1:
            opsi1 = st. button("9,51")
            opsi2 = st. button("9,50")
        with col2:
            opsi3 = st. button("9,49")
            opsi4 = st. button("9,48")
        if opsi1:
            st.markdown("<h2 style='text-align: center; color: green;'>Benar!!</h2>", unsafe_allow_html=True)
            st.success("soal selanjutnya!")
            st.balloons()
        elif opsi2:
            st.markdown("<h2 style='text-align: center; color: red;'>salah!!</h2>", unsafe_allow_html=True)
            st.error('Coba lagi!')
        elif opsi3:
            st.markdown("<h2 style='text-align: center; color: red;'>Salah!!</h2>", unsafe_allow_html=True)
            st.error('Coba lagi!')
        elif opsi4:
            st.markdown("<h2 style='text-align: center; color: red;'>Salah!!</h2>", unsafe_allow_html=True)
            st.error('Coba lagi!')
            
    if result == "soal 8":
        st.write("Perhitungan atau penetapan analit didasarkan pada keadaan...")
        col1, col2 = st.columns(2)
        with col1:
            opsi1 = st. button("Titik jenuh")
            opsi2 = st. button("Ekivalen")
        with col2:
            opsi3 = st. button("Titik didih")
            opsi4 = st. button("Standar")
        if opsi1:
            st.markdown("<h2 style='text-align: center; color: red;'>Salah!!</h2>", unsafe_allow_html=True)
            st.error('Coba lagi!')
        elif opsi2:
            st.markdown("<h2 style='text-align: center; color: green;'>Benar!!</h2>", unsafe_allow_html=True)
            st.success("soal selanjutnya!")
            st.balloons()
        elif opsi3:
            st.markdown("<h2 style='text-align: center; color:red;'>Salah!!</h2>", unsafe_allow_html=True)
            st.error('Coba lagi!')
        elif opsi4:
            st.markdown("<h2 style='text-align: center; color: red;'>Salah!!</h2>", unsafe_allow_html=True)
            st.error('Coba lagi!')
        
    if result == "soal 9":
        st.write(
            """
        Berapa gram KMnO4 yang harus ditimbang untuk membuat larutan KMnO4 0,1 N sebanyak 250 mL (reaksi dalam suasana asam), BM KMnO4 = 158 g/mol
        
        MnO4- + 8H+ → Mn2+ + 4H2O  (BE = 31,6 g/grek)
        """)
        col1, col2 = st.columns(2)
        with col1:
            opsi1 = st. button("0,81")
            opsi2 = st. button("0,80")
        with col2:
            opsi3 = st. button("0,78")
            opsi4 = st. button("0,79")
        if opsi1:
            st.markdown("<h2 style='text-align: center; color: red;'>Salah!!</h2>", unsafe_allow_html=True)
            st.error('Coba lagi!')
        elif opsi2:
            st.markdown("<h2 style='text-align: center; color: red;'>Salah!!</h2>", unsafe_allow_html=True)
            st.error('Coba lagi!')
        elif opsi3:
            st.markdown("<h2 style='text-align: center; color:red;'>Salah!!</h2>", unsafe_allow_html=True)
            st.error('Coba lagi!')
        elif opsi4:
            st.markdown("<h2 style='text-align: center; color: green;'>Benar!!</h2>", unsafe_allow_html=True)
            st.success("soal selanjutnya!")
            st.balloons()
            
    if result == "soal 10":
        st.write(
            """
        Asam oksalat ditimbang sebanyak 1,2653 gram dilarutkan dalam labu takar 250 mL. Sebanyak 25 mL dititrasi dengan NaOH sampai titik akhir titrasi pada volume 10,25 mL. 
        
        Hitunglah normalitas NaOH
        """)
        col1, col2 = st.columns(2)
        with col1:
            opsi1 = st. button("0,1953")
            opsi2 = st. button("0,1955")
        with col2:
            opsi3 = st. button("0,1957")
            opsi4 = st. button("0,1959")
        if opsi1:
            st.markdown("<h2 style='text-align: center; color: red;'>Salah!!</h2>", unsafe_allow_html=True)
            st.error('Coba lagi!')
        elif opsi2:
            st.markdown("<h2 style='text-align: center; color: red;'>Salah!!</h2>", unsafe_allow_html=True)
            st.error('Coba lagi!')
        elif opsi3:
            st.markdown("<h2 style='text-align: center; color:red;'>Salah!!</h2>", unsafe_allow_html=True)
            st.error('Coba lagi!')
        elif opsi4:
            st.markdown("<h2 style='text-align: center; color: green;'>Benar!!</h2>", unsafe_allow_html=True)
            st.success("soal selanjutnya!")
            st.balloons()
            
    

    
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
    if result == "soal 4":
        st.write("Berikut ini yang merupakan sifat senyawa aromatik adalah...")
        col1, col2 = st.columns(2)
        with col1:
            opsi1 = st. button("Memiliki rantai terbuka")
            opsi2 = st. button("Mudah larut dalam air")
        with col2:
            opsi3 = st. button("Tidak memiliki ikatan rangkap")
            opsi4 = st. button("Mudah terbakar")
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
    if result == "soal 5":
        st.write("Berikut ini yang merupakan produk adisi HBr pada butena mengikuti peraturan markovnikov adalah...")
        col1, col2 = st.columns(2)
        with col1:
            opsi1 = st. button("CH3–CH2–CH=CH2")
            opsi2 = st. button("CH2=CH–CH2–CH2–Br")
        with col2:
            opsi3 = st. button("CH3–CH2–CHBr–CH3")
            opsi4 = st. button("CH2–Br–CH2–CH3")
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
            st.markdown("<h2 style='text-align: center; color: red;'>Salah!!</h2>", unsafe_allow_html=True)
            st.error('Coba lagi!')
    if result == "soal 6":
        st.write("Senyawa alkohol yang jika dioksidasi akan menghasilkan alkanon adalah...")
        col1, col2 = st.columns(2)
        with col1:
            opsi1 = st. button("2,3,3-trimetil-1-butanol")
            opsi2 = st. button("3-pentanol")
        with col2:
            opsi3 = st. button("2-metil-1-butanol")
            opsi4 = st. button("propanol")
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
    if result == "soal 7":
        imageKO3 = Image.open('Resource/image/Quiz_Kimor/Soal_7.png')
        st.image(imageKO3)
        st.write("Penamaan yang benar untuk senyawa ini adalah?")
        col1, col2 = st.columns(2)
        with col1:
            opsi1 = st.button("2-bromo-2-kloropentana")
            opsi2 = st.button("2-bromo-2-kloroheksana")
        with col2:
            opsi3 = st.button("2-bromo-2,3-kloroheksana")
            opsi4 = st.button("2-bromo-2,3-dikloroheksana")
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
    if result == "soal 8":
        st.markdown("Berikut ini yang **bukan** penamaan IUPAC untuk rumus struktur alkohol dengan rumus C4H10O adalah")
        col1, col2 = st.columns(2)
        with col1:
            opsi1 = st.button("t-butil alkohol")
            opsi2 = st.button("3-butanol")
        with col2:
            opsi3 = st.button("2-butanol")
            opsi4 = st.button("1-butanol")
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