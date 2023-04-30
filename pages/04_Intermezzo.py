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
    opsi1 = st.button("Hidrogen (H)")
    opsi5 = st.button("Rubidium (Rb)")
  with col2:
    opsi2 = st.button("Litium (Li)")
    opsi6 = st.button("Sesium (Cs)")
  with col3:
    opsi3 = st.button("Natrium (Na)")
    opsi7 = st.button("Fransium (Fr)")
  with col4:
    opsi4 = st.button("Kalium (K)")
  if opsi1:
      st.markdown("<h2 style='text-align: center; color: raisin black;'>Hidrogen (H)</h2>", unsafe_allow_html=True)
      st.write(
        """
Ar : 1

Nomor Atom: 1

Konfigurasi Atom: 1S^1

Banyak ditemukan: Hidrogen ada dimana saja, dan merupakan unsur yang paling banyak ditemukan di alam semesta

Golongan: alkali

Wujud: Gas

Pada suhu dan tekanan standar, hidrogen tidak berwarna, tidak berbau, bersifat non-logam, bervalensi tunggal, dan merupakan gas diatomik yang paling gampang terbakar
""")
  elif opsi2:
        st.markdown("<h2 style='text-align: center; color: black;'>Lithium (LI)</h2>", unsafe_allow_html=True)
        st. write (
            """
Ar : 7

Nomor Atom: 3

Konfigurasi Atom: 1S^2 2s^1

Banyak ditemukan: Litium tidak pernah terdapat sebagai unsur bebas di alam, tapi hanya sebagai senyawa (biasanya ionik)
Golongan: Logam Alkali

Wujud: Logam lunak berawarna keperakan

Cara Pembuatan: Logam litium dihasilkan melalui elektrolisis dari campuran leburan 55% litium klorida dan 45% kalium klorida pada suhu sekitar 450 °C

litium sangat reaktif dan terkorosi dengan cepat dan menjadi hitam di udara yang lembap.
""")
  elif opsi3:
        st.markdown("<h2 style='text-align: center; color: black;'>Natrium (Na)</h2>", unsafe_allow_html=True)
        st.write(
          """
Ar : 23

Nomor Atom:11

Konfigurasi Atom: 1S^2 2s^2 2P^6 3S^1

Banyak ditemukan: Natrium adalah unsur keenam paling melimpah dalam kerak bumi, dan terdapat di banyak mineral seperti feldspar, sodalit dan halit

Golongan: Logam Alkali

Wujud: logam lunak, putih keperakan

Na sangat reaktif, apinya berwarna kuning, beroksidasi dalam udara, dan bereaksi kuat dengan cairan, sehingga wajib disimpan dalam minyak. Sebab sangat reaktif, natrium hampir tidak pernah ditemukan dalam bentuk unsur murni
""")
  elif opsi4:
         st.markdown("<h2 style='text-align: center; color: black;'>Kalium (K)</h2>", unsafe_allow_html=True)
         st.write(
           """
Ar : 39

Nomor Atom: 19

Konfigurasi Atom: 1S^2 2s^2 2P^6 3S^2 3P^6 4S^1

Banyak ditemukan: Kalium di alam hanya terdapat pada garam ionik.

Golongan: Logam Alkali

Wujud: logam lunak berwarna putih keperakan

unsur K  teroksidasi dengan cepat di udara dan bereaksi hebat dengan air, menghasilkan panas yang cukup untuk menyalakan hidrogen yang dipancarkan dalam reaksi dan terbakar dengan api berwarna ungu. Ia ditemukan terlarut dalam air laut
""")
  elif opsi5:
         st.markdown("<h2 style='text-align: center; color: black;'>Rubidium (Rb)</h2>", unsafe_allow_html=True)
         st.write(
           """
Ar : 85

Nomor Atom: 37

Konfigurasi Atom:5s1

Banyak ditemukan: rubidium hadir dalam jumlah signifikan pada mineral lain seperti lepodite (1,5%), pollucite, dan carnallite

Golongan: Logam Alkali

Wujud: logam abu-abu keputihan yang sangat lunak

Cara pembuatan: memperoleh Rubidium di lakukan melalui metode reduksi

Rubidium tidak dapat disimpan di bawah oksigen atmosfer, karena reaksi eksoterm yang sangat tinggi akan terjadi, kadang-kadang bahkan mengakibatkan logam ini terbakar.
""")
  elif opsi6:
         st.markdown("<h2 style='text-align: center; color: black;'>Cesium (Cs)</h2>", unsafe_allow_html=True)
         st.write(
           """
Ar: 133

Nomor Atom: 55

Konfigurasi Elaktron:[Xe] 6s1

Banyak ditemukan: cesium sendiri merupakan elemen yang secara alami ditemukan dalam jumlah kecil di dalam batu, tanah, dan debu.(1,5%), pollucite, dan carnallite

Golongan: Logam Alkali

Wujud: cesium sendiri merupakan elemen yang secara alami ditemukan dalam jumlah kecil di dalam batu, tanah, dan debu.

cesium sendiri merupakan elemen yang secara alami ditemukan dalam jumlah kecil di dalam batu, tanah, dan debu.
""")
  elif opsi7:
       st.markdown("<h2 style='text-align: center; color: black;'>Fransium (Fr)</h2>", unsafe_allow_html=True)
       st.write(
         """
Ar: 223

Nomor Atom: 87

Konfigurasi Elektron:[Rn] 7s1

Banyak ditemukan: Fr adalah hasil peluruhan alfa dariAc dan dapat ditemukan dalam jumlah kecil dalam mineral uranium

Golongan: Logam Alkali

Wujud: Logam berwarna merah bata

Cara pembuatan: Fransium dapat disintesis melalui reaksi fusi ketika target emas-197 dibombardir dengan seberkas atom oksigen-18 dari akselerator linear dalam proses yang awalnya dikembangkan di departemen fisika Universitas Negeri New York di Stony Brook pada tahun 1995.
""")
  
  

      
#Golongan II
if optiongolongan == "Golongan II":
  col1, col2, col3, col4 = st.columns(4)
  with col1:
    opsi1 = st.button("Berilium (Be)")
    opsi5 = st.button("Barium (Ba)")
  with col2:
    opsi2 = st.button("Magnesium (Mg)")
    opsi6 = st.button("Radium (Ra)")
  with col3:
    opsi3 = st.button("Kalsium (Ca)")
  with col4:
    opsi4 = st.button("Stronsium (Sr)")

