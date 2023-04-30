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
Ar: 19

Nomor Atom: 9

Konfigurasi Elektron: [He] 2s²2p⁵

Banyak ditemukan: Unsur ini ditemukan dalam air, batuan, tumbuhan, dan tanah sebagai Fluorida.
      
Golongan: Halogen

Wujud: Gas

Fluorin merupakan Halogen yang paling ringan dan muncul pada kondisi standar sebagai gas diatomik kuning pucat yang sangat beracun
       """)
  elif opsi2:
    st.markdown("<h2 style='text-align: center; color: raisin black;'>Klorin (Cl)</h2>", unsafe_allow_html=True)
    st.write(
      """
Ar: 35,5

Nomor Atom: 17

Konfigurasi Elektron:[Ne] 3s²3p⁵

Banyak ditemukan: Klorin banyak ditemukan bersenyawa dengan unsur natrium membentuk garam dapur, serta ditemukan dalam karnalit dan silvit.
      
Golongan: Halogen
      
Wujud: Gas

Unsur ini merupakan elemen sangat reaktif dan oksidator kuat, klorin mempunyai afinitas elektron tertinggi dan elektronegativitas ketiga tertinggi di belakang oksigen dan fluor
      """)
  elif opsi3:
    st.markdown("<h2 style='text-align: center; color: raisin black;'>Bromin (Br)</h2>", unsafe_allow_html=True)
    st.write(
      """
Ar: 80

Nomor Atom: 35

Konfigurasi Elektron: [Ar] 4s²3d¹⁰4p⁵

Banyak ditemukan: bromin dalam bentuk bromida banyak ditemukan di alam pada batuan mineral dan air laut. 
      
Golongan: Halogen
      
Wujud: Cairan

Unsur dari deret kimia halogen ini berbentuk cairan berwarna merah pada suhu kamar dan memiliki reaktivitas di antara klor dan yodium. Dalam bentuk cairan, zat ini bersifat korosif terhadap jaringan sel manusia dan uapnya menyebabkan iritasi pada mata dan tenggorokan. Dalam bentuk gas, bromin bersifat toksik.
      """)
  elif opsi4:
    st.markdown("<h2 style='text-align: center; color: raisin black;'>Iodin (I)</h2>", unsafe_allow_html=True)
    st.write(
      """
Ar: 127

Nomor Atom: 53

Konfigurasi Elektron:[Kr] 4d¹⁰ 5s² 5p⁵

Banyak ditemukan: Iodin dapat ditemukan di makanan yang bersumber dari tanah atau laut. Iodin juga dapat ditemukan terutama pada makanan protein hewani dan sayuran laut. Selain itu, mineral ini juga terdapat pada makanan seperti roti, sereal, dan susu
      
Golongan: Halogen
      
Wujud: iodin adalah benda padat abu-abu yang menyublim menjadi uap warna ungu. 
      """)
  elif opsi5:
    st.markdown("<h2 style='text-align: center; color: raisin black;'>Astatin (At)</h2>", unsafe_allow_html=True)
    st.write(
      """
Ar: -

Nomor Atom: 85

Konfigurasi Elektron: [Xe] 4f¹⁴5d¹⁰6s²6p⁵

Banyak ditemukan: Astatin merupakan unsur alami yang paling langka di kerak bumi, hanya terjadi sebagai produk peluruhan dari berbagai unsur yang lebih berat.
      
Golongan: Halogen
      
Wujud: Padatan

Astatin adalah sebuah unsur yang sangat radioaktif; semua isotopnya memiliki waktu paruh 8,1 jam atau kurang, meluruh menjadi isotop astatin lainnya, bismut, polonium, atau radon. Sebagian besar isotopnya sangat tidak stabil, dengan waktu paruh satu detik atau kurang.
      """)
  elif opsi6:
    st.markdown("<h2 style='text-align: center; color: raisin black;'>Ununseptium (Uus)</h2>", unsafe_allow_html=True)
    st.write(
      """
Ar:-

Nomor Atom: 117

Konfigurasi Elektron: 5f14 6d10 7s2 7p5 (diprediksi)

Banyak ditemukan: Ununseptium adalah unsur super berat yang dibuat secara artifisial dan tidak ditemukan secara bebas di bumi.
      
Golongan: Halogen
      
Wujud : -

Meskipun saat ini ditempatkan sebagai anggota terberat dari keluarga halogen, tidak ada bukti eksperimental yang sifat kimia dari ununseptium cocok dengan anggota ringan seperti yodium atau astatin dan analisis teoretis menunjukkan mungkin ada beberapa perbedaan penting. Ununseptium secara resmi dikenal sebagai Tennessine
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
Ar: 2

Nomor Atom: 2

Konfigurasi Elektron: 1s2

Banyak ditemukan: Helium ditemukan dalam jumlah besar dalam mineral uranium dan torium, termasuk kleveit, uraninit. karnotit, dan monazit, karena mineral-mineral ini mengemisi partikel alfa (inti helium He2+).
      
Golongan: Gas Mulia
      
Wujud : gas terkecuali pada kondisi yang sangat ekstrem.

Helium tak berwarna, tak berbau, tak berasa, tak beracun, hampir inert, berupa gas monatomik, dan merupakan unsur pertama pada golongan gas mulia dalam tabel periodik. Titik didih dan titik lebur gas ini merupakan yang terendah di antara semua unsur. 
     """)
  elif opsi2:
    st.markdown("<h2 style='text-align: center; color: raisin black;'>Neon (Ne)</h2>", unsafe_allow_html=True)
    st.write(
      """
Ar: 20,2

Nomor Atom: 10

