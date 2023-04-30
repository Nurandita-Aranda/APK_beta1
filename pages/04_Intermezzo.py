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

Konfigurasi elektron: 1S^1

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

Konfigurasi elektron: 1S^2 2s^1

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

Konfigurasi elektron: 1S^2 2s^2 2P^6 3S^1

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

Konfigurasi elektron: 1S^2 2s^2 2P^6 3S^2 3P^6 4S^1

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

Konfigurasi elektron:5s1

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

Konfigurasi Elaktron:[Xe] 6s^1

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

Konfigurasi Elektron:[Rn] 7s^1

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
  if opsi1:
      st.markdown("<h2 style='text-align: center; color: raisin black;'>Berylium (Be)</h2>", unsafe_allow_html=True)
      st.write(
        """
Ar: 9

Nomor Atom: 4

Konfigurasi Elektron:[He] 2s²

Banyak ditemukan:Beryllium dapat ditemukan dalam beberapa mineral, seperti beryl, kriptoklas, dan epidot

Golongan: Logam Alkali

Wujud: logam alkali tanah berwarna abu-abu-baja yang kuat

Batu permata terkenal yang mengandung berilium tinggi adalah beril (akuamarin, zamrud) dan krisoberil.
""")
  elif opsi2:
        st.markdown("<h2 style='text-align: center; color: black;'>Magnesium (Mg)</h2>", unsafe_allow_html=True)
        st.write(
          """
Ar: 24

Nomor Atom: 12

Konfigurasi Elektron:[Ne] 3s^2

Banyak ditemukan:paling melimpah di alam semesta, biasanya banyak terakumulasi pada batuan beku

Golongan: Logam alkali tanah

Wujud: padatan abu-abu mengkilap 

Magnesium diproduksi dalam penuaan bintang besar dari penambahan sekuensial tiga inti helium ke inti karbon.
""")
  elif opsi3:
        st.markdown("<h2 style='text-align: center; color: black;'>Kalsium (Ca)</h2>", unsafe_allow_html=True)
        st.write(
          """
Ar: 40

Nomor Atom: 20

Konfigurasi Elektron:[Ar] 4s^2

Banyak ditemukan: Kalsium paling banyak ditemukan di batu kapur

Golongan: Logam alkali tanah

Wujud: Dalam bentuk logam, kalsium berwarna perak hingga abu-abu yang seiring waktu bisa berubah warna menjadi kuning pucat

Sifat fisik dan kimianya paling mirip dengan homolognya yang lebih berat, stronsium dan barium. Ia adalah unsur paling melimpah kelima di kerak Bumi, dan logam paling melimpah ketiga, setelah besi dan aluminium
""")
  elif opsi4:
        st.markdown("<h2 style='text-align: center; color: black;'>Stronsium (Sr)</h2>", unsafe_allow_html=True)
        st.write(
          """
Ar: 87

Nomor Atom: 38

Konfigurasi Elektron:[Kr] 5s^2

Banyak ditemukan: Stronsium banyak terdapat di alam sebagai mineral Celestite (SrSO4) dan Strontianite (SrCO3)

Golongan: Logam alkali tanah

Wujud: Logam yang tekstur yang lembut dan berwarna putih

Logam stronsium membentuk lapisan oksida gelap ketika terkena udara, Titik lebur (777 °C) dan didihnya (1377 °C) lebih rendah daripada kalsium (masing-masing 842 °C dan 1484 °C)
""")
  elif opsi5:
        st.markdown("<h2 style='text-align: center; color: black;'>Stronsium (Sr)<Barium (Ba)</h2>", unsafe_allow_html=True)
        st.write(
          """
Ar: 137

Nomor Atom: 56

Konfigurasi Elektron: [Xe] 6s2

Banyak ditemukan: Barium tidak pernah ditemukan di alam sebagai unsur bebas karena reaktivitas kimianya yang tinggi.

Golongan: Logam alkali tanah

Wujud: logam lunak putih keperakan, dengan sedikit nuansa emas saat ultra murni

logam lunak putih keperakan, dengan sedikit nuansa emas saat ultra murni
""")
   elif opsi6:
        st.markdown("<h2 style='text-align: center; color: black;'>Radium (Ra))<Barium (Ba)</h2>", unsafe_allow_html=True)
        st.write(
          """
Ar: 226

Nomor Atom: 88

Konfigurasi Elektron:[Rn] 7s2

ditemukan: Radium, dalam bentuk radium klorida, ditemukan oleh Marie dan Pierre Curie pada tahun 1898 dari bijih yang ditambang di Jáchymov. Mereka mengekstraksi senyawa radium dari uraninit dan menerbitkan penemuan tersebut di Akademi Sains Prancis lima hari kemudia

Golongan: Logam alkali tanah

Wujud:Radium murni berwarna putih keperakan

Radium mudah bereaksi dengan nitrogen (daripada oksigen) saat terpapar udara, membentuk radium nitrida (Ra3N2) dengan lapisan permukaan hitam
""")




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