#Golongan III
if optiongolongan == "Golongan III":
  col1, col2, col3, col4 = st.columns(4)
  with col1:
    opsi1 = st.button("Boron (B)")
    opsi5 = st.button("Talium (Tl)")
  with col2:
    opsi2 = st.button("Alumunium (Al)")
    opsi6 = st.button("ununtrium (Uut)")
  with col3:
    opsi3 = st.button("Galium (Ga)")
  with col4:
    opsi4 = st.button("Indium (In)")
    
#Golongan IV
if optiongolongan == "Golongan IV":
  col1, col2, col3, col4 = st.columns(4)
  with col1:
    opsi1 = st.button("Karbon (C)")
    opsi5 = st.button("Timbal (Pb)")
  with col2:
    opsi2 = st.button("Silikon (Si)")
    opsi6 = st.button("flerovium (Fl)")
  with col3:
    opsi3 = st.button("Germanium (Ge)")
  with col4:
    opsi4 = st.button("Timah (Sn)")
    
#Golongan V
if optiongolongan == "Golongan V":
  col1, col2, col3, col4 = st.columns(4)
  with col1:
    opsi1 = st.button("Nitrogen (N)")
    opsi5 = st.button("Bismut (Bi)")
  with col2:
    opsi2 = st.button("Fosfor (P)")
    opsi6 = st.button("Ununpentium (Uup)")
  with col3:
    opsi3 = st.button("Arsenik (As)")
  with col4:
    opsi4 = st.button("Antimon (Sb)")
    
#Golongan VI
if optiongolongan == "Golongan VI":
  col1, col2, col3, col4 = st.columns(4)
  with col1:
    opsi1 = st.button("Oksigen (O)")
    opsi5 = st.button("Polonium (Po)")
  with col2:
    opsi2 = st.button("Sulfur (S)")
    opsi6 = st.button("Livermorium (Lv)")
  with col3:
    opsi3 = st.button("Selenium (Se)")
  with col4:
    opsi4 = st.button("Telurium (Te)")
    