Konfigurasi Elaktron: [He] 2s²2p⁶

Banyak ditemukan: Di bumi, satu-satunya sumber neon adalah dari ekstraksi udara cair. Neon juga ditemukan di berlian dan beberapa rongga vulkanik. 
      
Golongan: Gas Mulia
      
Wujud : Gas

Neon adalah gas monoatomik lengai yang nirwarna dan nirbau pada kondisi standar, dengan massa jenis sekitar dua pertiga udara. Neon memberikan pancaran oranye kemerahan yang berbeda saat digunakan pada lampu pijar neon bertegangan rendah, tabung lucutan, dan tanda iklan neon.[13][14] Garis emisi merah dari neon juga menyebabkan lampu merah dari laser helium–neon. Neon digunakan dalam beberapa tabung plasma dan aplikasi pendingin tetapi memiliki beberapa kegunaan komersial lainnya.
     """)
  elif opsi3:
    st.markdown("<h2 style='text-align: center; color: raisin black;'>Argon (Ar)</h2>", unsafe_allow_html=True)
    st.write(
      """
Ar: -

Nomor Atom: 18

Konfigurasi Elektron: [Ne] 3s²3p⁶

Banyak ditemukan: Argon adalah gas mulia yang paling melimpah dan menyumbang sekitar 0,94% dari atmosfer bumi dan sekitar 1,6% dari atmosfer Mars. Atmosfer tipis planet Merkurius terdiri dari sekitar 70% argon.
      
Golongan: Gas Mulia
      
Wujud : Gas

Argon memiliki kelarutan mirip oksigen dan sekitar 2,5 kali lebih mudah larut dalam air dari nitrogen.

Unsur kimia inert ini tidak berwarna dan tidak berbau baik dalam bentuk cair dan gas.

Argon diisolasi dari udara dengan fraksinasi, paling sering dengan distilasi fraksional kriogenik, suatu proses yang juga menghasilkan nitrogen murni, oksigen, neon, kripton dan xenon
     """)
  elif opsi4:
    st.markdown("<h2 style='text-align: center; color: raisin black;'>Kripton (Kr)</h2>", unsafe_allow_html=True)
    st.write(
      """
Ar: -

Nomor Atom: 36

Konfigurasi Elaktron: [Ar] 3d¹⁰4s²4p⁶

Banyak ditemukan: Kripton terdapat di udara dengan konsentrasi sekitar 1 ppm. Gas ini ditandai dengan spektrum garis-garis cerah hijau dan oranye.
      
Golongan: Gas Mulia
      
Wujud : Gas

Pada kondisi normal, kripton bersifat tidak berwarna dan tidak berbau. Namun, apabila diletakkan pada medan listrik bertegangan tinggi, kripton akan memancarkan cahaya berwarna putih.
     """)
  elif opsi5:
    st.markdown("<h2 style='text-align: center; color: raisin black;'>Xenon (Xe)</h2>", unsafe_allow_html=True)
    st.write(
      """
Ar: -

Nomor Atom: 54

Konfigurasi Elaktron:  [Kr] 4d¹⁰5s²5p⁶

Banyak ditemukan: Xenon adalah anggota gas mulia atau gas inert. Terdapat di atmosfer kta dengan kandungan satu bagian per dua puluh juta bagian atmosfer. Unsur ini ditemukan dalam bentuk gas, yang dilepaskan dari mineral mata air tertentu, dan dihasilkan secara komersial dengan ekstraksi udara cair. 
      
Golongan: Gas Mulia
      
Wujud : Gas

Xenon berupa gas mulia, tak berwarna, tak berbau dan tidak ada rasanya.

Xenon diperoleh dari udara yang dicairkan. Xenon dipergunakan untuk mengisi lampu sorot, dan lampu berintensitas tinggi lainnya, mengisi bilik gelembung yang dipergunakan oleh ahli fisika untuk mempelajari partikel sub-atom.
     """)
  elif opsi6:
    st.markdown("<h2 style='text-align: center; color: raisin black;'>Radon (Rn)</h2>", unsafe_allow_html=True)
    st.write(
      """
Ar: -

Nomor Atom: 86

Konfigurasi Elaktron: [Xe] 4f145d106s26p6

Banyak ditemukan: Konsentrasi radon yang tinggi dapat ditemukan di beberapa mata air dan mata air panas. 
      
Golongan: Gas Mulia
      
Wujud : Gas

Radon adalah sebuah gas mulia yang bersifat radioaktif, tak berwarna, tak berbau, dan tak berasa. Ia terjadi secara alami dalam jumlah kecil sebagai perantara dalam rantai peluruhan radioaktif normal di mana torium dan uranium perlahan-lahan meluruh menjadi berbagai unsur radioaktif berumur pendek dan timbal. Radon sendiri merupakan produk peluruhan langsung dari radium. 
     """)
  elif opsi7:
    st.markdown("<h2 style='text-align: center; color: raisin black;'>Ununoktium (UuO)</h2>", unsafe_allow_html=True)
    st.write(
      """
Ar: -

Nomor Atom: 118

Konfigurasi Elaktron:  5f14 6d10 7s2 7p6 (diprediksi)

Banyak ditemukan: -
      
Golongan: Gas Mulia
      
Wujud : Gas

Ununoktium (dikenal juga dengan nama eka-radon) merupakan nama sementara untuk unsur kimia sintetik super berat yang dalam tabel periodik bersimbolkan Uuo dan bernomor atom 118. Unsur ini diperkirakan memiliki sifat yang sama dengan unsur-unsur segolongannya, yaitu gas luhur.
     """)
  




    
    
    
    
    
    
    
    