#Golongan VII
if optiongolongan == "Golongan VII":
  col1, col2, col3, col4 = st.columns(4)
  with col1:
    opsi1 = st.button("Fluorin (F)")
    opsi5 = st.button("Astatin (At)")
  with col2:
    opsi2 = st.button("Klorin (Cl)")
    opsi6 = st.button("Ununseptium (Uus)")
  with col3:
    opsi3 = st.button("Bromin (Br)")
  with col4:
    opsi4 = st.button("Iodin (I)")
  if opsi1:
    st.markdown("<h2 style='text-align: center; color: raisin black;'>Fluorin (F)</h2>", unsafe_allow_html=True)
    st.write(
      """
Ar: 

Nomor Atom: 

Konfigurasi Elaktron:

Banyak ditemukan: 
      
Golongan: 

Wujud: 
       """)
  elif opsi2:
    st.markdown("<h2 style='text-align: center; color: raisin black;'>Klorin (Cl)</h2>", unsafe_allow_html=True)
    st.write(
      """
Ar: 

Nomor Atom: 

Konfigurasi Elaktron:

Banyak ditemukan: 
      
Golongan: 
      
Wujud: 
      """)
  elif opsi3:
    st.markdown("<h2 style='text-align: center; color: raisin black;'>Bromin (Br)</h2>", unsafe_allow_html=True)
    st.write(
      """
Ar: 

Nomor Atom: 

Konfigurasi Elaktron:

Banyak ditemukan: 
      
Golongan: 
      
Wujud:
      """)
  elif opsi4:
    st.markdown("<h2 style='text-align: center; color: raisin black;'>Iodin (I)</h2>", unsafe_allow_html=True)
    st.write(
      """
Ar: 

Nomor Atom: 

Konfigurasi Elaktron:

Banyak ditemukan: 
      
Golongan: 
      
Wujud:
      """)
  elif opsi5:
    st.markdown("<h2 style='text-align: center; color: raisin black;'>Astatin (At)</h2>", unsafe_allow_html=True)
    st.write(
      """
Ar: 

Nomor Atom: 

Konfigurasi Elaktron:

Banyak ditemukan: 
      
Golongan: 
      
Wujud:
      """)
  elif opsi6:
    st.markdown("<h2 style='text-align: center; color: raisin black;'>Ununseptium (Uus)</h2>", unsafe_allow_html=True)
    st.write(
      """
Ar: 

Nomor Atom: 

Konfigurasi Elaktron:

Banyak ditemukan: 
      
Golongan: 
      
Wujud :
     """)

    
    
#Golongan VIII
if optiongolongan == "Golongan VIII":
  col1, col2, col3, col4 = st.columns(4)
  with col1:
    opsi1 = st.button("Helium (He)")
    opsi5 = st.button("Xenon (Xe)")
  with col2:
    opsi2 = st.button("Neon (Ne)")
    opsi6 = st.button("Radon (Rn)")
  with col3:
    opsi3 = st.button("Argon (Ar)")
    opsi7 = st.button("Ununoktium (UuO)")
  with col4:
    opsi4 = st.button("Kripton (Kr)")
  if opsi1:
    st.markdown("<h2 style='text-align: center; color: raisin black;'>Helium (He)</h2>", unsafe_allow_html=True)
    st.write(
      """
Ar: 

Nomor Atom: 

Konfigurasi Elaktron:

Banyak ditemukan: 
      
Golongan: 
      
Wujud :
     """)
  elif opsi2:
    st.markdown("<h2 style='text-align: center; color: raisin black;'>Neon (Ne)</h2>", unsafe_allow_html=True)
    st.write(
      """
Ar: 

Nomor Atom: 

Konfigurasi Elaktron:

Banyak ditemukan: 
      
Golongan: 
      
Wujud :
     """)
  elif opsi3:
    st.markdown("<h2 style='text-align: center; color: raisin black;'>Argon (Ar)</h2>", unsafe_allow_html=True)
    st.write(
      """
Ar: 

Nomor Atom: 

Konfigurasi Elaktron:

Banyak ditemukan: 
      
Golongan: 
      
Wujud :
     """)
  elif opsi4:
    st.markdown("<h2 style='text-align: center; color: raisin black;'>Kripton (Kr)</h2>", unsafe_allow_html=True)
    st.write(
      """
Ar: 

Nomor Atom: 

Konfigurasi Elaktron:

Banyak ditemukan: 
      
Golongan: 
      
Wujud :
     """)
  elif opsi5:
    st.markdown("<h2 style='text-align: center; color: raisin black;'>Xenon (Xe)</h2>", unsafe_allow_html=True)
    st.write(
      """
Ar: 

Nomor Atom: 

Konfigurasi Elaktron:

Banyak ditemukan: 
      
Golongan: 
      
Wujud :
     """)
  elif opsi6:
    st.markdown("<h2 style='text-align: center; color: raisin black;'>Radon (Rn)</h2>", unsafe_allow_html=True)
    st.write(
      """
Ar: 

Nomor Atom: 

Konfigurasi Elaktron:

Banyak ditemukan: 
      
Golongan: 
      
Wujud :
     """)
  elif opsi7:
    st.markdown("<h2 style='text-align: center; color: raisin black;'>Ununoktium (UuO)</h2>", unsafe_allow_html=True)
    st.write(
      """
Ar: 

Nomor Atom: 

Konfigurasi Elaktron:

Banyak ditemukan: 
      
Golongan: 
      
Wujud :
     """)
  




    
    
    
    
    
    
    
    
