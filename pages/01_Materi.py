import streamlit as st
from PIL import Image

st.markdown("<h1 style='text-align: center; color: raisin black;'>Gaia Library</h1>", unsafe_allow_html=True)
st.subheader("Apa yang mau kamu pelajari hari ini?")

#Tab mata kuliah
tab_1, tab_2, tab_3, tab_4, tab_5 = st.tabs(["Kimia Dasar","Analisis Jenis", "Titrimetri", "Kimia Organik", "Fisika Dasar"])

#Materi Kimia Dasar
with tab_1:
    optionkimdas = st.selectbox(
            "Pilih materi yang kamu mau",
            ("--- Pilih Materi ---", "Atom, Molekul, dan Ion", "Stoikiometri","Ikatan Kimia","Sifat Fisis Larutan","Kinetika Kimia","Kesetimbangan Kimia","Asam Basa",))
    if optionkimdas == "Atom, Molekul, dan Ion":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Struktur Atom</h2>", unsafe_allow_html=True)
        st.write(
            """
            Konsep atom pertama kali ditemukan oleh Demo Cristus. Atom berasal dari kata atmos yang dalam bahasa Yunani “at” berarti “tidak” dan “tomos” berarti “dibagi”. Maka, jika digabungkan atom adalah partikel yang sudah tidak dapat dibagi lagi. Menurut Dalton konsep atom Demo Christus ini tidak bertentangan dengan hukum kekekalan massa dan hukum kekekalan energi. Sehingga Dalton membuat teori tentang atom.
            """)
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Teori Atom</h2>", unsafe_allow_html=True)
        st.write(
            """
            •	Teori Atom Dalton

John Dalton tahun 1803 merumuskan teori atom sebagai berikut: 
1.	Materi tersusun atas partikel-partikel terkecil yang disebut atom
2.	Atom-atom penyusun unsur bersifat identik (sama dan sejenis)
3.	Atom suatu unsur yang tidak dapat diubah menjadi atom unsur lain
4.	Senyawa tersusun atas 2 jenis atom atau lebih dengan perbandingan tetap dan juga tertentu.
5.	Pada reaksi kimia terjadi penataulangan atom-atom yang bereaksi. Teaksi kimia terjadi karena pemisahan atom-atom senyawa untuk kemudian bergabung kembali membentuk senyawa baru.

Kelebihan:
1.	Dapat menerangkan hukum kekekalan massa (hukum Lavoisier)
2.	Dapat menerangkan hukum Perbandingan tetap (Hukum Proust)

Kelemahan:
1.	Tidak dapat menjelaskan sifat listrik atom
2.	Pada kenyataannya atom dapat dibagi lagi menjadi partikel yang lebih kecil yang disebut subatomik.
            """)
        imageKimdas1 = Image.open('Resource/image/Kimdas/Atom1.jpg')
        st.image(imageKimdas1)
        st.write(
            """
            •	Teori Thomson

Setelah tahun 1897 Joseph John Thomson berhasil membuktikan dengan tabung sinar katode bahwa sinar katode adalah berkas partikel yang bermuatan negarif yang ada pada setiap materi maka tahun 1898 J.J Thomson membuat suatu teori atom. Menurut Thomson, atom berbentuk bulat dimana muatan listrik positif yang tersebar merata dalam atom dinetralkan oleh elektron-elektron yang berbeda di antara muatan positif. Elektron-elektron dalam atom diumpamakan seperti butiran kismis dalam roti, maka teori atom Thomson juga sering dikenal teori roti kismis.

Kelebihan: 

Membuktikan adanya partikel lain yang bermuatan negatif dalam atom. Berarti atom bukan merupakan bagian terkecil dari suatu unsur. Selain itu juga memastikan bahwa atom tersusun dari partikel yang bermuatan positif dan negatif untuk membentuk atom netral. Juga membuktikan bahwa elektron terdapat dalam semua unsur.

Kelemahan:

Belum dapat menerangkan bagaimana susunan muatan positif dan jumlah elektron dalam bola.
            """)
        imageKimdas2 = Image.open('Resource/image/Kimdas/Atom2.jpg')
        st.image(imageKimdas2)
        st.write(
            """
            •	Teori Rutherford
            
Pada tahun 1903 Philipp Lenard melalui percobaannya membuktikan bahwa teori atom Thomson yang menyatakan bahwa elekron tersebar merata dalam muatan positif atom adalah tidak benar. Hal ini mendorong ernest Rutherford (1911) tertarik untuk melanjutkan eksperimen Lenard. Dengan bantuan kedua muridnya Hans Geiger dan Ernest Mersden, Rutherford melakukan percobaan dengan hamburan sinar α. Partikel α bermuatan positif. Dari percobaan tersebut disumpulkan bahwa:
1.	Sebagian besar ruang dalam atom adalah tuang hampa; partikel α diteruskan
2.	Didalam atom terdapat suatu bagian yang sangat kecil dan padat yang disebut inti atom; partikel α dipentulkan kembali oleh inti atom
3.	Muatan inti atom dan juga partikel α sejenis yaitu positif; sebagian kecil partikel α dibelokkan
Hasil percobaan tersebut menggugurkan teori atom Thomson. Kemudian Rutherford mengajukan teori atom sebagi berikut: atom tersusun atas inti atom yang bermuatan positif sebagai pusa massa dan keliling elektron-elektron yang bermuatan negative.

Kelebihan:

Membuat hipotesa bahwa atom tersusun dari inti atom dan elektron yang mengelilingi inti dan satu sama lain terpisah oleh ruang hampa.

Kelamahan: 

Model tersebut tidak dapat menerangkan mengapa elektron tidak pernah jatuh ke dalam inti sesuai dengan teori fisika klasik.
            """)
        imageKimdas3 = Image.open('Resource/image/Kimdas/Atom3.jpg')
        st.image(imageKimdas3)
        st.write(
            """
            •	Teori Bohr
            
Diawali dari pengamatan Nels Bohr terhadap spectrum atom, adanya spectrum garis menujukan bahwa elektron hanya beredar pada lintasan-lintasan dengan energi tertentu. Dengan teori mekanikan kuantum planck, bohr (1913) menyampaikan 2 postulat untuk menjelaskan kestabilan atom.

Dua postulat bohr
1.	Elektron mengelilingi inti atom ada lintasan tertentu yang stasioner yang disebut orbit/kulit. Walaupun elektron bergerak cepat tetapi elekton tidak memancarkan atau menyerap energi sehingga energi elekktron konstran. Hal ini berarti elektron yang berputar mengelilingi inti atom memiliki lintasan tetap sehingga elektron tidak jatuh ke inti.
2.	Elektron dapat berpindah dari kulit yang satu ke kulit yang lain dengan memancarkan atau menyerap energi. Energi yang dipancarkan atau diserap ketika elektron berpidah-pindah kulit disebut foton. Besarnya foton dirumuskan.
3.	Energi yang dibawa foton ini bersifat diskrit (catu). Jika suatu atom menyerap energi, maka energi ini digunakan elektron untuk berpindah kulit dari tingkat energi rendah ke tingkat energi tinggi.

Kelebihan :

Mampu membuktikan adanya lintasan elektron untuk atom hidrogen dengan jari-jari bola

Kelamahan :

Hanya dapat menerangkan atom-atom yang memiliki elektron tunggal seperti gas hidrogen, tetapi tidak dapat menerangkan spektrum warna dari atom-atom yang memiliki banyak elektron.
            """)
        imageKimdas4 = Image.open('Resource/image/Kimdas/Atom4.jpg')
        st.image(imageKimdas4)
        st.write(
            """
            •	Teori Mekanika Kuantum
            
Konsep Bohr tentang tingkat-tingkat energi mendasari perkembangan teori atom mekanika kuantum. Elektron terletak pada orbital-orbital. Orbital merupakan suatu ruangan dimana kebolehjadian ditemukannya elektron.
            """)
        st.write(
            """
            Daftar Pustaka: 
           
Diki. 2022. 5 Teori Atom Menurut Para Ahli. https://dosenpintar.com/5-teori-atom-menurut-para-ahli/#Struktur_atom.

L,Admin. 2015. Kelebihan dan Kelemahan Model Atom. https://www.markijar.com/2015/05/kelebihan-dan-kelemahan-model-atom.html.
            """)
        st.write(" ")
        st.caption("Download Materi")
        st.write("Google Drive: [link](https://drive.google.com/file/d/1Slheotw7HAcpZ-uEzV7PkO1ingI3lATo/view?usp=sharing)")

    if optionkimdas == "Stoikiometri":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Stoikiometri</h2>", unsafe_allow_html=True)
        st.write(
            """
            A.	Pengertian Rumus Molekul dan Rumus Empiris
            
Rumus molekul adalah rumus yang menjelaskan mengenai jumlah atom pada tiap unsur di dalam suatu senyawa. Sementara itu, rumus empiris adalah rumus yang menjelaskan mengenai perbandingan atom yang paling sederhana di dalam suatu senyawa.

B.	Menentukan Rumus Molekul

Rumus Molekul pada dasarnya memiliki jumlah atom kelipatan dari rumus empiris. Meskipun ada beberapa senyawa yang rumus molekul dan rumus empirisnya sama. Persamaan yang digunakan untuk menuliskan rumus molekul.

Rumus molekul:
Mr rumus empiris x n = Mr rumus molekul


C.	Menentukan Rumus Empiris. 
1.	Menggunakan rumus molekul, 
caranya dengan menyederhanakan jumlah dari atom penyusun rumus molekul agar menghasilkan bilangan bulat yang paling kecil.
2.	Menggunakan perbandingan mol, 
caranya dengan membandingkan mol unsur penyusun senyawa dengan syarat massanya harus diketahui.

D.	Pengertian Stoikiometri

Stoikiometri pertama kali dikemukakan oleh ilmuwan Jerman Bernama Jeremias Benjamin Richter pada abad akhir ke-19. Ketika itu, ia ingin mencari tahu jumlah relatif reaktan dan produk di dalam suatu reaksi kimia. Jadi, Stoikiometri adalah suatu ilmu kimia yang mempelajari mengenai kuantitas yang terdapat di dalam suatu zat seperti massa, volume, jumlah mol, dan jumlah partikel. Suatu reaksi dikatakan sebagai reaksi stoikiometri apabila suatu reaktan habis sepenuhnya. Pada reaksi stoikiometri, bilangan yang mewakili mol reaktan dan produk di dalam reaksi disebut koefisien stoikiometri yang bertujuan untuk menetapkan perbandingan antara mol reaktan dengan mol produk.

E.	. Hukum Dasar Stoikiometri
1.	Hukum kekekalan massa (Hukum Lavoisier), 
hukum yang menjelaskan mengenai kondisi massa total suatu zat setelah reaksi yang sama dengan massa total sebelum dilakukan reaksi.
2.	Hukum Perbandingan Tetap (Hukum Proust), 
hukum ini menjelaskan perbandingan massa unsur penyusun pada senyawa akan selalu tetap. 
3.	Hukum Perbandingan Berganda (Hukum Dalton), 
hukum ini menjelaskan mengenai kondisi ketika dua unsur yang dapat menghasilkan lebih dari suatu senyawa maka perbandingan massa unsur salah satu unsur adalah bilangan bulat sederhana.
4.	Hukum Perbandingan Volume (Hukum Gay-Lussac), 
hukum ini menyatakan bahwa perubahan suatu volume gas akan dipengaruhi oleh suhu dan tekanan.
5.	Hipotesis Avogadro, 
hipotesis Avogadro menyatakan bahwa suatu partikel unsur tidak selalu atom, tetapi dapat berupa molekul unsur.

F.	Konsep Stoikiometri
1.	Massa Atom Relatif (Ar), massa atom relatif adalah perbandingan massa satu atom dengan 1/12 kali massa dari isotop karbon-12. C-12 dijadikan standar perbandingan karena memiliki kestabilan inti dibandingan dengan yang lain.
2.	Massa Molekul Relatif (Mr), massa molekul relatif adalah massa yang digunakan untuk mencari perbandingan massa dari satu molekul senyawa dengan 1/12 kali massa C-12.
3.	Konsep Mol. konsep mol menyatakan bahwa satu mol suatu zat adalah banyaknya zat tersebut mengandung 6,02 x 1023. Hubungan mol dengan jumlah partikel telah ditetapkan sesuai dengan hipotesis Avogadro.
4.	Molaritas (M), molaritas adalah jumlah mol zat terlarut pada satu liter larutan.
Rumus molaritas:
M = n/V
            """)
        st.write(
            """
            Daftar Pustaka:
            
            SEO Management. 2022. Stoikiometri Adalah : Pengertian, Rumus, Hukum dam Contoh soal. https://www.sampoernaacademy.sch.id/id/stoikiometri-adalah/
            """)
        st.write(" ")
        st.caption("Download Materi")
        st.write("Google Drive: [link](https://drive.google.com/file/d/17M05OfuolzThRbny0_0BwD1OPp8EfEto/view?usp=sharing)")
    if optionkimdas == "Ikatan Kimia":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Ikatan Kimia</h2>", unsafe_allow_html=True)
        st.write(
            """
            Konfigurasi Elektron Gas Mulia
            
A. Teori Lewis

G.N. Lewis dan W. Kossel mengkaitkan kestabilan gas mulia dengan konfigurasi elektron sebagai berikut :
1. Gas mulia bersifat stabil karena memiliki konfigurasi elektron penuh. Yaitu oktet atau 8 elektron pada kuliat terluar. Kecuali Helium dengan konfigurasi duplet atau 2 elektron pada kulit terluar.
2. unsur unsur lain dapat mencapai konfigurasi elektron oktet atau duplet dengan membentuk ikatan kimia. 

B. Pembentukan ion positif

Ion positif dapat terbentuk karena suatu atom melepaskan elektron terluarnya sehingga atom tersebut mencapai keadaan stabil yaitu oktet atau duplet. Atom logam yang memiliki valensi rendah (elektron valensi 1,2&3) cenderung melepaskan elektron. Elektron valensi sesuai dengan golongan tabel periodik. Jumlah ion positinf sama dengan jumlah elektron yang dilepaskan.
Contoh ; Na dengan nomor atom 11 memiliki konfigurasi elektron 1s1 2s1 2p6 3s1

C. Pembentukan Ion Negatif 

Ion negative terbentuk karena suatu atom menangkap elektron sehingga atom tersebut mencapai keadaan stabil yaitu oktet atau duplet. Atom logam yang memiliki valensi tinggi(elektron valensi 4,6,7) cenderung menangkap elektron.
Contoh : Fluorin dengan nomor atom 9 memiliki konfigurasi elektron 1s2 2s2 2p5

D. Struktur Lewis

Pembentukan ikatan kimia menyangkut pada perubahan konfigurasi elektron, khusunya pada kulit valensi. Oleh karena itu, untuk penyederhanaan, atom atom cukup digambarkan valensinya. Lambang atom yang disertai elektron valensi disebut lambang lewis. Contoh :
Be dengan nomor atom 4 memiliki konfigurasi elektron yaitu 1s2 2s2. Sehingga Be memiliki
elektron valensi 2, sehinga rumus lewis : 
            """)
        st.image("https://photos.google.com/u/2/album/AF1QipMK4HoKNipSDAoodvhXAuspTfcZW_wdLzKAgFzs/photo/AF1QipPRNObcGhl0Yzhyd5UjYhVbCkRSQUtZuHout0y8")
        st.write(
            """
            Ikatan Ion
Pada ikatan ion, terjadi transfer elektron dari satu atom ke atom lain. Karena Perpindahan elektron ini maka atom yang mendapatkan elektron yakan bermuatan negatif (Anion) dan yang kehilangan elektron akan bermuatan positif (Kation). Karena adanya perbedaan muatan antar ion, maka ion positif dan ion negative akan saling tarik menarik oleh gaya elektrostatik. Kejadian ini merupakan dasar ikatan ionic.
Contoh :
            """)
        st.image("https://photos.google.com/u/2/album/AF1QipMK4HoKNipSDAoodvhXAuspTfcZW_wdLzKAgFzs/photo/AF1QipO6C_N8IheyMyqGyvISbv5rP44dxwq3qus_dYvy")
        st.write(
            """
Sifat senyawa ion yaitu :
1. Memiliki titik didih dan titik leleh yang tinggi.
2. Keras tetapi rapuh.
3. Berupa padatan pada suhu ruang.
4. Larut dalam pelarut air, tetapi umumnya tidak larut dalam pelarut organic.
5. Tidak meghantarkan listrik pada fasa padatan. Tetapi, menghantarkan listrik pada fasa cairan.
            """)
        st.write(
            """
            Ikatan Kovalen
1. Proses Pembentukan Ikatan Kovalen Tunggal

Ikatan terjadi karena pemakaian Bersama elektron oleh atom atom yang berikatan. Pasangan elektron yang dipakai Bersama disebut pasangan elektron ikatan dan pasangan elektron valensi yang tidak terlibat dalam pembentukan ikatan kovalen disebut pasangan elektron bebas. Ikatan kovalen umumnya terjadi antara atom atom unsur nonlogam. Senyawa yang hanya mengandung ikatan kovalen disebut senyawa kovalen. Struktur Lewis adalah penggambaran ikatan kovalen yang menggunakan lambang titik lewis dimana Pasangan elektron ikatan dinyatakan dengan garis atau sepasang titik yang diletakkan di antara kedua atom dan Pasangan elektron bebas dinyatakan titik titik pada masing masing atom.
            """)
        st.image("https://photos.google.com/u/2/album/AF1QipMK4HoKNipSDAoodvhXAuspTfcZW_wdLzKAgFzs/photo/AF1QipPudcRnEanr4Dym72C2QeWM16T56R1eswBb-7GY")
        st.write(
            """
2. Proses Pembentukan Ikatan Kovalen Rangkap 2

Ikatan kovalen rangkap 2 adalah ikatan kovalen yang melibatkan dua pasang elektron bersama. Ikatan kovalen rangkap 2 dinyatakan dengan dua garis. Contohnya :
            """)
        st.image("https://photos.google.com/u/2/album/AF1QipMK4HoKNipSDAoodvhXAuspTfcZW_wdLzKAgFzs/photo/AF1QipNL5I8ePdpntlqOscIFDbOubktWgE8Nn9uR6IsZ")
        st.write(
            """
3. Proses Pembentukan Ikatan Kovalen Rangkap 3

Ikatan kovalen rangkap 3 adalah ikatan kovalen yang melibatkan dua pasang elektron bersama. Ikatan kovalen rangkap 3 dinyatakan dengan tiga garis. Contohnya :
            """)
        st.image("https://photos.google.com/u/2/album/AF1QipMK4HoKNipSDAoodvhXAuspTfcZW_wdLzKAgFzs/photo/AF1QipPQ7ZkJAD62tIYeTI6UgeRZzMKiF7Wkaq8PzQkB")
        st.write(
            """
            Sifat senyawa kovalen :
1. Berupa cairan, padatan lunak,dan gas pada suhu ruang.
2. Bersifat lunak dan tidak rapuh
3. Mempunyai titik leleh dan titik didih yang rendah.
4. Umumnya tidak larut dalam air, namun larut pada pelarut organik.
5. Tidak menghantarkan listrik.
            """)
        st.write(
            """
            Ikatan Kovalen Koordinasi
Ikatan Kovalen koordinasi adalah ikatan yang terbentuk dari pemakaian pasangan elektron bersama yang berasal dari salah satu atom yang memiliki pasangan elektron bebas. Ciri ikatan kovalen koordinasi adalah pasangan elektron bebas dari salah satu atom yang dipakai secara bersama-sama. Contoh : 
            """)
        st.image("https://photos.google.com/u/2/album/AF1QipMK4HoKNipSDAoodvhXAuspTfcZW_wdLzKAgFzs/photo/AF1QipMYW5lYI96F_r6fa3AgNha_QnBGc_HubVqkTCQy")
        st.write(
            """
            Jadi, senyawa HNO3 memiliki satu ikatan kovalen koodinasi dan 2 ikatan kovalen.
            """)
        st.write(
            """
            Ikatan logam
Ikatan logam merupakan ikatan kimia antara atom-atom logam,bukan ikatan ion maupun kovalen. Dalam suatu logam terdapat atom atom sesamanya yang berikatan satu sama lain sehingga suatu logam akan bersifat kuat, keras, dan dapat ditempa. Elektron elektron valensi dari atom atom logam bergerak dengan cepat (membentuk lautan elektron) mengelilingi inti atom. Ikatan yang terbentuk sangat kuat sehingga ikatan antaratom logam sukar dilepaskan. 
Sifat Senyawa Logam :
1. Berupa padatan pada suhu ruang
2. Bersifat keras, tetapi lentur/tidak mudah patah jika ditempa.
3. Mempunya titik didih dan titik leleh yang tinggi.
4. Penghantar listrik yang baik.
5. Mempunyai permukaan yang mengkilap.
6. Memberi efek foto listrik dan Efek Termionik.
            """)
        st.write(" ")
        st.caption("Download Materi")
    if optionkimdas == "Sifat Fisis Larutan":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Sifat Fisis Larutan</h2>", unsafe_allow_html=True)
        st.write(
            """
            A. Jenis Larutan

Larutan yang mengandung jumlah zat maksimum yang terkandung pada pelarut pada suhu tersebut disebut latutan jenuh. Sebelum titik tercapai, larutannya disebut larutan tak jenuh. Larutan tak jenuh mengandung zat terlarut lebih sedikit dibandingkan dengan kemampuaanya untuk melarutkan. Sedangkan larutan lewat jenuh, mengandung lebih banyak zat terlarut dibandingkan yang terdapat dilarutan jenuh. Larutan lewat jenuh bukanlah larutan yang sangat stabil. Pada saat,Sebagian zat terlarut akan terpisah dari larutan lewat jenuh sebagai kristal. Proses inilah yang disebut kristalisasi. 

B. Proses Pelarutan Dari Sudut Pandang Molekul.

Gaya tarik menarik memainkan peran penting dalam pembentukan larutan. Bila zat terlarut larut dalam zat pelarut, partikel zat tersebut akan menyebar ke seluruh pelarut. Partikel zat terlarut ini menempati posisi yang biasanya ditempati oleh molekul pelarut. Tiga jenis interaksi :
1. Interaksi pelarut-pelarut.
2. Interaksi zat pelarut-zat terlarut.
3. Interaksi pelarut-zat terlarut.
Proses pelarutan dibagi menjadi tiga tahap :
            """)
        st.image("https://photos.google.com/u/2/album/AF1QipMK4HoKNipSDAoodvhXAuspTfcZW_wdLzKAgFzs/photo/AF1QipPofJTjGRK6KkFFPNUrmwpt_JTtcW0WllqSdEwl")
        st.write(
            """
            Proses pelarutan dipengaruhi oleh dua faktor. Faktor pertama adalah energi, yang menentukan apakah proses berlangsung eksotermik atau endotermik. Faktor kedua adalah kecenderungan hakiki menuju ketidakteraturan dalam semua kejadian dialam. 

C. Satuan Konsentrasi
1. Jenis Satuan konsentrasi.

Persen berdasar massa

%zat terlarut = (Massa zat terlarut/massa larutan)x100%	

Molaritas 

M= mol zat terlarut/liter larutan

Dengan satuan (mol/L)

Molalitas

m = mol zat terlarut/massa pelarut(kg)

2. Perbandingan Satuan Satuan Konsentrasi

V1 X M1=V2 X M2

Keterangan : V adalah volume pelarut dan M dapat diganti dengan satuan lain sesuai dengan yang diketahui.

D. Pengaruh Suhu terhadap kelarutan
1. Kelarutan Padatan dan Suhu

Kelarutan zat padatan meningkat dengan meningkatnya suhu.

2. Kelarutan Gas dan Suhu

Kelarutan gas dalam air biasanya menurun dengan meningkatnya suhu. Dengan meningkatnya suhu, molekul udara yang terlarut mulai’mendidih’dan keluar dari larutan jauh sebelum air itu mendidih

E. Pengaruh Tekanan Terhadap Kelarutan Gas

Hubungan Kelarutan gas dan tekanan ditunjukkan oleh hukum Henry yang menyatakan bahwa kelarutan gas dalam cairan berbanding lurus dengan tekanan gas diatas larutannya. 
Dengan rumus : c=kP

Keterangan : 
c : konsentrasi molar(mol per Liter)

P : tekanan

k : konstanta

F. Sifat Koligatif

Sifat koligatif adalah beberapa sifat penting larutan bergantung pada banyaknya partikel zat terlarut dalam larutan dan tidak bergantung pada jenis partikel zat terlarut.
1. Penurunan Tekanan Uap
Hubungan tekanan uap larutan dengan tekanan uap pelarut bergantung pada konsentrasi zat terlarut dalam larutan. Hukum Raoult yang menyatakan bahwa tekanan parsial pelarut dari larutan, Pi adalah tekanan uap pelarut murni, Pio dikalikan dengan fraksi mol pelarut dalam larutan Xi.
Pi = Xi. Pio

2. Tekanan Titik Didih

Keberadaan zat terlarut yang tidak mudah menguap menurunkan tekanan uap larutan,maka berpengarug pada titik didih. Titik didi adalah suhu pada saat tekanan uap larutan sama 
dengan tekanan atmosfer luar. Kenaikan titik didih didefinisikan sebagai berikut:
 ΔTd = Td - Tdo
Dimana Td adalah titik didih larutan, dan Tdo adalah titik didih pelarut murni.

3. Penurunan titik beku 

Penurunan titik beku didefinisikan sebagai berikut:
ΔTb = Tbo – Tb
Pembekuan melibatkan transisi dari keadaan tidak teratur ke keadaan terarur. Agar proses itu terjadi, energi harus diambil dari system karena larutan lebih tidak teratur dibandingkan pelarut, maka lebih banyak energi yang diambil untuk menciptakan keteraturan. Jadi, larutan memiliki titik beku lebih rendah dibandingkan pelarut.

4. Tekanan Osmotik

osmosis adalah Gerakan bersih molekul pelarut melewati membrane semipermeabel dari pelarut murni atau dari larutan encer ke larutan pekat. Telakan osmotik adalah tekanan yang digunakan untuk menghentikan osmosis. 
Π = MRT

Keterangan :

M : Molaritas

R : Konstanta gas (0,0821 L. atm/K. mol)

T : Suhu mutlak.

5. Sifat Koligatif Elektrolit

Sifat koligatif elektrolit memerlukan pendekatan yang sedikit berbeda daripada yang digunakan untuk sifat koligatif nonelektrolit. Karena elektrolit terurai menjadi ion-ion dalam larutan dan dengan demikian satu satuan senyawa elektrolit terpisah menjadi dua atau lebih partikel bila dilarutkan. Persamaan Sifat Koligatif :

Π = iMRT

keterangan :

M : Molaritas

R : Konstanta gas (0,0821 L. atm/K. mol)

T : Suhu mutlak.

i : faktor van’t hoff 

i : jumlah partikel sebenarnya dalam larutan setelah penguraian/jumlah satuan rumus yang semua terlarut dalam larutan
              """)
    if optionkimdas == "Kinetika Kimia":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Kinetika Kimia</h2>", unsafe_allow_html=True)
        st.write(
            """
            A. Laju Reaksi

Laju reaksi,yaitu perubahan konsentrasi reaktan atau produk terhadapa waktu (M/s). Persamaan Umum produk 

Reaktan → Produk

Dari persamaan ini dapat diketahui bahwa,selama berlangsungnya suatu reaksi, molekul reaktan bereaksi sedangkan molekul produk terbentuk.Sebagai hasilnya, kita dapat mengamati jalannya reaksi dengan cara memantau menurunnya konsentrasi reaktan atau 
meningkatnya konsentrasi produk.

A → B
Laju = - Δ[A]/Δt           
Laju = - Δ[B]/Δt 

B. Hukum laju

Salah satu cara untuk mengkaji pengaruh konsentrasi reaktan terhadap laju reaksi ialah dengan menentukan bagaimana laju awal bergantung pada konsentrasi awal. Konsentrasi reaktan menurun dan akan menjadi sulit untuk mengukur perubahan nya secara akurat. Selain itu, mungkin saja terjadi reksi balik seperti

Produk → Reaktan

Hukum laju : Laju = k[A]X[Y]Y

Untuk reaksi umum : aA + bB → cC + dD

C. Hubungan Antara Konsentrasi Reaktan dan Waktu
1. Reaksi Orde Pertama : Reaksi yang lajunya bergantung pada konsentrasi reaktan dipangkatkan dengan satu.
2. Reaksi Orde Kedua : Reaksi yang lajunya bergantung pada konsentrasi reaktan dipangkatkan dengan dua.

D. Energi Aktivasi dan Ketergantungan Konstanta Laju Terhadap suhu
1. Teori Tumbukan pada Kinetika Kimia
Dari segi teori tumbukan pada kinetika kimia, maka dapat diperkirakan laju reaksi akan berbanding lurus dengan banyaknya tumbukan molekul per detik atau berbanding lurus dengan frekuensi tumbukan molekul.

   Laju = banyaknya tumbukan/waktu(sekon)
    
2. Persamaan Arrhenius
Ketergantungan konstanta laju reaksi terhadap suhu dapat dinyatakan dengan persamaan yang dikenal dengan persamaan Arrhenius :

    k = Ae-EaIRT

E. Mekanisme Reaksi dan Hukum Laju

Dalam banyak kasus, persamaan ini sekedar menyatakan jumlah dari sederet reaksi sederhana yang sering dinamakan sebagai tahap elementer karena reaksi reaksi sederhana tersebut merepresentasikan jalannya reaksi keseluruhan pada tingkat molekul. Urutan-urutan elementer yang mengarah pada pembentukan produk dinamakan mekanisme reaksi. Sebagai contoh ;

2NO(g) → N2O2(g)
N2O2(g) + O2(g) → 2NO2(g)
Maka : 
Tahap 1 : NO(g)   + NO(g) →  N2O2(g)
Tahap 2 : N2O2(g) + O2(g) →  2NO2(g)
Reaksi Keseluruhan : 2NO(g) + N2O2(g) + O2(g) → N2O2(g) + 2NO2(g)

Tahap Elementer harus memenuhi dua syarat :
1. Jumlah elementer harus menghasilkan persamaan setara keseluruhan untuk reaksi tersebut.
2. Tahap penentu laju, yaitu tahap paling lambat dari seluruh rangkaian tahap menuju pembentukan produk. Harus memprediksi hukum laju yang sama.

F. Katalisis

Katalis adalah zat yang meningkatkan laju reaksi kimia tanpa ikut terpakai. Katalis dapat bereaksi membentuk produk antara, tetapi akan diperoleh kembali dalam tahap berikutnya. Mari kita anggap bahwa reaksi berikut memiliki konstanta laju k tertentu dan energi aktivasi Ea.

   A + B → C + D

Namun demikian, dengan kehadiran katalis, konstanta laju disebut konstanta laju katalitik. Maka berdasarkan definisi katalitik :

   Lajuberkatalis>lajutakberkatalis
           """)
    if optionkimdas == "Kesetimbangan Kimia":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Kesetimbangan Kimia</h2>", unsafe_allow_html=True)
        st.write(
            """
            A. Konsep Kesetimbangan

Bila laju reaksi maju dan reaksi balik sama besar dan konsentrasi reaktan dan produk tidak lagi berubah seiring berjalannya waktu, maka tercapailah kesetimbangan kimia. Kesetimbangan kimia merupakan proses dinamik. Kesetimbangan antara dua fasa dari zat yang sama dinamakan kesetimbangan fisis karena perubahan yang terjadi hanyalah proses fisis. Dalam kasus ini,molekul H2O meninggalkan dan yang Kembali ke fasa cair sama banyaknya.

    H20(l) ⇆ H20(g)

B. Konstanta Kesetimbangan

Kita dapat mengggeneralisasi pembahasan ini dengan memperhatikan reaksi reversibel berikut.
    aA + bB ⇆ cC + dD

Dimana a,b,c, dan d adalah koefisien stoikiometri untuk spesi spesi yang bereaksi dengan A,B,C,dan D. konstanta kesetimbangan untuk reaksi pada suhu tertentu ialah.

     k = [C]c[D]d/[A]a[B]b

C. Beberapa Cara Untuk Menyatakan Konstanta Kesetimbangan
1. Kesetimbangan Homogen : berlaku untuk reaksi yang semua spesi bereaksinya berada pada fasa yang sama.
2. Kesetimbangan Heterogen : untuk reaksi yang melibatkan fasa yang berbeda.

D. Aturan-Aturan Penulisan Persamaan Konstanta Kesetimbangan
1. konsentrasi dari spesi spesi yang konsentrasi-reaksi di dalam fasa terkondensasi. Dinyatakan dalam mol per liter.
2. Konsentrasi dari padatan murni, cairan murni dan pelarut tidak dituliskan dalam persamaan konstanta kesetimbangan.
3. konstanta kesetimbangan tidak berdimensi.

E. Apa yang Dapat Diketahui Dari Konstanta Kesetimbangan
1. Memprediksi arah reaksi.
2. Menghitung konsentrasi kesetimbangan.

F. Faktor yang mempengaruhi Kesetimbangan Kimia.
1. Asas Le Chatelier
Ada satu aturan umum yang membantu kita memprediksi kearah mana reaksi kesetimbangan akan bergeser bila terjadi perubahan konsentrasi, tekanan. Volume, atau suhu. Asas le chatalier menyatakan bahwa “ jika suatu tekanan eksternal diberikan kepada suatu sistem kesetimbangan, sistem ini akan menyesuaikan diri sedemikian rupa untuk mengimbangi sebagian tekanan ini pada saat sistem mencoba setimbang Kembali.”

2. Perubahan Konsentrasi
3. Perubahan Tekanan dan Volume
4. Perubahan suhu 
5. Pengaruh katalis
        """)
    if optionkimdas == "Asam Basa":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Asam Basa</h2>", unsafe_allow_html=True)
        st.write(
            """
            A. Asam dan Basa Brønsted 
1. Pasangan Asam Basa Konjugat

Basa konjugat dari suatu asam Brønsted ialah spesi yang tersisa ketika satu proton pindah asam tersebut. Sebaliknya, suatu asam konjugat dihasilkan dari penambahan sebuah proton pada basa Brønsted. Setiap asam Brønsted memiliki satu basa konjugat dan setiap basa Brønsted memiliki satu asam konjugat.

B. Sifat Asam Basa dari Air

Salah satu sifat khas air ialah kemampuannya untuk bertindak baik sebagai asam maupun sebagai basa.Air berfungsi sebagai basa dalam reaksi dengan asam,dan pelarut ini berfungsi sebagai asam dalam reaksi basa. Air merupakan elektrolit yang sangat lemah sehingga air merupakan penghantar listrik yang buruk, meskipun hanya terionisasi sedikit.

   H2O(l)  ⇆ H+(aq) + OH-(aq)

Reaksi ini adakalanya disebut autoionisasi air. Untuk menjelaskan sifat asam basa dari air dari sudut pandang Brønsted sebagai berikut : 

   H2O + H2O ⇆ H3O+ +  OH-
   
   asam1 basa2  asam2   basa1

C. pH Suatu Ukuran Keasaman

Karena konsentrasi ion H+ dan OH-  dalam larutan air serinh kali sangat kecil dan kerena itu sulit diukur. Maka, seorang biokimiawan Denmark Soren Sorensen pada tahu 1909 mengajukan cara pengukuran yang lebih praktis yang disebut pH. pH suatu larutan didefinisikan sebagai logaritma negative dari konsentrasi ion Hidrogen(dalam mol per liter).

   pH = - log [H+]

Karena pH pada dasarnya hanyalah suatu cara untuk menyatakan suatu konsentrasi ion Hidrogen. Larutan asam dan basa pada suhu 25oC dapat di definisikan berdasarkan nilai pH nya. Seperti :

Larutan asam : pH < 7,00

Larutan basa  : pH > 7,00

Larutan netral : pH = 7,00

Rumus mencari pH asam = pH : -log[H+]

Rumus mencari pH basa = pOH : -log[OH-] lalu pH : 14,00-pOH

D. Kekuatan Asam dan Basa

Asam kuat ialah elektrolit kuat, yang kebanyakan digunakan untuk kebutuhan praktis karena dianggap terionisasi sempurna dalam air. Kebanyakan asam kuat adalah asam anorganik. Kebanyakan asam terionisasi hanya sedikit dalam air,asam seperti ini disebut asam lemah. Kekuatan asam lemah sangat beragam karena beragamnya derajat ionisasi. Terbatasnya ionisasi asam lemah berkaitan dengan konstanta kesetimbangan ionisasi.
Basa kuat ialah semua elektrolit kuat yang terionisasi sempurna dalam air. Sedangkan basa lemah adalah elekrolit lemah. Hal yang perlu diingat yaitu

1. jika asamnya kuat, basa konjugat sangat lemah.
2. H3O+ ialah asam terkuat yang dapat berada dalam laturan berair.
3. Ion OH- ialah basa terkuat yang dapat berada dalam larutan berair. 

E. Asam Lemah dan Konstanta Ionisasi Asam

Mari kita asumsikan suatu asam monoprotik lemah HA, ionisasinya dalam air adalah :

    HA(aq) ⇆  H+(aq) + A-(aq)

Maka konstanta kesetimbangan untuk asam ini dinamakan konstanta kesetimbanga asam. Dinyatakan sebagai berikut :

     ka = [H+][A-] / [HA]

Dalam hal ini, tiga dasar tahapnya ialah:
1.	Nyatakan konsentrasi kesetimbangan dari semua spesi dalam konsentrasi awalnya dan satu bilangan tak diketahui x, yang menyatakan perubahan konsentrasi.
2.	Tuliskan konstanta ionisasi asam dalam konsentrasi-konsentrasi k setimbangnya. Dengan mengetahui nilai k maka kita dapat mengetahui nila x.
3.	Setelah menentukan x, hitunglah konsentrasi kesetimbangan dari semua spesi atau pH larutan.

1. Persen ionisasi

Cara lain untuk mengetahui kekuatan asam ialah mengukur persen ionisasi,

Persen ionisasi = (konsentrasi asam ionisasi/konsentrasi awal asam)x100%

Semakin kuat asam maka semakin besar nilai persen ionisasinya.

F. Basa Lemah dan Konstanta Ionisasi Basa

Sama seperti halnya pada asam lemah, Dimana nila kb konstanta kesetimbangan basa dinamakan konstanta ionisasi basa. 

G. Hubungan Antara Konstanta-Konstanta Ionisasi Asam-Basa Konjugat

Ketika dua reaksi ditambahkan untuk menghasilkan reaksi ketiga, konstanta kesetimbangan untuk reaksi ketiga adalah hasilkali antara konstanta-konstanta kesetimbangan dari kedua reaksi yang ditambahkan. Jadi, untuk pasangan asam konjugat-basa konjugat akan selalu berlaku.

H. Sifat Asam Basa dari Garam
1. Garam yang menghasilkan larutan netral.
2. Garam yang menghasilkan larutan basa.
3. Garam yang menghasilkan larutan asam.
4. Hidrolis ion logam
5. Garam yang kation dan anion nya terhidrolisis.
        """)


            

            
            
  
            


       
            
                
                
#Materi Analisis Jenis            
with tab_2:
    optionanjen = st.selectbox(
            "Pilih materi yang kamu mau",
            ("--- Pilih Materi ---", "Reaksi Kimia dan Persamaan Reaksi", "Satuan Konsentrasi", "Pemisahan Kation Golongan I-V", "Identifikasi Zat Dengan Cara Kering", "Pemisahan Anion Golongan I-V", "Pembuatan Larutan",))
    if optionanjen == "Reaksi Kimia dan Persamaan Reaksi":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Reaksi Kimia dan Persamaan Reaksi</h2>", unsafe_allow_html=True)
        st.write(
            """
                 Reaksi kimia adalah proses dimana zat baru, yang disebut produk terbentuk dari sejumlah zat 
asal, yang disebut sebagai reaktan, gambaran zat-zat yang terlibat dalam suatu proses reaksi kimia dapat dinyatakan sebagai persamaan reaksi kimia

 A + B   →  C + D
Reaktan     Produk
Persamaan ini mengandung rumus dari zat-zat yang bereaksi pada sisi sebelah kiri (reaktan), dan rumus dari hasil reaksinya pada sisi sebelah kanan (produk). Penulisan reaksi Kimia memiliki  tiga  tahapan  prosedur  yang  sistematis  yang  perlu  diperhatikan  untuk memudahkan penulisan  persamaan  reaksi  kimia, ketiga tahap tersebut adalah sebagai berikut:
1.	Tuliskan nama dari reaktan dan produk

    kalsium hidroksida + asam fosfat → kalsium fosfat 

2.	Ubahlah Nama dari reaktan dan produk menjadi rumus kimia

    Ca(OH)2 + H3PO4 → Ca3(PO4)2 + H2O

3.	Setimbangkan rumus  kimia  untuk  memperoleh persamaan  reaksi  kimia, dengan mengatur koefisien reaksi

    3Ca(OH)2 + 2H3PO4 → Ca3(PO4)2 + 6H2O

Syarat-syarat berlangsungnya suatu reaksi kimia yaitu terjadi perubahan bentuk wujud zat (mengendap, melarut, atau terurai menjadi gas),warna, suhu, daya hantar atau terbentuk elektrolit lemah.
            """)
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Reaksi Kimia</h2>", unsafe_allow_html=True)
        st.write(
            """
            1.	Reaksi penetralan / reaksi penggaraman

Reaksi penetralan disebut juga reaksi asam basa. reaksi penetralan adalah reaksi yang membentuk unsur bersifat netral yaitu air (H2O) yang berasal dari zat asam yang melepaskan ion (H +) dengan zat basa yang melepaskan ion (OH-)

a.	     Oksida asam + oksida basa → garam
           
    CO2 + 2NaOH → Na2CO3 + H2O
           
b.	     Oksida basa + asam → garam + air
           
    K2O + HCl → KCl + H2O
           
c.	     Oksida logam (oksida basa)
     
    Na2O + H2O → 2NaOH
     
d.	     Oksida non logam (oksida asam)
     
    CO2 + H2O → H2CO3

2.	Reaksi metatesis

Reaksi Metatesis adalah reaksi pertukaran pasangan ion dari dua elektrolit. Pada reaksi ini, setidaknya satu produk reaksi akan membentuk endapan, gas atau elektrolit lemah.
Garam 1 + garam 2 → garam 3 + garam 4

Contoh: 
    
    AgNO3 (aq) + NaCl (aq) → AgCl(s) + NaNO3 (aq)

3.	 Reaksi redoks

Reaksi reduksi-oksidasi (ada perubahan biloks/ bilangan oksidasi). Dalam reaksi redoks atom yang menyumbangkan electron dioksidasi dan atom yang menerima electron direduksi.

    H2 + F2 → 2HF
    
Untuk membentuk senyawa hidrogen fluorida, molekul H2 melepaskan 2 elektron menjadi 2H+ : H2 → 2H+ + 2e-, sedangkan molekul F2 menangkap/mengikat 2 elektron, menjadi 2F- : F2 + 2e- → 2F-.

4.	Reaksi pengendapan

Endapan adalah zat yang memisahkan diri sebagai suatu fase padat keluar dari larutan, endapan terbentuk jika larutan menjadi terlalu jenuh dengan zat yang bersangkutan, kelarutan (s) suatu endapan, menurut definisi adalah sama dengan konsentrasi si molar dari larutan jenuhnya. Kelarutan bergantung pada berbagai kondisi, seperti suhu, tekanan, konsentrasi bahan-bahan lain dalam larutan itu, dan pada komposisi pelarutnya.

Contoh: 
    
    Pb(NO3)2 (aq) + 2 NaI(aq) → PbI2(s) + 2NaNO3(aq)

5.	Reaksi kompleks

Suatu ion (atau molekul) Kompleks terdiri dari satu Atom (ion) pusat dan sejumlah ligan dan terikat erat dengan atom (ion) pusat itu.

Contoh: 
    
    [Co(NH3)6]3+ + 6H3O+ → [Co(H2O)6]3+ + 6NH4+
            """)
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Kelarutan Elektrolit Dalam Air</h2>", unsafe_allow_html=True)
        st.write(
            """
Semua asam larut, Sebagian besar basa tidak larut kecuali ; NaOH, KOH,NH4OH, Ba(OH)2 , Ca(OH)2, Sr(OH)2 larut.
            
Garam sulfat (SO42-) umumnya larut, kecuali: BaSO4, PbSO4, Ag2SO4 tidak larut.
            
Garam klorida (Cl-), bromida (Br-), iodida(I-) umumnya larut kecuali : AgCl, PbCl2, Hg2Cl2, AgBr, PbBr2, Hg2Br2, AgI, PbI2, Hg2I2, tidak larut. 
            
Garam fluorida (F-) umumnya larut kecuali: MgF2, CaF2, dan BaF2 tidak larut.

Garam kalium (K+), natrium (Na+), ammonium (NH4+), Nitrat (NO3-), asetat(CH3COO-), hipoklorit (ClO-), klorit (ClO2-),klorat ( ClO3-), perklorat (ClO4-), Bromat(BrO3-), dan Iodat (IO3-) semuanya larut. 

Garam sulfida (S2-) umumnya tidak larut kecuali : Na2S, K2S , (NH4)2S, MgS, CaS, BaS larut. 

Garam- garam (CO32-, CrO42-, PO43-) umumnya tidak larut kecuali garam K+, Na+ dan NH4+. 
Asam yang berupa gas : H2S, asam yang terurai menjadi gas:H2CO3 H2O + CO2 (g) H2SO3 H2O + SO2 (g) 
Basa yang terurai menjadi gas : NH4OH H2O + NH3 (g).
            """)
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Tata Nama Senyawa Kimia</h2>", unsafe_allow_html=True)
        st.write(
            """
Syarat_syarat dalam penamaan senyawa kimia adalaha sebagai berikut:
1.	Senyawa yang terdiri dari unsur logam dan non logam: nama kation diikuti nama anion dengan akhiran-ida

NaCl = Natrium klorida

MgCl2 = Magnesium klorida

2.	Senyawa yang terdiri dari unsur non logam dan non logam : nama unsur diikuti
dengan awalan mono(1), di(2), tri(3), tetra(4), penta (5), heksa (6), penta (7), okta (8),
nona(9), deka(10), dst....

Contoh:

SO2 = sulfur dioksida

N2O5 = dinitrogen pentaoksida

3.	Senyawa yang mengandung logam atau kation yang memiliki 2 bilangan oksidasi maka : nama kation dengan akhiran – i, untuk biloks yang tinggi dan akhiran –o, untuk biloks rendah, atau nama kation, dengan nama umum (dalam bahasa indonesia) diikuti muatan kation dengan angka romawi.

Contoh:

FeCl2 = Ferro klorida atau besi (II) klorida

FeCl3 = Ferri klorida atau besi (III) klorida
            """)
        st.write(" ")
        st.caption("Download Materi")
        st.write("Google Drive: [link](https://drive.google.com/file/d/1nNtSU-ZxXD4xd_w0tBYA09KwL6vMIht3/view?usp=sharing)")
        
    if optionanjen == "Satuan Konsentrasi":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Satuan Konsentrasi</h2>", unsafe_allow_html=True)
        st.image("https://lh3.googleusercontent.com/eOpuDrN1ooOt6QSapIlw3ZievbUDwE0azDWkjEdp1B_VDOwsLbpmFne72Y4QwJtJjLzXH47tsmpJwlog4qlPE-CYz6vqB3iybF3c2A-8RnjvTulRRXAjXStAhiVBNTJzsYrQH0n-pxEUCFiZR-IaZePhxx9voqLhiV9afy3DQrlAVVqwL2ynTy8iSR-2OI5CKO3g2l4ZeSv9lzeiDgL96FO4TQL_iyApywFNviJINX5PkdBjJLpVfxlb1-Fg1oU3soJlOc_gjavLRNoWv85biE_lIYmMYgAyvAyDIjj_FyDf2XghgFoSZF8S-h9zgtdhoku8rb1O-1M3nk1wFfwnxNG4RacQ_pvQwdrn-vb1ANtBx8e5YrhwIvX7J98SMeMeY9cglwFxOByAxLM8rE3B6yLaKQr8TvWocR8rcDn_m1MrF7A2sUDVtOefMyKT9moNMgYS18dsBn33A8pFVr7NYYOkuHxyD3dPZiSUjCEn755sOvafEXxBJYgUEJE8qoea-dWCyZOMW7-NKhBPP16m1D_b9Byzn0d7ZoAjtGQJTcBNwVMVMdPkJs_boZXlcNjrkBfYCyZNxHtfcI0W6sURZ7OyUAB6LyR4WHiRDjv8fCDXEmmU-obSI8tyaJi_BZTDDOiUXOfiuIG7sevnCN_6qCqJcy105YlMrMTSzPjvII6tc3tWPHnP2aG6qfcyslvLExq1QH25itHdjZc291gft6YqfkduaoKhqudQP0PAod07OG-TUGH2mTMav0Fg1mp2YF8xMvQiUD-PZPKtuRiVoeP4ep_CRYHQI1yS8qTnyljITtyw-TbC9O445QJUvfBGksg2g6Z_iOVBLFI1-LuyKWoA8bhRC2ULA2CnOZAJikotYlngi45VQ3TIxYH9qKJxPBkIBRw7z_7dasfgaH7uWGk7TFTnJ5dTWlS1meQKhtAVV0g=w256-h173-s-no?authuser=0")    
        st.write(
            """
      Gambar 1. Konsep Mol (Sumber : temukanpengertian.com )
            
            Mol = g/BM = g/Mr = g/Ar    
            
g = massa (gram)

BM = berat molekul (g/mol atau mg/mmol)

      Contoh:
Hitung berapakah mol molekul yang terdapat dalam 10 gram glukosa (C6H12O6), diketahui Ar C = 12, O = 16, serta H = 1.

      Jawaban:
Mr glukosa = (6 x 12) + (12 x 1) + (6 x 16) = 180
Mol = 10/180  = 0,05
""")
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Hukum proust</h2>", unsafe_allow_html=True)
        st.write(
            """
 Bunyi hukum Proust  “perbandingan massa unsur-unsur penyusun suatu senyawa selalu tetap”
 """)
        st.image("https://lh3.googleusercontent.com/Yki-PivXC7_1r-jpieqJWwfrSQpZf5TQcMon-z2Ku5sp8g2qBCIHdXtTv6hOXKQ3FPgW_O80b9ooQpdcXH6753_sEtm5IQFHmILjjTHdu_-0Bn5GS4aMGoCedweRUPCSKGRvbpK4FEt0qgaoVbJYVf90jxtjN66iG7VpDVKxgmmEsWxhQYOKt_1-g-saUBlC1mxGarZAAJuC4qlrzG8CfsX8btvhB1UNm8Or7gUPZLXerzgZ_2MwlUcDYG-E-cLgLIED6DgoXLGNuZ_yBUDRg-EvywWffzWHkaVqVpVpUohxxXi5miIBhl5sd8AQtd3dBJgNoen9lz62QAHRG6_qYVwhzO7hWP00CFo06ZSZxGTi5Gl6CEOhA5EnQDA1PaUbp-1yt--lnDlQU8GKLlYjLvoM2i4tWRc7-ZkI3YkR0GSXmWe2_N6bvJIxW9E6WQwPnnrEeGeMY10zQThR9jAuTHXY6tjo26deEXFC1hsX5eUpLJuoiP67GFBQcbqO-CwkWAfCxQCpTYZdMyzxLTm-xhN3TVVGz2SfFh_5iLb1jVFh3r5LCOEkYvkJeV0UDdEVYSDqoVdxWhBQq1n4hObtwYgjlg18Gv8-5-naO3DeUjpIaTOq4NHly1-GwqdW1SIjXBZFHfZgk2UNg0H2kU7Ole1m8PRWjquAlab0MrMwTMLrteiKwSsBE1aasrEKLuieUk200SmOnY9RH9P2p3i-qsut7cBTnvqbps2_SIQ66JJ5zDuHTDXoXP8F_aPAl3Zexs_15ATlbNnDZ33vBykouJ0-s9vFVQeF51sKCHxf_eD_-31eEuEJKHZ9Wi03P_zCuPscN5sqmJkbZiSjOx_8flRnqZBjkj7zeZlg34fmHmTI_vJ5aSfZExDHG2sXTQYxv8ks3-C04r2uYFlLD7_7Xg2zUi5pTAHA2MfKBQHKalINLlE=w959-h432-s-no?authuser=0")
        st.write(
            """
            
      Contoh :
   
   Berapa % kadar Fe dalam Fe2O3  
   
   Jawab :
   
   % = ((2 × 56 g/mol) )/(160 g/mol × 100) = 70 %
   """)
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Konsep ekuivalen & Berat Ekuivalen (BE)</h2>", unsafe_allow_html=True)
        st.write("""
        Rumus ekuivalen dan berat ekuivalen
        
        grek = g/BE
         
      BE = BM/a
         
  BE = berat ekuivalen (g/grek atau mg/mgrek)
  
  a = valensi yang nilainya tergantung reaksi
  
  **Berat Ekuivalen (BE) Reaksi asam basa**
  
        BE asam = (BM asam)/(jumlah H+)          
        
      BE Basa = (BM asam)/(jumlah OH-)
        
  **Berat Ekuivalen (BE) Reaksi redoks**
  
        BE zat = (BM zat)/(Jumlah elektron yang terlibat)
        
  **Berat Ekuivalen (BE) Reaksi penggaraman**
  
        BE garam = (BM garam)/(Muatan anion × jumlah anion )
  
      BE garam = (BM garam)/(Muatan kation × jumlah kation )
        
        """)
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Molaritas (M)</h2>", unsafe_allow_html=True)
        st.write(
            """
Molaritas menyatakan banyaknya mol solute yang terdapat dalam 1 liter atau 1000 mL larutan
Rumus Molaritas : 

       M = mol/L = G/Mr × 1000/volume = g/(BM ×L)
       
Contoh : 

Berapa Normalitas H2SO4 dengan Molaritas = 0,25 M?

Jawaban :

N = 0,25 × 2 = 0,5 N
""")
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Normalitas (N)</h2>", unsafe_allow_html=True)
        st.write(
            """
Normalitas adalah ukuran yang menunjukkan konsentrasi pada berat setara dalam gram per liter larutan

      N =  greak/L = g/(BE ×L)
      
Contoh : 

Berapa Normalitas H2SO4 dengan Molaritas = 0,25 M?

Jawaban :

N = 0,25 × 2 = 0,5 N
""")
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Kadar Larutan Dalam Persen(%)</h2>", unsafe_allow_html=True)
        st.write(
            """
**Persen berat/berat (% b/b)**
      
      % b/b = (g solut)/(100 g larutan)
      
Contoh : 

Larutan NaOH 50% b/b = (50 g NaOH)/(100 g larutan)

**Persen volume (% v/v)**

      %v/v = (mL solut)/(100 mL solut)
      
Contoh : 

Alkohol 70 % (v/v) = (70 mL)/(100 mL larutan)

**Persen berat / volume (% b/v)**

      %b/v = (g solut)/(100 mL larutn) 
      
Contoh : 

NaCl 60 % (b/v) = (60 g)/(100 mL)
""")
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Bagian per sejuta (ppm : parts per million) & Bagian Permiliar (ppb:parts per billion)</h2>", unsafe_allow_html=True)
        st.write(
            """
Bagian tiap juta (ppm) menyatakan berapa jumlah bagian satu komponen dalam 1 juta bagian campuran

      ppm = mg/L = mg/kg
      
ppb = parts per billion dalam bahasa Indonesia bpm = bagian per milliar, berarti kandungan atau Konsentrasi dalam ppb jauh lebih encer dibandingkan dengan Konsentrasi dalam ppm. 
        
      ppb=1 µg/kg = 1 µL/L
      
contoh:

Hitunglah besar ppm 10 liter air apabila dilarutkan Natrium Hidroksida atau NaOH sebanyak 1500 mg.

jawab

ppm= mg/L = 1500 mg/10 L
""")
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Pengenceran</h2>", unsafe_allow_html=True)
        st.write(
            """
Rumus pengenceran :

(C1 x V1) sebelum diencerkan = (C2 x V2) setelah diencerkan

C adalah konsentrasi larutan (M, N, ppm, dan %), V adalahvolume larutan (L atau mL)
""")
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Hubungan antar satuan</h2>", unsafe_allow_html=True)
        st.write(
            """
•	Hubungan mol dengan grek = grek = mol x a

•	Hubungan molaritas dengan normalitas = N = M x a

•	Hubungan % (b/b) dengan % b/v = % (b/v) = % b/b x bj bj = berat jenis atau density

•	Hubungan % dengan ppm = 1% = 104 ppm
      
            
Daftar Pustaka:
            
Da lopez, Yos F. 2017. Konsentrasi Larutan dalam Satuan Kimia. Nusa Tenggara Timur (NTT): Politeknik Pertanian Negeri Kupang

Wardaya, Anton. 2014. Modul, Rumus, & Soal Hukum Proust (Hukum Perbandingan Tetap). Jakarta Barat: wardayacollege
""")
        st.caption("Download Materi")
        st.write("Google Drive: [link](https://drive.google.com/file/d/1YEEzMSlhS6j2v2EYRyXd5JQHVOsrZ_zD/view?usp=sharing)")

    if optionanjen == "Pemisahan Kation Golongan I-V":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Pemisahan Kation Golongan I-V</h2>", unsafe_allow_html=True)
        st.write(
            """
            Kation-kation diklasifikasikan dalam 5 golongan berdasarkan sifat-sifat kation itu terhadap beberapa reagensia, penggolongan ini didasarkan pada terbentuk atau tidaknya endapan jika suatu kation bereaksi dengan reagensia tertentu, reagensia golongan yang dipakai untuk klasifikasi kation yang paling umum, adalah asam klorida, hidrogen sulfida, amonium sulfida dan amonium karbonat.

     Proses analisis kation dan anion dilakukan dengan dua cara yaitu pemisahan dan identifikasi. Pemisahan dilakukan dengan mengendapkan kation dari larutannya. Endapan yang dihasilkan dipisahkan dengan mencuci larutannya dan dibuat larutan dengan jalan mengaduk menggunakan alat sentrifuge lalu membagi dua hasil penyaringan. Larutan yang masih mengandung kation lain lalu diendapkan juga sehingga terbentuk grup kation baru. Apabila di dalam grup tersebut masih terdapat kation lain, proses pengendapan dilakukan lagi sehingga tertinggal hanya satu kation saja.

     Jadi boleh dikatakan bahwa klasifikasi kation yang paling umum didasarkan atas perbedaan kelarutan dari klorida, sulfida, dan karbonat dari kation tersebut. Kelima golongan Kation dan ciri khas golongan-golongan ini adalah sebagai berikut:
            """)
        st.image("https://lh3.googleusercontent.com/pw/AJFCJaVt6CKvucA33DVeqEVl-6QePAnWHkG8UHERCUiXfZQ27yazt45GiSzKmipLUdX_g3jVsk0mQ16XBbpCe1gg63017HstAwuW1n7FSKsiXkrceQVi-WlpUUgq7BegNChpODNYYyxCxyHP7nRxZoXhX__O=w1124-h657-s-no?authuser=0")  
        st.write(
            """
Gambar 1. Bagan Pemisahan Kation (Sumber: Penuntun Praktik Analisis Jenis)
        
1.	Golongan I : Kation grup ini membentuk endapan dengan asam klorida encer. Kation Golongan I yaitu: Ag+, Hg2 2+, Pb2+
2.	Golongan II : Kation grup ini adalah kation-kation yang tidak bereaksi dengan asam klorida, namun membentuk endapan dengan asam sulfida dalam suasana asam mineral encer.
    Gol II A : Cu2+, Cd2+, Bi3+,
    Gol II B : As3+, As5+, Sb3+, Sb5+, Sn2+, Sn4+
    Sulfida dari kation dalam golongan IIA tak dapat larut dalam amonium polisufida, sulfida dari kation dalam golongan IIB justru dapat larut.
3.	Golongan III : Kation grup ini tidak bereaksi dengan asam klorida encer maupun dengan asam sulfida dalam suasana asam mineral encer. Namun, kation ini membentuk endapan dengan amonium sulfida dalam suasana netral atau amoniakal.
    Gol III A : Fe2+, Fe3+, Al3+, Cr (III), Cr (VI)
    Gol III B : Zn2+, Co2+, Ni2+, Mn (II), Mn (IV)
4.	Golongan IV : Kation yang termasuk dalam grup ini adalah kation yang tidak bereaksi dengan pereaksi-pereaksi Golongan I, II dan III. Kation-kation ini membentuk endapan dengan amonium karbonat dengan adanya amonium klorida, dalam suasana netral atau sedikit asam.
    Gol IV : Ba2+, Ca2+, Sr2+
    Beberapa sistem klasifikasi golongan meniadakan pemakaian amonium klorida disamping amonium karbonat sebagai reagensia golongan; dalam hal ini, magnesium harus juga dimasukkan ke dalam golongan ini. Tetapi, karena dalam pengerjaan analisis yang sistematis, amonium klorida akan terdapat banyak sekali ketika kation-kation golongan keempat hendak diendapkan, adalah lebih logis untuk tidak memasukkan magnesium ke dalam Golongan IV.
5.	Golongan V : Kation-kation yang umum, yang tidak bereaksi dengan pereaksi pereaksi golongan I, II, III dan IV merupakan golongan kation yang terakhir, yang meliputi ion-ion magnesium, natrium, kalium, amoium, lilitium dan hidrogen.
   """)
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Pemisahan kation golongan I</h2>", unsafe_allow_html=True)
        st.write("""
     Kation golongan I yaitu Pb2+, Hg2 2+, dan Ag+ . Kation ini membentuk endapan putih ketika bereaksi dengan HCl encer. Endapan yaang terbentuk antara lain; PbCl2, Hg2Cl2, dan AgCl. Berikut reaksi pengendapan kation golongan I oleh asam klorida encer.
   
• Ag+ (aq) + Cl(aq) → AgCl(s) (endapan putih)
      
• Pb2+ (aq) + 2 Cl(aq) → PbCl2(s) (endapan putih)
    
• Hg2 2+ (aq) + 2Cl(aq) → Hg2Cl2(s) (endapan putih)
    
    """)
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Pemisahan kation golongan II</h2>", unsafe_allow_html=True)
        st.write ("Setelah ditambahkan hidrogen sulfida, kemudian saring menghasilkan filtrat dan residu (Golongan III). Filtrat ini mungkin terdiri dari sulfida-sulfida logam logam IIA (HgS, PbS, Bi2S3, CuS) dan sulfida-sulfda logam golongan IIB (As2S3, Sb2S3, Sb2S5, SnS2). Pemisahan golongan IIA dan IIB dilakukan dengan mencuci dengan sulfida yang diendapkan dengan sedikit larutan NH4Cl yang telah dijenuhi H2S.")
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Pemisahan kation golongan III</h2>", unsafe_allow_html=True)
        st.write("Pemisahan kation-kation golongan III dan golongan-golongan lain yaitu dengan menambahkan H2O dan Panaskan, kemudian saring menghasilkan residu dan filtrat (Golongan IV). Endapan yang dihasilkan tersebut ditambahkan sedikit air, NH4Cl serta larutan NH3 dan panaskan hingga mendidih, kemudian saring menghasilkan residu dan filtrat. Residu mungkin mengandung golongan III.A yaitu MnO- , Fe(OH)3, Cr(OH)3, dan Al(OH)3, dan filtrat mungkin mengandung CoS, NiS, MnS, dan ZnS.")
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Pemisahan kation golongan IV</h2>", unsafe_allow_html=True)
        st. write("Hasil filtrat yang diperoleh dari pemisahan kation golongan III, mungkin mengandung golongan IV dan V. Cara pemisahannya dilakukan dengan penambahan reagen natrium heksanitritokobaltat(III) sebanyak 5 mL, kemudian saring menghasilkan residu dan filtrat (mungkin golongan V). Pemisahan Kation Golongan IV dengan Metode Sulfat yaitu residu yang dihasilkan mungkin mengandung BaCO3, SrCO3 dan CaCO3")
        st.write(
            """
            Daftar Pustaka:
            
            Svehla,G.1990.Buku Teks Analisis Anorganik Kualitatif Makro dan Semimikro.Jakarta: PT. Kalman Media Pustaka 
        
        """)
        st.caption("Download Materi")
        st.write("Google Drive: [link](https://drive.google.com/file/d/1nNtSU-ZxXD4xd_w0tBYA09KwL6vMIht3/view?usp=sharing)")
        
 
    if optionanjen == "Identifikasi Zat Dengan Cara Kering":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Identifikasi Zat Dengan Cara Kering</h2>", unsafe_allow_html=True)
        st.write(
            """
            Analisis kualitatif secara konvensional dapat dilakukan secara visual melalui 2 uji yaitu uji reaksi kering dan uji reaksi basah.Uji reaksi kering adalah pengujian yang diterapkan dalam keadaan kering dan tanpa proses pelarutan sampel, cara uji reaksi kering antara lain: Sifat fisik, Reaksi nyala, Pipa tiup, Mutiara boraks
Pengamatan dalam uji kering meliputi
•	Bentuk
•	Warna
•	Bau
•	Warna nyala 

**Teknik uji dalam uji reaksi kering yaitu:**

**1.	Sifat fisik** 

Dalam sifat fisik yang perlu diperhatikan:
-	Pengamatan bentuk
bentuk harus diperhatikan secara seksama,apakah berupa padatan atau cairan
-	Pengamatan warna
beberapa senyawa berwarna yang secara umum dijumpai 

**2.	Reaksi Nyala**
""")
        st.image("https://lh3.googleusercontent.com/pw/AJFCJaWTmFIrwBdG4ppNH5VxR_7wwOwsA-dXrey65mtG2E_EuBxx8-luM3cBDFdzAvH_ff2UEnlBVAepSOX2UZzVL9OR8pWBW-M_1nDcYI_uswWc9qgl8UqFnBHEQkJ6Jq5YdSW51NIZIv1UuaJAkqzRloOn=w407-h192-s-no?authuser=0")
        st.write(
            """
            Gambar 1. Uji nyala (Sumber: yuninainggolan.wordpress)
            
Uji nyala api adalah suatu prosedur analisis yang digunakan dalam ilmukimia untuk mendeteksi keberadaan unsur tertentu, terutama ion logam, berdasarkan karakteristik spektrum emisi masing-masing unsur, ide pengujian ini adalah bahwa atom-atom sampel menguap dan karena panas, mereka mengemisikan sinar ketika berada dalam nyala api.

Prosedur Kerja:
1. Disiapkan kristal NaCl dalam kaca arloji.
2. Diisi 2 tabung reaksi masing-masing dengan 1 mL HCl pekat.
3. Dicelupkan   ujung   kawat   nikrom   dalam   tabung   reaksi   1   dan
dimasukkan   dalam   nyala   api   bunsen.   Dilakukan   hal   ini   sampai
kawat tidak memberikan warna lain.
4. Dicelupkan ujung   kawat  nikrom   tersebut   dalam  tabung  reaksi  2
kemudian dalam kristal NaCl.
5. Diamati   warna  nyala   yang  terjadi  dan   dicatat   hasil   pengamatan
kalian.
6. Diulangi kegiatan yang sama untuk kristal yang lain.
Disiapkan kristal NaCl dalam kaca arloji.
""")
        st.image("https://lh3.googleusercontent.com/pw/AJFCJaUbNmKYlJvm1kSb2f69YsPI9CxAJHD0XLazF_pygMRyM_xRiuahvJuKvIiiiR67azAo6BXscGOdZtKMH0T13URaBZXww-jtl53cOC4RtODj7cWD_3hTni7GUYs1vzfTiz8eYKjihb6JR_beeuIOAPbq=w609-h657-s-no?authuser=0")
       
    
        st.write(
            """
**3. Uji Pipa Tiup**

Uji pipa tiup bertujuan untuk membebaskan logam tertentu dari sampel tertentu yang memiliki warna yang khas
""")
        st.image("https://lh3.googleusercontent.com/pw/AJFCJaXOQ7FZ8lhtV7DFZThINJZUnufyOLw986lIOV8hPE0ohxQN9GyXJAE8VMlhAj-iqKoHCLrVTo7aXiI_-Qklt4huhdhm9X8lrxyzZFGgJ-3iViAdzTtXdSdiBrqC_WEuAIr4X3-K_IvvswurD_mQwBTl=w739-h415-s-no?authuser=0")
        st.write(
            """
Prosedur kerja
1.  Campurkan di dalam mortar garam yang akan di periksa dengan Na2CO3(perbandingan 1:2) gerus sampai halus.Buat gerukan pada permukaan arang kayu.
2.  Nyalakan bunsen perlahan sampai di dapat nyala api TB. Kemudian panaskan campuran yang ada
3.  Siapkan sebongkah arang, lubangi arang kurang lebih 1,5cm. Sampel yang sebelumnya dilarutkan  dengan pereaksi dalam plat tetes dimasukan kedalam arang.
4.  Arang yang telah diisi sampel simpan diatas kassa asbes dan nyalakan api.
5.  Tiupkan dengan pipa tiup, arahkan pada zat sampai semuanya bereaksi. Ambil sampel yg ada dalam arang dan masukan ke dalam tabung reaksi lalu tambahkan pereaksi tertentu.
""")
        st.image("https://lh3.googleusercontent.com/pw/AJFCJaWBEClod3ldjqvtOp4kOw5K8m0qsqIMraHFiyXtXl9JH20sI73vcN4gZhxKedtSePTunuw-s33WCnc2Li0OazHffc9EZ0fkrBO7uGs8GcU4sBm0JTznYQrBmGuq2ym7ByTM2g_qouw6YkejUoyiGgOO=w527-h233-s-no?authuser=0")
        st.write(" ")
        
        st.write(
            """
**4. Uji Mutiara Boraks**
""")
        st.image("https://lh3.googleusercontent.com/pw/AJFCJaXuaz4j1r4kN5PpsK6ZqDwr8ISh0A8bEMZ_zExvZArLzvjiDA-pviCjX6UPjHCrQXS-S7fVH67qpGrDaCcTlzzl0vCPJsbKgTlklOhf-wn6YfWKiySiX6XFaA6IY8X88Etdz8yqDsqS5CyDOmgrhv9T=w739-h415-s-no?authuser=0")
        st.write(
            """
            Gambar 3. Uji Mutiara Boraks (Sumber: davin tiska abriani)
            
pengamatan warna nyala sampel pada manik boraks yang dipanasi diatas nyala api oksidasi dan reduksibaik dalam dingin ataupun panas dapat diperoleh warna yang menunjukkan apakah zat itu mengandungkation atau anion. Jika sampel mengandung anion logam maka saat dipanaskan pada nyala api akanmengeluarkan warna nyala mutiara boraks yang spesifik.
     
 Prosedur Kerja
 
-	Kawat platina dipijarkan (sampai merah)
-	Kawat dimasukkan ke dalam boraks (bubuk halus)
-	Kawat dipanaskan lagi sampai terbentuk butiran tak berwarna dan transpara (tembus cahaya),
-	Mutiara panas disentuhkan ke zat uji
-	Dipanaskan dalam api pengoksidasi dan api pereduksi
""")
        st.image("https://lh3.googleusercontent.com/pw/AJFCJaXiOVJX1JoTaC5enyf11ngrq7mb9RpnzeVkC8KxcYKjhHRykwzLYE6CcJo-QAMHD9wGujSP99hvN1ouvdA9Qu1ffM37Ms7LaWZdt9cSxi3puLyVFs0pReHjSWfEFr-8z6rQ6Y5ArVRLYUfa8rG-U0bN=w384-h293-s-no?authuser=0")
        st.caption("Download Materi")
        st.write("Google Drive: [link](https://drive.google.com/file/d/1ScSsWu9PxEWEXU6g3RbpDOOg7V_5-fhF/view?usp=sharing)")
        
    if optionanjen == "Pemisahan Anion Golongan I-V":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Pemisahan Anion Golongan I-V</h2>", unsafe_allow_html=True)
        st.write(
            """
            Klasifikasi anion ini adalah salah satu contoh pengelompokan anion yang dibagi berdasarkan reaksinya dengan asam klorida encer (HCl(aq) ) dan perbedaan kelarutannya sebagai garam barium dan perak. Empat golongan anion dan karakteristiknya adalah sebagai berikut:
            """)
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Anion Golongan I</h2>", unsafe_allow_html=True)
        
        st.write(
            """
            Anion golongan ini bereaksi dengan HCl(aq) menghasilkan gas atau endapan, yaitu karbonat, silikat, sulfida, sulfit, dan tiosulfat
  
Reaksi Karbonat:
            
            CO3 2- + 2H+ → CO2(g) + H2O
            
Reaksi Silikat:

           SiO3 2- + 2H+ → H2SiO3(s)
           
Reaksi Sulfida:

           S2- + 2H+ → H2S(g)
           
Reaksi Sulfit:

           SO3 2- + 2H+ → SO2(g) + H2O
           
Reaksi Tiosulfat:

           S2O3 2- + 2H+ → S(s) + SO2(g) + H2O
           """)
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Anion Golongan II</h2>", unsafe_allow_html=True)
        st.write( 
             """
             Anion golongan ini tidak bereaksi dengan HCl(aq) namun membentuk endapan dengan ion barium pada kondisi netral. Anion golongan ini adalah sulfat, fosfat, fluorida, dan borat

Reaksi sulfat: 

    SO4 2- + Ba2+ → BaSO4(s)

Reaksi Fosfat:

    2F - + Ba2+ → BaF2(s)

Reaksi Borat:

    B4O7 2- + 2Ba2+ + H2O → 2Ba(BO2 )2(s) + 2H
""")

        st.markdown("<h2 style='text-align: center; color: raisin black;'>Anion Golongan III</h2>", unsafe_allow_html=True)
        st.write(
            """
            Anion golongan ini tidak bereraksi dengan HCl(aq) maupun ion barium, namun membentuk endapan dengan ion perak dalam media asam nitrat encer. Anion golongan ini adalah klorida, bromida, iodida, dan tiosianat.
            
Reaksi Klorida: 

          Cl- + Ag+ → AgCl(s)
          
Reaksi Bromida:

         Br- + Ag+ → AgBr(s)
         
Reaksi Iodida: 

         I - + Ag+ → AgI(s)
         
Reaksi Tiosianat:

         SCN- + Ag+ → AgSCN(s) 
         """)
        
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Anion Golongan IV</h2>", unsafe_allow_html=True)
        st.write(
            """
            Anion-anion yang tidak bereaksi dengan pereaksi-pereaksi di atas dikelompokkan pada golongan ini, yaitu ion nitrit, nitrat, dan klorat
            """)
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Identifikasi Produk yang mudah menguap</h2>", unsafe_allow_html=True)
        st.write(
            """
            Gas yang dilepaskan dengan HCl atau H2SO4 encer : (karbonat, bikarbonat, sulfit, tiosulfat, sulfida, nitrit, hipoklorit, sianida, dan sianat) Gas atau uap asam yang dilepaskan dengan H2SO4 pekat : (fluorida, heksafluorosilikat, klorida, bromida, iodida, klorat, perklorat, permanganat, bromat, borat, heksasianoferat (II), heksasianoferat (III), tiosianat, format, asetat, oksalat, tartrat
dan sitrat)

Contoh Reaksi anion karbonat (CO32-) dari larutan garam natrium karbonat penta hidrat (Na2CO3.10H2O) dengan HCl encer:

         CO32-(aq) +2H+(aq)=CO2+ H2O(l)
         
 Identifikasi dilihat dari :
- Berbuih
- Mengeruhkan air kapur :

    CO2(s)+ Ca2+(aq) + 2OH-(aq)=CaCO3(s)putih + H2O(l)

    CO2(s)+ Ba2+(aq) + 2OH-(aq)=BaCO3(s)putih + H2O(l)

Contoh Reaksi anion sulfit (SO32-) dari larutan garam natrium sulfit hepta hidrat (Na2SO3.7H2O) dengan HCl encer:

    SO32-(aq) + 2H+(aq)=SO2(aq) + H2O(l)

Identifikasi dilihat dari :
- bau belerang terbakar yang menyesakkan nafas
- warna hijau (terbentuk dari ion Cr3+ yang dihasilkan jika sehelai kertas saring yang telah dibasahi larutan K2Cr2O7 yang telah diasamkan,dipegang diatas mulut tabung reaksi.

Daftar Pustaka:
            
Svehla,G.1990.Buku Teks Analisis Anorganik Kualitatif Makro dan Semimikro.Jakarta: PT. Kalman Media Pustaka 
        
""")
        st.caption("Download Materi")
        st.write("Google Drive: [link](https://drive.google.com/file/d/1HJm0txtr--xvcj2rKRQ9bOhwIgSabtu0/view?usp=sharing)")
        
        
    if optionanjen == "Pembuatan Larutan":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Pembuatan Larutan</h2>", unsafe_allow_html=True)
        st.write(
            """
            Cara membuat larutan perlu diperhatikan,yaitu cara membuat larutan  dari bahan  cair atau padat dengan menggunakan  konsentrasi tertentu. Larutan adalah campuran homogen dari dua atau lebih zat  yang berbeda komposisinya. Suatu larutan dalam volume kecil disebut zat  terlarut. Pelarut didefinisikan sebagai zat yang jumlahnya melebihi zat lain.
            """)
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Cara Pembuatan Larutan</h2>", unsafe_allow_html=True)
        
        st.write(
            """
•	Menimbang kristal senyawa atau memipet dari larutan pekat

•	Hasil penimbangan dan pemipetan dilarutkan dalam volume tertentu

•	Larutan yang dibuat harus dengan konsentrasi tertentu

•	Larutan disimpan dalam botol/ wadah yang sesuai

•	Botol atau wadah penyimpanan harus diberi label
""")
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Informasi Yang Ada Pada Label</h2>", unsafe_allow_html=True)
        st.write(
            """
•	Nama senyawa kimia/ Rumus kimia senyawa dari larutan yang dibuat

•	Konsentrasi larutan

•	Tanggal pembuatan

•	Tanggal kadaluarsa

•	Sifat bahan bahan kimia

•	Inisial pembuat larutan
""")
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Alat Yang Digunakan Untuk Pembuatan Larutan</h2>", unsafe_allow_html=True)
        st.write(
            """
•	Labu takar

•	Beaker glass

•	Kaca arloji

•	Pipet

•	Batang pengaduk

•	Labu semprot

•	Corong

•	Bulp
""")
        st.caption("Download Materi")
        st.write("Google Drive: [link](https://drive.google.com/file/d/12ZVIMB3NRyBopmbTfveV_GPcmlg4wltK/view?usp=sharing)")
        

        


      
#Materi Titrimetri
with tab_3:
    optiontitri = st.selectbox(
            "Pilih materi yang kamu mau",
            ("--- Pilih Materi ---", "Pengenalan Analisis Titrimetri","Asidimetri-Alkalimetri","Asidimetri","Alkalimetri","Permanganometri","Iodometri"))
    if optiontitri == "Pengenalan Analisis Titrimetri":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Pengenalan Analisis Titrimetri</h2>", unsafe_allow_html=True)
        st.write(
            """
            **Definisi**

Analisis volumetri /analisis titrimetri adalah teknis analisis yang berdasarkan pada volume suatu larutan yang sudah diketahui konsentrasinya yang diperlukan untuk bereaksi sempurna dengan sejumlah tertentu komponen cuplikan (sampel).
             """)
        imageT1 = Image.open('Resource/image/Titri/Titri_1.png')
        st.image(imageT1)
        st.write(
            """
            Istilah dalam analisis volumetri/titrimetri:
            
•	Titrasi adalah proses penambahan larutan standar dari buret sedikit demi sedikit sampai jumlah zat yang direaksikan tepat ekuivalen satu sama lain.
•	Titran adalah zat yang diketahui konsentrasinya yang digunakan untuk menitar zat lain
•	Titrat adalah zat yang dititrasi
•	Titik ekuivalen (setara) adalah titik pada saat titran yang ditambahkan tepat ekuivalen dengan titrat maka penambahan titran harus dihentikan
•	Titik akhir titrasi adalah titik pada saat titrasi dihentikan yang ditandai oleh perubahan warna dari indikator
•	Indikator : Zat yang ditambahkan ke dalam titrat sebagai penunjuk titik akhir titrasi
•	Larutan standar (larutan baku) adalah larutan yang konsentrasinya diketahui secara pasti

**Prinsip /reaksi titrimetri**
•	aA + tT → produk 

A = Analit
T = zat penitar (titran)
a dan t = jumlah molekul / koefisien reaksi

•	Prinsip reaksi titrasi volumetri :
mgrek titran = mgrek titrat



Syarat-syarat reaksi dapat digunakan sebagai reaksi titrasi:

1.	Berlangsung sempurna, tunggal dan menurut persamaan yang jelas.
2.	Reaksi berlangsung cepat
3.	Ada penunjuk titik akhir ( indicator)
4.	Larutan baku yang direaksikan dengan analit harus mudah didapat dan sederhana    menggunakannya, harus stabil sehingga konsentrasinya tidak berubah sewaktu disimpan.

**Problema dalam titrasi:**

a.	
1.	Cara menentukan titik akhir harus tepat
2.	Cara menghitung jumlah analit
3.	Cara menentukan konsentrasi larutan baku dengan teliti
4.	Titrasi yang baik,perubahan: warna/kekeruhan harus terjadi tepat pada saat titran telah ekuivalen dengan titrat, titik ekuivalen tepat sama dengan titik akhir
    
b.	Umumnya titik ekuivalen tidak sama dengan titik akhir sehingga terjadi kesalahan titrasi. Kesalahan yang terjadi tidak boleh lebih dari 0,1 %

c.	Kesalahan positif : Jumlah yang dipakai lebih dari yang sesungguhnya diperlukan untuk ekuivalen

**Penggolongan titrasi berdasarkan reaksinya**
1.	Titrasi Asam-Basa (Asidimetri-alkalimetri)
2.	Titrasi Redoks (Permanganometri dan Iodometri)
3.	Titrasi Pengendapan (Argentometri)
4.	Titrasi Kompleksometri

**Berdasarkan cara titrasi**
1.	Titrasi langsung, 
cara ini dilakukan dengan melakukan titrasi langsung terhadap zat yang akan ditetapkan. Cara ini mudah, cepat, dan sederhana
2.	Titrasi tidak langsung, 
analit direaksikan dengan suatu pereaksi ,kemudian hasil reaksi di titrasi (analit tidak langsung terlibat dalam titrasi)
3.	Titrasi balik /titrasi kembali ( _back titration_ ), 
analit direaksikan dengan pereaksi berlebih. Dan kelebihan pereaksi di titrasi
            """)
    if optiontitri == "Iodometri":
       st.markdown("<h2 style='text-align: center; color: raisin black;'>Iodometri</h2>", unsafe_allow_html=True)
       st.write(
          """
                 Iodometri (titrasi tidak langsung)
Analit → Oksidator (KIO3, K2Cr2O7)
Oks(analit) + KI ⇋ I2 + Red(analit)
I2 + 2S2O32- ⇋ 2I- + S4O62-

IO3- + 5I- + 6H+ ⇋ 3I2 + 3H2O (pH rendah)
Cr2O72- + 6I- + 14H+ ⇋ 2Cr3+ + 3I2 + 7H2O (pH rendah)

Reaksi I2 dengan S2O32- berlangsung sempurna dan cepat 
Reaksi unik karena oksidator lain tidak mengubah S2O32- menjadi S4O62- melainkan menjadi SO32- dan SO42-

Titrasi tanpa Indikator :
• Lenyapnya warna I2 (coklat tua - kuning - bening)

Titrasi dengan Indikator Amilum/kanji :
• Lenyapnya warna I2 (coklat tua - kuning - biru tua - bening)

 Amilum + I2 membentuk kompleks berwarna biru tua, sangat jelas walaupun I2 sedikit sekali
 
Titik akhir : iod yang terikat dengan amilum itu pun hilang bereaksi dengan titran (S2O32-) sehingga warna biru hilang
Titran Na2S2O3 yang digunakan dari garam pentahidrat (Na2S2O3.5H2O)

Larutan stabil pada pH 9 dan 10 untuk meminimalkan
bakteri yang dapat menguraikan S2O32- menjadi SO32- , SO42-, dan S↓
Titik akhir : iod yang terikat dengan amilum itu pun hilang bereaksi dengan titran (S2O32-) sehingga warna biru hilang

**Kesalahan titrasi**
Kesalahan Oksigen
O2 diudara dapat menyebabkan hasil titrasi terlalu tinggi karena dapat mengoksidasi
4I- + O2 + 4H+ → 2I2 + 2H2O
Reaksi ini dikatalisis oleh cahaya dan panas

Penambahan Amilum terlalu awal
I2 menguap karena terlalu lama menunggu titrasi pH tinggi, S2O32- teroksidasi secara parsial menjadi SO42-
4I2 + S2O32- + 5H2O → 8I- + 2SO42- + 10H+
    
**Bobot Ekivalen**
Dalam titrasi iodometri, BE suatu zat dihitung dari banyaknya jumlah atom I, bukan jumlah ion I-
BE= BM/n atom I
""")
    if optiontitri == "Permanganometri":
       st.markdown("<h2 style='text-align: center; color: raisin black;'>Permanganometri</h2>", unsafe_allow_html=True)
       st.write(
           """
          **Pengertian titrasi redoks**
Titrasi yang melibatkan reaksi reduksi dan oksidasi antara titran dan titrat hingga tepat ekuivalen

**Jenis Titrasi Redoks**
1. Oksidator kuat sebagai Titran
KMnO4 (Permanganometri)
K2Cr2O7
Ce (IV)
2. Reduktor kuat sebagai Titran
Ti (III)
Fe (II)
Na2S2O3
3. Na2S2O3 sebagai Titran
Iodometri (Tak langsung)
4. I2 sebagai Titran

**Iodometri (langsung)**
Oksidator kuat sebagai Titran	
KMnO4 (Permanganometri)
Kalium permanganat adalah oksidator kuat yang dapat bereaksi dengan cara yang berbeda tergantung kondisi pH
Dalam larutan asam [H+] 0,1 N
MnO4- + 8H+ + 5e ⇋ Mn2+ + 4H2O
b. Larutan netral/sedikit basa pH 4-10
     MnO4- + 4H+ + 3e ⇋ MnO2    + 2H2O
     MnO4- + 2H2O + 3e ⇋ MnO2   + 4OH-
Larutan sangat basa [OH-] 0,1 N 
MnO4- + e ⇋ MnO4

**Titrasi langsung**                           
Fe2+
Sn2+
Fe(CN)6 4-
HNO2

**Titrasi tidak langsung**
Ba2+
Ca2+
Pb2+
Zn2+
Hg2+

**Titrasi langsung**
5Fe2+ + MnO4- + 8H+ ⇋ 5Fe3+ + Mn2+ + 4H2O

**Titrasi tidak langsung**
Sampel diendapkan sebagai oksalat
Disaring, dicuci 
Dilarutkan dalam H2SO4 berlebih sehingga terbentuk asam oksalat
Dititrasi asam oksalat dengan KMNO4
Ca2+ + C2O42- ⇋ CaC2O4 ↓
CaC2O4↓ + 2H+ ⇋ Ca2+ + H2C2O4
5H2C2O4 + 2MnO4- + 6H+ ⇋ 10CO2 + 2Mn2+ + 8H2O
KMnO4 bertindak sebagai auto indikator
Warna titik akhir titrasi berasal dari KMnO4

 **Pembuatan dan Penyimpanan KMnO4**
 
""")
       st.image("https://lh3.googleusercontent.com/IMhCdyGJ45Ml9P7nPOtOyv56IzGYKuSU5qsQRncFSJ2ArKNaumtOiHNkClu0b5edpStjorldhFisw7Fv4yMo2kcVhHwi8m7cj74s9Si6jPfrx5lTO3aiPKyIJ0vwqwDJU-qBNOpSnXkvhCyh7e9TfjFE96nBd0-GXmHz0cRL6D-PnXofxjINw0Gi7qSgKaw15QtDmggv5sYwkW1btu6wJlkoDu7mmZHWlhC9YiezBwV-sOZU2PvkqhyoJYtmb1ijr-ozprFsFtbO1rWyzxhi153_4EpVCnC1spCSjn9sftoNU9Xx7GyKrjSWFhot3RSOPonfQfHwFDPsvWdhbZTebRRhbN8WxDRSCpOL_VpZMBqfm9lhqrrLrzx2deRziqFqemeTLxLxk6KWbUlCbSAmHLYt45KHZr6qjAbyq4fQXt7_f31Rgb3RrGG0bzmljnqh0qIRCAjp30H0inGegsAsKfPG2zUKXkhvLOo7NZmYpzCRybi5c6bMIf7cG599NrIArCd9igdwH7vv4IX1zd_eFTTl8T7PnWsf9eoX1MfrUJ9OqXwQIPl_R1zQA0tu_N4BnjeBjUZjxzGBSAovkQm58VXAbwOMKDNN6mynqkRZ-Ey1O-HE28iSyyhKF0OXdxYkKYd-EQd2iT6pw_F3G9rsbJSjjGzgrHV51RW45fu-WV8ODOT2sOTagPrALeUfUTxUY4Ccy2gEIewm-uamtMfSJOMPi3V4O-QqudtX9fOP44rW1WPcgfJivGrX0ER5_l9wVKUcyxDrcmquAp1qOHsIAZNnTYb0KbYA-Qssj6NWqWTNm0ChBzhB6i8qbKaRtdBMWPV0-EY9je3MIAaTGpUggKeXR6WWPNXNM9rFTct57UqKPc7FQDqN0Fo-qwo43WmUyuDOjCJohNH3kafBVGNGUVQycvfkwPpEqULcY3956EkD=w1188-h658-s-no?authuser=0")
       st.write(
       """
     **Kesalahan titrasi**
Kesalahan Positif
Penambahan KMnO4 terlalu cepat,menyebabkan terjadinya reaksi MnO4- dengan Mn2+ 

Kesalahan Negatif 
Penambahan KMnO4 terlalu lama, menyebabkan hilangnya oksalat karena membentuk peroksida yang terurai menjadi air

H2C2O4 + O2 ⇋ H2O2 + 2CO2↑
H2O2 ⇋ H2O + O2 ↑

**K2Cr2O7 (Kalium Dikromat)**
Kalium dikromat adalah oksidator yang lebih lemah daripada KMnO4 dan Ce(IV), namun sangat stabil dan inert terhadap Cl- 
Dalam suasana asam, K2Cr2O7 mengalami reduksi menjadi
 Cr3+Cr2O7 2- + 14H+ + 6e ⇋ 2Cr3+ + 7H2O
Memerlukan indikator redoks, yaitu zat yang dapat dioksidasi/ reduksi dan berubah warna akibat reaksi tersebut
Penentuan Fe2+ digunakan indikator asam difenilamin sulfonate

**Ce(IV) (Serium Tetravalen)**
Serium tetravalen yang digunakan dalam bentuk garam

• Ce(NO3)4.2NH4NO3

• Ce(SO4)2.2(NH4)2SO4.2H2O

•Ce(HSO4)4  

Ce4+ mengalami reduksi menjadi Ce3+ Ce4+ + e ⇋ Ce3+
Kelebihan

• Larutan stabil dalam H2SO4

• Hasil reaksi tunggal

• Tidak mengoksidasi Cl-

Kekurangan

• Larutan stabil dalam H2SO4

• Hasil reaksi tunggal

• Tidak mengoksidasi Cl-

• Hanya larut dalam asam

• Membentuk endapan dalam basa

• Harga tinggi

• Memerlukan indicator redoks : Fe(II)- ortofenantrolin (ferroin)

**Reduktor kuat sebagai Titran**
Ti (III), Fe(II), Na2S2O3
Ti (III) mudah teroksidasi oleh udara, sehingga perlu penanganan khusus
Proses titrasi dilakukan dalam atmosfer inert (mengalirkan N2atau CO2)
Fe (II) mudah teroksidasi oleh udara dalam larutan netral, sehingga larutan harus dalam suasana asam 
Na2S2O3 iodometri (titrasi tidak langsung)
""")
    if optiontitri == "Asidimetri-Alkalimetri":
       st.markdown("<h2 style='text-align: center; color: raisin black;'>Asidimetri-Alkalimetri</h2>", unsafe_allow_html=True)
       st.write(
           """
           Asidimetri-alkalimetri
Asidimetri adalah Bila ditentukan berapa mL larutan asam yang konsentrasinya diketahui untuk menetralkan suatu larutan basa yang kadarnya dicari.
Alkalimetri adalah bila penitar dengan memakai basa yang konsentrasinya diketahui untuk menetapkan suatu asam
""")
       st.image("https://lh3.googleusercontent.com/K7bmKtS-Ya75TDaiZUL6_ZAVyZZ7D19-vBrmUTaSKKsFuqWnimVMVHxrKfypBz66vrEKoHW7RvK9KRN5UZmCwrUekfGHj678FnW-JqNXCie95tt71ES90xeOfW4rXXCZXTnzncprL4XY7Mom1m3bdatP0d7FxHzaKKy-s_69DYf5OMF6LhofxdY8vB-60lxGixuI1JQpmZHr5BfOW2SBo5Gs7xvp34Zomr_LwxUq5_A3SGsqpz3rXIsbyF3YOCAz5w22mlfd9y1MmWdibeald91AcEkgoEKWmJ6cxtoI6WISiWIcMf5krEbif5VsDLRgVRO6CWLcBasKnq5CRIN1ax6dmkf8liQLwGhHrVALuSLY9AwPPsAsmZe0-G1MdDH6RNuCZgac7QdUjt67ebBYcTyYOzpF41N3iVblQKFzGLQMH7Jtv8QYZwtVED5qriBQ1bSkLEUxwPgWONGpd3vKGjV8gUBo3tnFoCj5Uzd8x9lJeNU5IxFqc_s0bKvI941M3PR7dca7AVMWGAHZoX7_r2FFd8DGoqJPUL2ZASnSUn_Bx6DJPHtpi1_Ke_Jp5zZBXEVFyAI-pIiAyYnw8THYC7J1P3rR2QdRIQjOWRXQv39Q44w2LReNUrpsn7zMHlYBTF9VecD_HFg_mLFKiCIxg9neAaUqxna2H3_uevThIZyrZwX69G1S1bufkwbb-Ly5OWdp0DPZIKEI0n2yxW2gDhYW8jtcY4lWemYSTHEDNQKYtaDQswlbLO9MUMEodQF3WITeIzSjclTwuKPOgmIZ3oybOcl99rfUF0vng6t1Tv2alpHyjabTl0apqEpG0Y04CpXJG-aMKV7eXE4yWhN23mHTwqAGImQ0MdGiSc4aUlq_nXG1cyF96yAiN0HKXp5nVm92_PD5YfvtVRqRvZlJWuk86IwamomRHauUry0t9BuX=w341-h475-s-no?authuser=0")
       st.image("https://lh3.googleusercontent.com/p09MJ6OgA0mqj8MbYzvEJ48rwO3U4j47FyHgSih7xiyo8EtHQMXGJ5PpCd2U6iUY504wVz0NgZvX1lxgg99nTToCBoEI1j3Etsw4NFOKZXiVQoId1YVVoZjgEGUE88FKu90dREtqIKIJGQqmS3BNoKlBpdRnQu4JbOOxKgWUjy32iQd9vBb_P_qeOBjhZli5OY8DTq1oh_UVt6D4Sa8um-71plHXe_mQkSD-tHq6OckTA3C3DZzNGTJpY8p96AJA97W5PYnSZr6VfxK7kNYc81fzQHzaop1DwL54vYauQeNe5zj8i7biUlbCZFE37h4Lt2EIrZyDBFf1uaAsO2LhiLqyhx5GbXkQ4sk_paq74IVsga5yoNPLfrHENzYgwHEHanCInz-jV2Nf5otskEjjU21rA5vkaxw2CBfGM2X3x0PDQCYiJhBhiMPrM8yoLFQdbzHAz1iV3mV4jGkFHGZ24onW5kArmhfB-G90mgViWaUI-3GXXW1lN20gMkY-upCPKDuKWCI1koFFIHF2N8howm9W9XgnNWKnHTn2oOJm9DuF4Ey7tfrB0QlQvOG09y2G7_VuyRrtl-aTdaDZ1UrG0YIlGZ1zoiss6q3iLKXw6t5CAhpSX7FrWwcuv3z4u8BE4ItN6w4lgYk8x5MOYLDaDR3jroQoY8QqwUs_NVE_TuBS9PlHjtFTw1XTiMHOm_Jm3RiUkKBRy2EzBaqJzArqLG6OOWhzJld1amRc34GWjejTwRorefFEF0YHTPC88jYzM_G0Wfx0lMJwSPZCtktz1Dr6xEvkkHXFz3gbiF6sKMIOo1PJ77eAegbsMcIijSl0mPIN20X3ZdjqfjKmeirjHCwDubBdbjoNmSi0vm0Z53qfvX1ianb4uKKOu5Ij14JOTZ2QrXXumz0Z2jqRWBqduk4Yna_rWVVq4cfQ2yU5U-p0=w538-h485-s-no?authuser=0")
       st.write(
           """
           **Pemilihan Indikator**
           
• Indikator asam – basa adalah zat yang dapat berubah warna apabila pH lingkungannya berubah
• Warna dalam keadaan asam dinamakan warna asam
• Warna yang ditunjukkan dalam keadaan basa dinamakan warna basa
""")
       st.write(
            """
    **Jenis indikator asam-basa**
   
   """)
       st.image("https://lh3.googleusercontent.com/3KYn70iT0UprJOs6uoqUjmnTdyi-svgpMpAB6bONduJgIEd51vAhX12p0E_mw0PlldqH01LFKLvpofmpWHiu2E64-BdjcH9E_sNcahN-s-gw_zQ8-PpsKKNU9TpNP--oAnzfOyv2TjZfWfsdEiwcDAB0DCCg__BYv9UB3zt6HwU5BdsVaXsyQT67NgTFlDfWPb53yPNYZOogKP9p3VvN5lJTkYczOYHeBqRto1HTqcZbYjrD2TA7LOJmuyIG9lbWRJA9LoFAxrP_6or_wIEhvAJDSh9yRGiEGt6nCEuBu0GVeVT2PU2elIUeRREbYCx51AmZABnFjffUWIeHl8HRDXK8a6qhYKo44FxEiyF-FYDGdBeIN0gm-456KXfMscbgYOyGv6RJQaDH8l6WCzlZj3tUFkMAPgvI_HQTDaCidm5SUx2_QKkGtEbl7Q1Whpl0js0H_iThIsYwncA_7fCCjlYMVFgbSyAomsQo0Af92cKqrGJ6mLjqsG1KZOPEkrlmCXW3-YS5h-PMk5xc8p1rfE6aQAnQVudUnEN_0YtP2pVJiZzSaCONxV9p-IoT76WcmWSoS97ygAn2p1OOUv_irhDLZq4TOqNkqzt91ySxXxbsiwjgPExFWoNsNfjiD5VXd6AFTM7XBjIztTDreSpPAnYJzQ8E3V4kYq-YMvl5piXrmrUsw6yFc6Sa75nfmQLq9Dgm3HN5OLPVCKt4L62UMBalT8Th47b-WswHm4jB6G9RqTawQl2NafqlyzvlxlGc62GA1zACuww4lzyQ-6xu03Wg7dGnEXrCKpOhFASurib2PzrotjnGa98t-afQvKzPy4WmJ-roPIBKT7QrMnBhtfWY1umbcQnXVJuwbW-ftJp4n73qt4wv4PkjAl4fsMpIMHG_c-ZXhNACzZ1nHeaYjk0TRnUA1ZULeGV9oHb3oesO=w877-h432-s-no?authuser=0")
       st.write(
          """
            **Indikator asam-basa berubah warna bila pH lingkungannya berubah**
            
• Indikator asam-basa ialah asam organik lemah, jadi dalam larutan mengalami kesetimbangan pengionan.
• Molekul-molekul indikator tersebut mempunyai warna yang berbeda dengan ion-ionnya
• Letak trayek pH pada pH tinggi, atau rendah atau ditengah, tergantung dari nilai ka, kb indicator

    HIn     ⇌     H+ + In-
(warna A)        (warna B)

**Suatu indicator pH digunakan untuk menunjukkan titik akhir**

1. Indicator harus berubah warna tepat pada saat titran menjadi ekivalen dengan titrat agar tidak terjadi kesalahan titrasi. Untuk mengatasinya trayek indicator harus mencakup pH larutan pada titik ekivalen
2. Perubahan warna itu harus terjadi dengan mendadak(jelas). Untuk mengatasinya trayekindicator harus memotong bagian yang curam dari kurva

**Titik ekuivalen**

• Titrasi asam kuat oleh basa kuat , pH titik ekuivalen = 7
• Titrasi asam lemah oleh basa kuat, pH titik ekuivalen ± 9
• Titrasi basa kuat oleh asam kuat, pH titik ekuivalen = 7
• Titrasi basa lemah oleh asam kuat, pH titik ekuivalen ± 5
• Makin besar daerah curam kurva ( makin panjang daerah yang curam), makin leluasa pemilihan indicator. Bentuk kurva dan panjang bagian yang curam tergantung pada:           
  •Kesempurnaan reaksi 
  • Konsentrasi titran dan titrat
  
**pH larutan**

pH = -log [H+]
pOH = -log [OH-]
pH + pOH = 14
""")
       st.image("https://lh3.googleusercontent.com/2ThiusA4t_vN-0XPenr5f-eSV8tkjU9k7_cg_tYaOaiABWaSL59QqowZ1fd6yaD0dW7n4fuWw-6XYk8nZYBygI8OTglffLGRziT73w3Q4SxQ_w7VyjvxbvVTcvtBU5PWLeaFJbrrNrBUmfvXLWkufpijwI_VONjmPUEsvcVOeRwG1V6EOssce5YJStTQfbbXlkea1wxFhqNt79-ABf2fbqMM4KpoMJdhYNy0-ED6n26ug7k2G6fUwliO-5P6vYPBensnJFjd5W9Xbb2V0XnDJi8i556acZ6sVdUrjFVkRJ0U_LjM5oImnXZ726_SxjijzpEqSOilY1oUyNLLXBPMlsDwIUAsuyejuImEGR3uChF9U-w2uJ-lnZi1cZ_dw3fH-z1uNvvwqFrLOvxPzc5_rzg-DQjQT-uOptcfGi2CUO63FE4V5nc5ORFz4tqFqEO5fWvMVRsmp7GZMVTMiLuziG-ISGXiglKPh80YBodEzNpBiC-25KmPDwWMs03saxzzUO9YfO3BBxp7kOlnFSrAsP45RPhHM3SX7nt_387Dq6Ui2CG-a0VV8ZwIvniUwU60Gblys7yrNrX2sslaSQZd-7ly3pMrO1X123TDKvYF7QyrAXgJB1GNFLMWRUgF-BaEhGJdMtSGWatYqaP95QiPtS0pfjlYHqUr0I5bW65OrPWETNXpqhTCMmajrDqtHg3xnWJQve6Vcz89J-b0Lq4LRqeVG_DRSTaYB0nM89NQVsEs1AY5PUuBzKsVWbu72iMYmPzB40FkdLIYppd5v1v9vw2jtvb_nwdrnqXOUMpMViJzG-BjIa0w6m0yOFEFP9kdFLTy2T6GKKxeEYDZUVPgamqG4RMQ2YD6GTFsU2bVLDt212CQHyLFOFMSxXUpHzvgOMAtlY3XNH73f1v90ukvziIkLjy_OtujhuCv4ragojqd=w917-h663-s-no?authuser=0")

       st.image("https://lh3.googleusercontent.com/zyJs4mOlXN7SbmdqojzdQvn7W08FgW2NRCSLg8Ag3J1k-M5_6MdM0NKtl2cUSLjFV12C3Yq9Fr0UrjJy_W00pvPpN3a4SLJSL2N8jmyaseIu8o97hv6lwZ4T0apKQyrDYoTHuZ7HiPoTcix3dK2xrai3JMfAbSFZSL9iT9oqMABXhCZQU1BNyhM4Y4IKHZjJIld7vgKCN_7HKvy8TCaEUSB7Uq4oTQChApRSrWUGVDqUZgsfBzSP0XOhA75mquHfHdwR4pz8n1u-CPYWgVAtE8PExHE1UB-exOSHxHH-dRY58iYTdKzHdMrYWzuxe1N9_WlKGRUAroNKd5H1tv7mAuQcrrIMUmOBK8cha_bn5ZEIEVolEbb_pqcO-1L0V_LEP7vvnv-v9TKCBtXgeb4ge2INw6L-V3oB_YFPtCCgpuhJmUiuwFECRjV3bv_LZFgvbH9MvgIQTHM_B-Qn8xpxrEF5a38c0NvBvEa2b992piz7P09Cus99kzYiN7-t4k1QkmKJEMm2H2dckKzbLOQnJq2jTY9HCt5_Noh1rKRwX9uTKFiJHJOstatyXPjZVf6tDc6z2n6buLze4MjUwbiqgdPnZDqtT2tVST8n4NKQudIIwI2eLpvTkJcGwVBBZ-DRGHX2wMC8K00bTMpPJLjFgIy4VKsQLdxf9Ua4dvGCKnr9Mg_jHodRjW-1Z_Z5TIBvfDUJswvonFcRDIlwiNn7xCuiud4DTMQrxCxW1cN3pnH3Jo_L0UgV9ITAN4MNCTsDdnCWgS7NsxbmIgx9cHI3__H0IdDqD7Gkicy58Qnf9tFjOzuUuMvZtz6CowBPqcvZbq4ue48W5GkoWiBzLsY96gPhKCJGhS3dLf1Iu6euQlVzbefeWSvOwgLY__c643RCk-ptyfOxDj_1ICl-iLDE1Uwd3APkQ72A-6dwKTna6YlK=w848-h648-s-no?authuser=0")
                        
       st.image("https://lh3.googleusercontent.com/qkfbTinTZvmh0YM9bRpp2tjkoRpjNfZb8TOX7txvIFbLBHN2vuB1Ihr5ovHTSplJRzwuxIxlS-bJxq5nySQb2Dj4EJwhp1PmipQLNybRBe3sNaHOwvgQrXttJKi1saommTyI_Uaw9ppIhMdAqCHqK_jhfFTrs4mdqZ5oE72E5VkZOS_BAn-0NjZpGkitOfogNNiXJN4FPj_RCVw-V9vm9oZo7P9zX2O_9w9fBcrR8TWCbZxIStAuS0tNYyVpSuiFKXASPCoRxyR7Xz9YXZLq1eWvWeDowoi9LkyIG_GSpCuSKz2g4qKRJ5KzWRsS8LVqyMwz2_VH2ybmfQvPVEC9gTid8r5iexD0F8ht0rGAPaA8sVCqZ2qXqWv3ej8NkOztLibmFNn699eTH2P6-yoF1vpEeTl0wdAjlqPiVPy2bsKY9c58FQOVPd4ydQYm45mjbYZds-Wkzebti6SVQ3Hrutc51e3527obg6F3oaYhgwZhBJfXiLRNvBTPBOCPJHr4eYeVZNt9rwi53eCO5Qw-dRAu7dklC0iempicbCcgGAvTBDx0ootwbA986uKWXGzLCZLjJMgh_pOhLPOLQozIPvY3CT4BHye5QVI3V9ZBGbmabP5NNJ1NRMSdN0j4wqi2kANRwDJwYCZF3af09PmIydo0cC9ZokaIkDMA03xwGWQoWVEZ8CbICR-942M7if-bUCpndYwxM2h8OESbedWP1ck2KfHCNRp4cNVqGISGbE_xTV040M3gzavApmGI5MRs_lxCE7qV6OZhbn_fzz46abTzZQ5hg3rMaIJMTKXKnW4xpsrx0l0FYkP-mNth36mlDP_HTqrXZBHW3lN2OpFQAxmMbpSD1Vt45bLr5_A_hAptuOpvnsoP-mx8HekOr3JSoHMmtMg4eb3GMl8W_a-6arlolCJY_UxQipm7wbWyF-QR=w803-h577-s-no?authuser=0")
        
       st.image("https://lh3.googleusercontent.com/BuEzRl2oRFpiJILdxy_neSAwZZEHF-A7p-WWqy_t6X7ORGnrJHxEIPIElrj7N_T8AFFEia5qj_d8tEvnwqdRKAyE_xrFPkD6AAAY09NbAMuaFfzzKHQZXTnhczevU3obkHRTkSyg8Lcv4S6-tMjXV0oklpjllTwZOBvw740LFxeuC70Tt2hAzFu83j10EG6vqg6K95dFQMT_4MrCIqYSI13u5-cVlOSJnmJi_w6F2giyZCXuX76l-mzw063UXzs6s0fk6qIZWZ0AFJxLvhS9Gbtw06y68zrJXId-kNvqhkDbD_kZnZ4oQw04EjUqDPxPeXa8tRlqGny2L-Y5harEB1tQBK7eA19BuvN61NOUHZI2UaMTWkpa21Zg82JYDwY6XxuXME3kukf4KRE4oTEJoTwjZuKUf2n556QMB4kzTN4cFLbPudbtn1f7S2AFFteE4-2AJiZIQQsvqeeY0emPX7eIj6kT1EPD7VLnifAtBvnCavLguqYeR7cviHWAp0JY6mWAUFWR1Wvap7RnAiysh8nQ4fMuUiJ4IMzJ1lXB8QZAZKzBi2H3GAGRJ7BxI9dxQD4TJyRYbj2fA6gcqc4Uaoxpa79Ds9eQ4S5QcRyUF9Ba4R2odabveJVCSUVYz8yzJam7gW7giabSiUNAgji8XL-7jBIcqpgNEdEdCk_XHB34YndWUyZ5lMk3Sb7VWcQwLW8Yd3OAqnpARHZuFnssxuthBoSeQ-z3Kun39sgvWKDsnOD0X0hO8WBSWbFUFtyy0LFLaS79ZNzOjSt3jWytIObH-oClDdzwSt6HPmkLd37xTIouQVePjPhBJGO9KbSt0VLdBJaTB8vMzREoNAKSxxBEV5C2oK_O86jYbAjDzU81rpcValxfl6QaecsbpnwsFsb7lp9M1SHIugJxD1fVzM2tZFw4VY3Q7rAKmA9NT13v=w901-h760-s-no?authuser=0")
       st.image("https://lh3.googleusercontent.com/4uyA5mwYNBjFgRFo59Owz7HlW-p8n6aik9QZjGtRFD9VzQCnhA8kqiLGjqvGwF4HgmWQdrukQiKgQWdV2287tAaZzr0EBJNAgEDUKLRMvyomRaiNpGtyq_vbi-MH8jOWYm20s4NkHZJcYAPasbET_LPtGm9_0NqLkoInd2QQp_AcTZp7it1aHaIsOnDbO4qBHdS3D598DUdyEN0nVLDIxjPKuUIQXOQNmwPdt7bxi_kNNLb0rvyIyKVC2HaihSNMGlN_KbSMn6vjx3IDLlUyTjZ3712KdECFxc0BAFPs2NIizaew6LGAxg0xs6q52S7LY2N8Q4M9UNSy38qKdO1fZeSeGGlgrdpnLq3nAC7r9r9EXRWqVYzVii90R44kgc3pavfOY09R9Rjvr2hfN89O5iBCqrDZv7rhXEZl0VIal20cys79cL4vC8HbNar4_E3FWpjScJIigkuzv7cc9AZ8HL_wGkq5sx-hb5rzZfRrqGm1R9q2FglORvC0BZg-08imhPTHbbj0e_8tc0CWaoQzPaZFdySFpax52EJIBoFq5RKugJ0EoDqg3uzYOimoeyu9G74JnCzWUaBtyqnrrHpBpwYaKnZtojyB-1D-YQJkusoprCYz1a5JUdDsv0k27UeQlvZcwmtO_FPL6pKzUs-naBkK42zdkA3QoMsxRp8WKEtp-7H1TBAolXhrn04fUae9sCI7sglb-TqxxHtLO9hbqF_37Gy7fnpMuNq11dPr4gokrETbA2KNAqKSjOJy9AJAtnpim6Gf_DqU2bBn8u13FPZK66sYULQ6_IxvjyF-do0ZWVQ3U0AQUFkVrg4apRL1O6Pqn_cj6wCkTdDjqqde4W9NDprj6gf7QmkVt_zPpM0cb_eAusH9DYsUQlQtMBI478zLpRwRYtuOtAdhDtB3yFDhnJsbuWiTTUkBgCdErYOK=w1124-h793-s-no?authuser=0")
        
    if optiontitri == "Asidimetri":
       st.markdown("<h2 style='text-align: center; color: raisin black;'>Asidimetri</h2>", unsafe_allow_html=True)
       st.write(
          """
              **Bahan baku primer standarisasi asam (HCl)**
Borax atau natrium tetraborat dekahidrat

Na2B4O7.10 H2O ( BM =381,4 BE = BM/2)

Na2B4O7 + 5H2O   →   2NaH2BO3 + 2H3BO3
2NaH2BO3 + 2HCl   →  2NaCl + 2H3BO3
Na2B4O7 + 5H2O + 2HCl   →   2NaCl + 4H3BO3

Natrium karbonat ( Na2CO3) ( BM = 105,96)

Na2CO3 + HCl   →    NaHCO3 + NaCl
NaHCO3 + HCl   →   NaCl + H2O + CO2

**Standardisasi HCl 0,1 N dengan Bahan Baku Primer Boraks**

Ditimbang teliti  ± 1500 mg boraks dengan kaca arloji, larutkan ke dalam labu takar 100 mL dan tepatkan sampai tanda garis, lalu homogenkan. Larutan dipipet sebanyak 25 mL ke dalam Erlenmeyer, tambahkan 2 tetes indikator MM kemudian dititar dengan larutan HCl 0,1 N sampai larutan berubah warna menjadi merah
""")
       st.image("https://lh3.googleusercontent.com/F_wgX_wVZXH9a5TPRmPwLDoq_Mj7g86tqwlQK3xj0eyaSZO2nrjQKlUTIRBbqckvKN3QtNd4UyOAnCdz8_Malms4PJWO7ad9wyX6HUopRJVNKeqviw69TJll3IyZ5II1k39OReAcMGwqtEf--IDw0_GIjlWWQxEqNrJe-DkEE-K6Tvd4E-3jYCI_Ohv0heu-7p7jT1VI7mTL88ue8nzcxbhExytBVwWWb28dZkchf28POwqz4EVdtPwKuvueP71Ay7lsZaF79wKuvowZIJj7Jl_tZdWzqsu0KxgIPKFkL8VndAb9HSQ-I7FAPbwHdKPXXnxqTMsRnzlEo_c50U2Z2jTNEJzmmaP3k2ojNwQKxm-atGCqVaupbJNZphPPlTluAJbn_05jshwkkYT01Mu137_9LmGES7MJJ3U6KMgrYCCqrbKuln698y2vr76JHhXwnQkf1dIoqqUkhPX5zEXT4sJn9yx85RDv0-E3CmrVxGD0H4WAMcMMgnygf2R6yQwg2X7vclNQ04BZhnjsRlvfe6zrE_dr8K-cnCl7r5WJzKJOvxt0FIdC76XGTZ2lnVdjC5WK745sag_tKc80P0TTPzyxnaSfw0unwY5QsM4-0FGaPKd-6h2adWYomF_lbMooS6hRF6aWLvnSrYq5fkb87N7EUqgwGh0vT6Ray0c6xLFXTuKL2NZHUfNG1xGRTgjHgao07Tc3U4eXhkVXRFnvPEuv0Hb7LvA1zcxCZQBi7SHGnfEBtn153TtS73nNUL7WCt7pKKc5qDuEQ-q8H7qdgYIVMDOXWTc72-yiLb36bJSWszTZ7rdbIlkTHExB9BFp1fxbsWrIkn4Ypk5jNfynQO4jSXdF63pLY4AoBGlfY7SbPSmnD9F82i2yz11bkIcaTurhodzgZnWi0I-y5gBkqTcURPa3EQCHzkhY_JyuuEFn=w1016-h159-no?authuser=0")
       st.write(
           """
           **Penetapan Kadar NaOH dan Na2CO3 dalam Campuran Secara (WARDER)**
           
Na2CO3 dan NaOH dalam sampel campuran dapat ditentukan kadar

masing-masing dengan titrasi asam-basa menggunakan larutan standar

HCl dengan 2 indikator (pp dan SM).
Tahap 1: Digunakan indikator pp, HCl akan bereaksi terlebih dahulu dengan natrium hidroksida, dilanjutkan dengan reaksi ion karbonat menjadi hidrogen karbonat (bikarbonat).
Tahap 2: Ditambahkan indikator SM, HCl bereaksi dengan ion hidrogen karbonat (bikarbonat)

**Prosedur**

Dipipet 25 mL contoh ke dalam Erlenmeyer ditambahkan dengan sedikit air suling, dibubuhi 2-3 tetes PP, lalu dititar dengan HCl 0,1 N sehingga tercapai titik akhir hilangnya warna merah muda. Banyaknya HCl yang dipakai dicatat, misalnya a mL. Larutan dibubuhi 2-3 tetes indikator SM, titar dengan HCl sampai titik akhir dari buret tadi tanpa buret dinolkan lagi. Panaskan hingga hampir mendidih (jika warna larutan berubah warna maka dititar lagi dengan HCl). Catat mL HCl yang dipakai, misalnya b mL.
Reaksi  
               PP
1). NaOH + HCl  →  NaCl + H2O                             
                PP
2). Na2CO3 + HCl →  NaHCO3 + NaCl
                SM
    NaHCO3 + HCl →  NaCl + CO2 + H2O 
    """)
       st.image("https://lh3.googleusercontent.com/jZlm4_Vl3jQZGlhrFfxq8Ml_n5qvvxdHowWGUkDaJolpzkBn_M9L9Wb3ha_6QvotZJSZW1Txw0kTarow4J3OcYthdqBDLdYcI-whpHK_Bgpe4VImGclj_CqEu_E61y3rAjlPQfbNaVUEiGlR-TfT1EoAefk0clvFxwZHke7yGmzNk71z9VUXXE9xIshgf12h0QCK9QMSfnSXf91acWxkQCXTjP-H4fdT_A6v3oiJQLjb8Dl5oEO6kE-HuhRbklD4B-aPKo68blMcHULJ549oDua9h3YiwksS0lHZ4_njy6w7cVNHM-1Wh0fWHQ-v3svXuG7RyGsw-AsHcoFoMq23VuNHMdenI_uyRQ3Xb3B_zDS-JhP4LQr1LdTKlFXL1G5N4Gja_3MKEgzu9kilNR-kanmzya5EylU2Q7K5o2wQkguaKeVxudD9TkYGCKoY_kUFqCI5uuGjaM31hxVD9bpksi8EQnYbho-seHTAvzpC47oJPkG4wX3W47tp0GDCMpigWRILEjM8lmJYUGm1iV9I8ZD2npIxeC6c63jlvkFDQaUwL_RyD1pvga_o3JVisdvIb29MIl6vhk0K1NoZxHh9jhWC8RCzFQa8ybLMEiGJFPTn8aYOqOtF16uVI0JN2aga5Zz3VuYrtebSKlmhc7xSxV1nCKWfi5V-YF2p7QJU0wp1RiKPsTIeENtIgm6e3Z_OM7wBjyMcTWbIpU2CnVNXetKdKekLli9vUSIMyfJZrKxXDh3IkCz9fZtesRoXKmzqFhWL4dilkqjAqtSbw7wRqzZfmq-Qwtk3_RG2I61byedliLJ7E09jgannuZtKh-FuDiwbn4vYechq6hYxVeynCmdqW0KWDTEAfIbm333D8CKulsHd15ZWsqkfv3RMWTkb5ouDEaEOf8m9hF199La2kPglSy2WhC0FCg-sc3eZjn_m=w621-h327-no?authuser=0")
       st.image("https://lh3.googleusercontent.com/EFMWwPFLq06PkqgoBJJzPyPYoYoM8fRbUooUzJ6s9ori_OUrP-XE5m8ZCulwY_Hbj477DafL2im1o7gjjUeRi8CeuqJesTtU0xjGO91znRsNHsFW-Q1CqQYpNNdeC_4lMpGLKFIw532-s2eDgGofpASIeUU9ljP8BfNFpUm399P_VN2vQiLs_I9oEhX8UQCEabqDlVgYmtEomMV6PCkh-lyQJk2r-s1UXVnQnYC3kfTHXtkzIHuw_5S2pnx1LxUmxBInXF0WpwCC1trR-_oPrl7CpCACVeNCNa85rj9G6SrRb9zft-pU6lT2R2Tw0-ugdWmD9YKzijxiAITw7OIOYHYHVpzOVWUqU1NwWZZlg2O_cSS6h3HBggLm3wfbDgybLjnO-CN0kCs3a4MpAQ8UyjyfXFyt5Xk1DiYcF5jSjxPmerMvLfEBTwetU1PGwJUFEJrntTHi1zuCkgCPBg9-wGDd4OxtjrRX-XBEv54hQIz0YNCn2WAYyyAPn8l06qAPveo07NhuqgSfXOPBdbPVpfINTjbSU6xhk9cwMpNIybM0ew2TCyTP__6rR8GPU0tyomW-xYyhtH6oTCQxyyBDgbBP5ppHoJEY-qBy01-q6YHcFy_q1Uw1S9wLqQ9sVhx1qACYFlBvkxcNoW0EVq_bS2Auilp_yiLA0g8LpX_UksFNkDAfruHNQwfmDifXLTfnfbmonBs8D3FiiheWg0lp8UyGm8MTOHJ3fZ5fNky09vvbzzF1FkvEbOq3vjjoObnpmG9hEkUlphflq2Ew8SGxWcP3xttVclkMOE2zUmEL9o2Sjn6jXIShs3veGpvlpaEYyd0xkJ55pVyhtZ0Zo_aSCWgsJ_xnwVbmcg6l6_bQ95ZYuxrl6tMoAiR7_RfxIc646KtPjl_Nkl3YcxhJ2hNS3AF0tLubM3qIni7EEtKAggQM=w622-h336-no?authuser=0")
       st.write("**Kadar Na2CO3 dan NaOH**")
       st.image("https://lh3.googleusercontent.com/XzvRNeFjeok64TqT8XJCCM5uKX8pA6Ptd_e-oONrCdK7sLqKgVdOlml8J-NQqb41An82MuBrarbng2BgKcZf8uMdhIn9Zgefa_Ay-1x4oXR6xrFdnBIMRYODGysEEgiWKsFNQ6OEOEkQKGBZZLECxKHW3g_jS97n4UUbD5ADPMJ0FPInl0sfSGYHiu1LMkg-ThnILmb6le7GBKdKPiIR1n6RWDpkE15a2HKz3lZATZ0xgWbH2kzSbS9Z6AiqoMLu2VkkY-sSqu_X1iYUwqRLNy07SzvNa6PfIttk0vbOiSirmcwLrldtFGx0dOulp1ZYUIO_AULu2EK0_-k_0fsUFDO1qQqXfZqbsok7qEUbQdH-fhoxnQNmYaWv4_vKwB04QNlmfYGy2cQkOO8Xlb5Qtc9KhBODdXmTHfpc-TsW9F4o_oww-J1K_HdjtA5zgBtamqY1o07GMXkb5TtBn9XaUr0CMctZBunyF6H3JbO_ALp79pGgbT2ZnyVo5CQlNKhV0aMgaUbsSskcb3NFI-BxXD9zSBZfvrTj1zWWJoEhqzaB3AKUPZ_EfSa8BPhk3MoKpGYMTFx3bU_OM_s0OhIOjCyFKsD8MJ9Yo9VefiP9OhWGWfDCntM2mZ68Vmb4AC47UP-fsSUe_rK-dKbXNcxhf5QB4zsm_hHofzlZrBsKZbv524UwMl73GOuVKV0_UN44ocMojzmcWw-RyQ15VxWC6owmA7YuCwNQB9eNC13htaqbTkkj006CBQcL25QfN9YYLdRD68Hz_sP-vgOdiR6LQNSvA1o06-sZDrLR6iexLsqcbV0jXPw9iNk062kM2jOj72difjPcR3Omle2mL-x_KSWlSWOW4cfAP4MLVeVfqbf040YWUkuSgQzF_6kOez6ZDhSwkLpuVAhaR56hIg9LS0i-l3MoRlATE_uccw0jCEHv=w607-h327-no?authuser=0")
    
    if optiontitri == "Alkalimetri":
       st.markdown("<h2 style='text-align: center; color: raisin black;'>Alkalimetri</h2>", unsafe_allow_html=True)
       st.write(
         """
           **Larutan standar (larutan baku)**
Larutan standar adalah larutan yang digunakan sebagai titran yang konsentrasinya di ketahui secara pasti
           
**Larutan standar terdiri dari**
Larutan standar primer adalah larutan yang konsentrasinya harus diketahui dengan teliti dengan cara penimbangan zat yang dilarutkan dalam volume tertentu.

**Syarat-syarat larutan standar primer**
1. Zat harus mudah diperoleh, murni, mudah dikeringkan
2. Zat tak berubah selama penimbangan, stabil, tidak higroskopis
3. Mudah diperiksa kemurniannya
4. Mudah larut
5. Reaksi dengan larutan standar harus stoikiometri dan cepat

**Larutan standar sekunder**
larutan yang dapat digunakan untuk standarisasi atau menentukan kadar zat lain dan konsentrasinya sudah distandarisasi dengan suatu standar primer
Standardisasi ialah suatu usaha menentukan konsentrasi yang tepat dari larutan baku yang akan digunakan untuk titrasi.

**Standarisasi NaOH**

Ditimbang teliti  ± 630 mg asam oksalat dengan kaca arloji, larutkan ke dalam labu takar 100 mL dan tepatkan sampai tanda garis, lalu homogenkan. Larutan dipipet sebanyak 25 mL ke dalam Erlenmeyer, tambahkan 2 tetes indikator PP kemudian dititar dengan larutan NaOH 0,1 N sampai larutan berubah warna menjadi merah muda
""")
       st.image("https://lh3.googleusercontent.com/F_wgX_wVZXH9a5TPRmPwLDoq_Mj7g86tqwlQK3xj0eyaSZO2nrjQKlUTIRBbqckvKN3QtNd4UyOAnCdz8_Malms4PJWO7ad9wyX6HUopRJVNKeqviw69TJll3IyZ5II1k39OReAcMGwqtEf--IDw0_GIjlWWQxEqNrJe-DkEE-K6Tvd4E-3jYCI_Ohv0heu-7p7jT1VI7mTL88ue8nzcxbhExytBVwWWb28dZkchf28POwqz4EVdtPwKuvueP71Ay7lsZaF79wKuvowZIJj7Jl_tZdWzqsu0KxgIPKFkL8VndAb9HSQ-I7FAPbwHdKPXXnxqTMsRnzlEo_c50U2Z2jTNEJzmmaP3k2ojNwQKxm-atGCqVaupbJNZphPPlTluAJbn_05jshwkkYT01Mu137_9LmGES7MJJ3U6KMgrYCCqrbKuln698y2vr76JHhXwnQkf1dIoqqUkhPX5zEXT4sJn9yx85RDv0-E3CmrVxGD0H4WAMcMMgnygf2R6yQwg2X7vclNQ04BZhnjsRlvfe6zrE_dr8K-cnCl7r5WJzKJOvxt0FIdC76XGTZ2lnVdjC5WK745sag_tKc80P0TTPzyxnaSfw0unwY5QsM4-0FGaPKd-6h2adWYomF_lbMooS6hRF6aWLvnSrYq5fkb87N7EUqgwGh0vT6Ray0c6xLFXTuKL2NZHUfNG1xGRTgjHgao07Tc3U4eXhkVXRFnvPEuv0Hb7LvA1zcxCZQBi7SHGnfEBtn153TtS73nNUL7WCt7pKKc5qDuEQ-q8H7qdgYIVMDOXWTc72-yiLb36bJSWszTZ7rdbIlkTHExB9BFp1fxbsWrIkn4Ypk5jNfynQO4jSXdF63pLY4AoBGlfY7SbPSmnD9F82i2yz11bkIcaTurhodzgZnWi0I-y5gBkqTcURPa3EQCHzkhY_JyuuEFn=w1016-h159-s-no?authuser=0")
       st.write(
           """
           **Standarisasi NaOH secara langsung tanpa pelarutan secara kuantitatif**
           
Ditimbang teliti  ± 157,5 mg asam oksalat dan dimasukkan ke dalam Erlenmeyer kemudian ditambahkan air suling kira-kira 25 mL. Ke dalam larutan ditambahkan 2 tetes indikator PP kemudian dititar dengan larutan NaOH 0,1 N sampai larutan berubah warna menjadi merah muda
""")
       st.image("https://lh3.googleusercontent.com/NtJ4Bax7NDQxyzStGdlPZpGFHL43Abv_RyIKOovArBl_-VDghjXeZwOiN529ku8H3yvVFqlg4uF24JdNvXcukSPpfP0Ej2r15ebF6PpkIh0VNpTGYKhmYDnf-CU5zL4dCCBvyUsr0wZctD0ZFycGAR1Lplr34jBB16KVyCfVVYfHe3mvN2zH1uuloW0unpMubE1LrElyMM0zWud6RIX9gOfnzLWwq4eakpWkXDwDJwZlN8WfIhEp-ThunjdKBDHcmoncA2T9UwUr0s_wwTOexDCdkppk5-9-UVGb9PM5SZbkbUjPMXjScj8_S4YJYdX517PapAsSPxQIMHN2_7Ol96EL8iPgr4IrJNKMARuIek7O4GcsOzE8AnO1xtnmUjZ2KkIa8YDyoHpzgVAJaZDklMCMjveOciZyx1fM6Nld2DXtWnFxdHQgI4Q2gapyt_W4aNaXwOHKTMh8GfZQmy7XC282PPGw5KTmGY85xk49Zagm-WmFI6jbBBRlRViQFlJ96k2zDzCEonX_F1t-VqnlBUyLeYgkWKHTdoCR3r68f38kyT3vBno-W7fZSuJTeE_ZOgzNIGiRocG6pb1MwK8Mwkb_1V2Xn8iuuy8ShD0QElPZ3TLtTJ8q5UkCWSpEUSXqRsQ1y2hyJInWTONI7F5IDZ2plE7Jgp0v68Kq8BEm2PYG0VCEBWKvRt8lwjUfboYkS_DJdJP3sKgHrL9wuanK8NpwYxs-W9NuLn2hDprjqnlHOrJt0137TLuvkX4gadjo0N0cnqz0oy6FVhWZHSbOfMQvhSrnaB0D92ep_6Gd708KzQFvCW-drecWb6C8d_We2p3wlqi68ByY8Si5swoh2OzHK50BmKyic-0HGXYCOh7SI8YDm8rJtLcg74iX09lzupXB12vq-F4zKidO01oxCnkPnQnviS5rToHuL1jy1juR=w807-h160-s-no?authuser=0")
       st.write(
           """
           **Penetapan kadar asam asetat dalam cuka makan**
           
Dipipet 5 mL contoh cuka makan ke dalam labu takar 250 mL kemudian ditepatkan dengan air suling sampai tanda tera. Dipipet 25 mL larutan tersebut ke dalam Erlenmeyer. Tambahkan 2 sampai 3 tetes indikator PP lalu dititar dengan NaOH 0,1 N (yang sudah distandarisasi).

Menghitung kadar analit:
""")
       st.image("https://lh3.googleusercontent.com/meZ72KJURC2zTpaN6jog1UN6nd4E5aGdLuyYvIXcQ33misUKM6UI4grmgSQ67V7Xwnx98Hlk6wCMAil0ijIIGYHr3kgNKv0K9jDwf7TPn-nGUBQMN9s2fKp60mSB4Ie8dGHudkEXMgm3ET62GXHdbvMDIKIT9JmWKKg-0BDD5TC14VIfDlrxFQnBLor70Ua-WSCWhWD7uQBN5Ft4ToJdEPrP6AWH3DEqgKpTos3G05BuEwxK6hQfby4-IJq-Y3oeV6exjP0uzlTExrAqTLPsdVk4oqpexBwjd-DEO-MNm-hCefzazkM-MYkM4-co-7UC5edP9VWo0aphF6Drx1-5Hq4-Brpj6KieAglQ_yvrtWBOLsjUMXT7S2uQ5IGVCyb_4xtrt_lWM-X4NNno9Mrsivs9Bugs-HujJf5WvY0lCGc3hoaOjpUkkLZJw0Ml678SBvi8O0jgqoJBUdRdrKV7yYjNzOSmIC7XZ9JvkIS554cpE6RPVw-n_v-VmLMHB37ECjxEwSTMjIPWJFfBx1j7AswX2KRf2oLW2m9pAgRm7RCSJiZUdPR0NuzKf2NFwaURjmSWlqPUoIyzxxRy5UnHcRkl_kuwyqBGSK5Ncm-W7mP4zZCCBzTLhr050aP3s72-Rb0aurFCoB6YR1ji_Lg4QQ9os-sLET0vetlFxgLkp_v-Qsj-YzLGxALqFglOl0YGcIjqNrGKEExF6AA-E4kp6myvGpE4cdizTqBsa6kuJgeMO5lrSVozhr8Gadjj2YhzQU-eDvYlPuk7kFyrhdCbgThlGyWbfqAiaZbL4ZjWHgNsjzJ5Gom-lthYqsI_lg5iMtcRnSTtdcGI3v9bQUtQ3cJK1-GJhB_tRjg600zNw_ZodDyJUnE-EmtJvhilOGCr1ndi-3qTRzfWTWpBlos33Gcvv8hXO6leUZ4CaSFhhX-5=w1121-h436-s-no?authuser=0")
       st.image("https://lh3.googleusercontent.com/jf-34ekEXapqqXyO-DHYULhpUV5tEpCBajOJoFmyTcIIWykGH8zpeVGGZwiy721p1c2J3WbPZ94krO-MpqdzwOP11PD8ldXrK8nlthYtE_zJ_h0hfwm08UHDRTNe75uoJLytlRdPXIqZSEzfKdv2Ym4nN2Snd-ohacyYlR5GTQUK5_mRQBF2kZfA0mBLqixAv5YNc8ZeFoOnfgwD-jxa39J172ZphkWlL_S3ToiYCbVR3uCOmV-ImhzdBVO0WL3ew8iRJhZlcr3y5bjRXSvyMt1bci4hw6zVjSDw9SGdSlTk-me5T-cytyDvz-htV4-8S4lWs1L8-ln45r0fcadL1lq8nv8Fgmc_nHvI5X5B8StmlhxwrXOQdvKS1X7sn0-NNdhHAAN38S-6R59qDicFqfXEtxY4XnlAOGnCRE_9x7DD-i_Mhr5hBOmj9z2MgJM8SMogeEKg_S43zT4KijZe7aybb4sd4eObD2yVsmC75nrK6yyB_1ZFe-vR3Mt0smly3F8FwWAcVS8YhKGqKok4uLom0E9dgLnPDGvRLY4NACbAJ0L1fJR7bcdanOmPuTdEJjhZX7D3kW222XFcjrDrErPjaZ4KWuIY-_Vzy6HPTzluONFDQQG6RKg34sRuAxN7SWlZUqCfJ9uO3rnUEEn9QrLxksI1bBe-WH9UXNwHSCT8KFCqPYEnMFqLGNZfpw2kj1Iq_XgxE6cFHgTCoL0uI0jANYCjH1mTj2u4BSsX_NeNpFTDeLKwh69dKGdq-oNjCXsRi4ijJSF4P_4zjOV3sFgRSaaQpfmvY383EaqOhQAHO1TWSkQ99O3hCa-70sXahvPyPk0Nk1MrFmoSwfmn_pkVBHawXFbM9q-z6sUf7sWpGl3qEfTVRNNPv7TURnZE7ZbsfnBTgmr9Z9TAAGcHV9k9tYDe5WmzVa7aEjEU5ROR=w1112-h362-s-no?authuser=0")


   

     
          

    

   
                                    
#Materi Kimia Organik
with tab_4:
    optionKO = st.selectbox(
            "Pilih materi yang kamu mau",
            ("--- Pilih Materi ---", "Pendahuluan", "Alkana dan Sikloalkana", "Alkena dan Alkuna", "Stereokimia", "Senyawa Aromatik", "Alkohol dan Fenol"))
    if optionKO == "Pendahuluan":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Pendahuluan</h2>", unsafe_allow_html=True)
        st.write(
            """
            Kimia organik adalah cabang ilmu pengetahuan mengenai kimia senyawa yang mengandung unsur karbon. Jika suatu senyawa tidak mengandung unsur karbon, maka dikatakan anorganik. Ada beberapa alasan mengapa karbon menjadi hal utama dalam kimia organik:
1.	Atom karbon dapat membentuk ikatan yang kuat dengan atom karbon lain untuk membentuk cincin dan rantai atom karbon
2.	Atom karbon juga bisa membentuk ikatan yang kuat dengan unsur-unsur seperti hidrogen, nitrogen, oksigen, dan belerang.

Karena dari sifat-sifat pembentuk ikatan ini, karbon dapat menjadi dasar keragaman senyawa yang sangat besar dan diperlukan untuk munculnya organisme hidup.


Kimia organik awalnya dikotakkan hanya mencakup senyawa-senyawa yang berasal dari makhluk hidup, tapi pandangan ini berubah karena banyaknya penelitian yang membuktikan bahwa senyawa-senyawa organik dapat terbentuk dari senyawa anorganik, contohnya adalah Friedrich Wohler yang berhasil membuat urea dari senyawa anorganik pada tahun 1828.

Selain itu, Alexander Oparin pada tahun 1924 juga menyatakan bahwa kehidupan di Bumi mungkin berkembang melalui evolusi bertahap dari molekul-molekul berbasis karbon dari senyawa -senyawa yang dianggap ada di Bumi prebiotik (masa sebelum ada makhluk hidup): metana, hidrogen, air, dan amonia. Ide ini diuji dengan percobaan yang dilakukan di University of Chicago pada tahun 1952 oleh Stanley Miller dan Harold Urey. Dalam publikasi mereka di tahun 1953, mereka menunjukkan ada lima asam amino (konstituen penting protein) terbentuk ketika percikan listrik melewati labu yang berisi campuran keempat senyawa ini. 
            """)
        st.markdown(
            """
            Daftar Pustaka: 
            
            SOLOMONS, T. W. G., C. B. FRYHLE, & S. A. SNYDER. 2008. _Organic Chemistry_. Edisi ke-12. John Wiley & Sons, Inc. Hoboken.
            """)
        st.write(" ")
        st.caption("Download Materi")
        st.write("Google Drive: [link](https://drive.google.com/file/d/1HkxDojpo7XzYukO5ALVDAE9_5FtR4nGB/view?usp=sharing)")
        
    if optionKO == "Alkana dan Sikloalkana":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Alkana</h2>", unsafe_allow_html=True)
        st.write(
            """
            Sebelum memasuki materi alkana, kita perlu mengetahui apa aitu hidrokarbon. Hidrokarbon adalah senyawa yang hanya mengandung atom karbon dan hidrogen. Alkana adalah hidrokarbon yang tidak memiliki ikatan rangkap pada atom karbonnya. Alkana tergolong hidrokarbon jenuh/tersaturasi dan merupakan hidrokarbon paling sederhana.
            Rumus umum: CnH2n+2

Aturan-aturan pemberian nama alkana bercabang menurut sistem IUPAC:
1.	Rantai atom karbon yang terpanjang dianggap sebagai nama senyawa induknya (rantai utama).
2.	Gugus-gugus yang terikat pada rantai utama disebut substituen dan setiap subtituen memiliki satu nama dan satu nomor (menunjukkan  nomor atom C yang mengikat substituen).
3.	Jika terdapat substituen, penomoran rantai utama dimulai dari ujung yang memberikan nomor cabang yang lebih rendah.
4.	Jika terdapat lebih dari satu subtituen yang sama, maka nomor masing-masing substituen harus dituliskan. Jumlah substituent ditunjukkan dengan awalan di-, tri-, tetra-, dan seterusnya.
5.	Penulisan cabang diurutkan berdasarkan abjad
            """)
        imageKO1 = Image.open('Resource/image/Kimor/Penamaan_alkana.png')
        st.image(imageKO1)
        st.write(
            """
            Dalam hidrokarbon, berdasarkan jumlah atom C yang terikat pada suatu atom C dibedakan menjadi 4:
1.	Atom C primer (1°)
2.	Atom C sekunder (2°)
3.	Atom C tersier (3°)
4.	Atom C kuartener (4°)
            """)
        imageKO2 = Image.open('Resource/image/Kimor/Atom_C.png')
        st.image(imageKO2)
        st.write(
            """
            Sifat Fisika Alkana:
1.	Merupakan senyawa nonpolar dan 
2.	gaya antarmolekulnya (van der Waals) adalah gaya London (gaya dipol sesaat-dipol induksian)
3.	Isomer alkana yang bercabang memiliki titik didih lebih rendah daripada isomer yang memiliki rantai lurus (tak bercabang).

Pembuatan Alkana:
1.	Reaksi aluminium karbida dengan air

        Al4C3 + 12H2O → 3CH4 + 4Al(OH)3

2.	Mereaksikan gas alkena dengan gas hidrogen (Adisi)

        C2H4 + H2 → C2H6
            """)
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Sikloalkana</h2>", unsafe_allow_html=True)
        st.write(
            """
            Sikloalkana adalah tipe alkana yang mempunyai satu atau lebih cincin atom karbon pada struktur kimia molekulnya.
            Rumus umum: CnH2n

Aturan-aturan pemberian nama sikloalkana bercabang menurut sistem IUPAC:
1.	Jika terdapat substituen, maka nama cabang disebutkan terlebih dahulu diikuti dengan nama sikloalkananya
2.	Jika terdapat lebih dari dua substituen, nomor pada cincin dimulai dari substituen yang memiliki urutan abjad pertama, dan arah penomorannya memberikan nomor terendah untuk substituen selanjutnya

            """)
        imageKO3 = Image.open('Resource/image/Kimor/Penamaan_sikloalkana.png')
        st.image(imageKO3)
        st.write("Pembuatan: Hidrogenasi Benzena")
        imageKO4 = Image.open('Resource/image/Kimor/Hidrogenasi_benzena.png')
        st.image(imageKO4, caption = "sumber: ruangguru.com")
        st.write(
            """
            Reaksi penting:
            1.	Oksidasi
            """)
        imageKO5 = Image.open('Resource/image/Kimor/Oksidasi_sikloalkana.png')
        st.image(imageKO5)
        st.write("2.	Halogenasi")
        imageKO6 = Image.open('Resource/image/Kimor/Halogenasi_sikloalkana.png')
        st.image(imageKO6)
        st.markdown(
            """
            Daftar Pustaka: 
            
            SOLOMONS, T. W. G., C. B. FRYHLE, & S. A. SNYDER. 2008. _Organic Chemistry_. Edisi ke-12. John Wiley & Sons, Inc. Hoboken.
            """)
        st.write(" ")
        st.caption("Download Materi")
        st.write("Google Drive: [link](https://drive.google.com/file/d/1eyxBoTTdDbhp84Ae_aRKHMt57B-5iyc1/view?usp=sharing)")
        
    if optionKO == "Alkena dan Alkuna":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Alkena</h2>", unsafe_allow_html=True)
        st.write(
            """
            Alkena adalah hidrokarbon tak jenuh dengan sebuah ikatan rangkap dua selang atom karbon. 
Rumus umum: CnH2n

Penamaan Alkena:

Mengikuti tatanama IUPAC, nama alkena diambil dari nama alkana dengan menggantikan imbuhan belakang -ana dengan -ena. sistem penomorannya mengikuti system penomoran alkana dengan catatan penomoran rantai karbon terpanjang dinamakan dari ujung yang terdekat dengan ikatan rangkap, sehingga atom karbon pada ikatan rangkap tersebut mempunyai nomor sekecil mungkin.

Sifat Fisik:

Sifat alkena tidak jauh berbeda dengan alkana. Namun, alkena mempunyai tingkat keasaman yang jauh lebih tinggi dibandingkan alkana dan wujud zatnya tergantung dari massa molekulnya.

Reaksi penting:
1.	Hidrasi

        CH2=CH2 + H2O + H+(katalis) → CH3–CH2OH

2.	Halogenasi

        CH2=CH2 + Cl2 → ClCH2–CH2Cl

Pembuatan:
1.	Dehidrogenasi alkohol
            """)
        imageKO1 = Image.open('Resource/image/Kimor/Dehidrogenasi_alkohol.png')
        st.image(imageKO1)
        st.write("2.	Hidrogenasi alkuna")
        imageKO2 = Image.open('Resource/image/Kimor/Hidrogenasi_alkuna.png')
        st.image(imageKO2)
        st.write(
            """
            Notasi Cis-Trans:
            
Jika 2 atom karbon alkena mempunyai 2 gugus yang sejenis, maka notasi cis-trans mampu dipakai. Jika gugus sejenis terletak pada tempat yang sama dari ikatan rangkap, maka dinamakan sebagai (cis-). Jika gugus sejenis terletak berseberangan, maka dinamakan sebagai (trans-).
            """)
        imageKO3 = Image.open('Resource/image/Kimor/Cis_trans.png')
        st.image(imageKO3,caption = "Sumber: roboguru.ruangguru.com")
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Alkuna</h2>", unsafe_allow_html=True)
        st.write(
            """
            Alkuna adalah molekul hidrokarbon tak jenuh yang memiliki ikatan rangkap tiga. Rumus umum: CnH2n-2
            
-Penamaan Alkuna:
1.	Tatanama IUPAC

Nama sistematis alkuna menurut sistem IUPAC diperoleh dengan mengganti akhiran –ana pada alkana dengan akhiran –una.

2.	Tatanama umum (trivial)

Dalam tatanama umum, alkuna diberi nama sebagai asetilena tersubtitusi.
            """)
        imageKO4 = Image.open('Resource/image/Kimor/Penamaan_alkuna.png')
        st.image(imageKO4)
        st.write(
            """
            Sifat Fisika:           
1.	Semua alkuna tidak larut dalam air (larut dalam pelarut nonpolar)
2.	Titik didih semakin meningkat dengan bertambahnya berat molekul.
3.	Kenaikan titik didih pada alkuna juga dipengaruhi percabangantom C

Reaksi penting:
1.	Adisi Hidrogen (Hidrogenasi)
            """)
        imageKO5 = Image.open('Resource/image/Kimor/Hidrogen_alkuna.png')
        st.image(imageKO5)
        st.write("2.	Adisi Hidrogen (Hidrogenasi) parsial")
        st.image(imageKO2)
        st.write("3.	Oksidasi dengan KMnO4")
        imageKO6 = Image.open('Resource/image/Kimor/Kmno4_alkuna.png')
        st.image(imageKO6)
        st.write("Pembuatan: Dehidrohalogenasi Alkil Dihalida")
        imageKO7 = Image.open('Resource/image/Kimor/Pembuatan_alkuna.png')
        st.image(imageKO7)
        st.write(" ")
        st.caption("Download Materi")
        st.write("Google Drive: [link](https://drive.google.com/file/d/1eAMRVME-3UA3idZkBo7D82KzdFy1mBwz/view?usp=sharing)")


    if optionKO == "Stereokimia":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Streokimia</h2>", unsafe_allow_html=True)
        st.write(
            """
            Studi mengenai molekul-molekul dalam ruang tiga dimensi, yaitu bagaimana atom-atom dalam sebuah molekul ditata dalam ruangan satu relatif terhadap yang lain.
            
Stereoisomer: senyawa berlainan yang mempunyai struktur sama, berbeda hanya dalam hal
penataan atom-atom dalam ruangan

a. Isomer Struktural

Isomer struktur adalah senyawa karbon yang mempunyai rumus molekul sama, tetapi susunan ikatannya berbeda.
1.	Isomer Kerangka (Isomer Rantai)

Isomer kerangka (isomer rantai) terjadi pada senyawa yang memiliki rumus molekul dan gugus fungsi sama, tetapi struktur kerangka atom karbonnya berbeda.

2.	Isomer Posisi

Isomer posisi terjadi pada senyawa yang memiliki rumus molekul sama, gugus fungsi sama, tetapi posisi gugus fungsi atau ikatan rangkapnya berbeda.

3.	Isomer Fungsional (Isomer Gugus Fungsi)

Isomer fungsional atau dikenal juga sebagai isomer gugus fungsi terjadi pada senyawa yang mempunyai rumus molekul yang sama, tetapi gugus fungsinya berbeda.

b. Stereoisomer
1.	Isomer geometrik atau isomer cis-trans : stereoisomer yang berbeda karena gugus-gugus berada pada satu sisi atau pada sisi-sisi yang berlawanan terhadap letak ketegaran molekul
            """)
        imageKO1 = Image.open('Resource/image/Kimor/Cis_trans.png')
        st.image(imageKO1,caption = "Sumber: roboguru.ruangguru.com")
        
    if optionKO == "Senyawa Aromatik":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Senyawa Aromatik</h2>", unsafe_allow_html=True)
        st.write(
            """
            Senyawa aromatik merupakan senyawa hidrokarbon yang memiliki ikatan tunggal dan ikatan rangkap di antara atom-atom karbonnya. Dengan syarat:            
1.	Memiliki rantai tertutup (siklik). 
2.	Memiliki bentuk planar atau datar.
3.	Memiliki ikatan rangkap terkonjugasi (berselang-seling) dengan ikatan tunggal.
4.	Memiliki jumlah elektron phi sesuai rumus 4n+2, dimana n merupakan bilangan bulat positif (0, 1, 2, 3, dst.)

Sifat Fisika:
1.	Berwujud cair dengan titik didih 80oC
2.	Tidak berwarna, tak larut dalam air, larut dalam kebanyakan pelarut organik
3.	Mudah terbakar dengan nyala bergelaga dan berwarna (karena kadar karbonya  tinggi).

Tata nama:
1.	Benzena Monosubstitusi

Sistem IUPAC tetap memakai nama umum untuk beberapa benzena monosubstitusi, misalnya toluena, kumena, stirena. Cincin benzena diberi nama sebagai substituent yang terikat pada rantai utama
            """)
        imageKO1 = Image.open('Resource/image/Kimor/Benzena.png')
        st.image(imageKO1)
        st.write(
            """
            2.	Benzena Disubstitusi

Jika ada 2 gugus substituen, penamaan diberikan dengan nomor atau awalan orto (o), meta (m) atau para (p).
            """)
        imageKO2 = Image.open('Resource/image/Kimor/Benzena_disubstitusi.png')
        st.image(imageKO2, caption = "Sumber: roboguru.ruangguru.com")
        st.write(
            """
            3.	Benzena Polisubstitusi
                1.	Jika ada lebih dari 2 substituen penamaan ditunjukkan dengan nomor, sehingga penomoran diberikan sekecil mungkin.
                2.	Jika ada lebih dari 2 substituent yang berbeda, penomoran diurutkan sesuai abjad.
            """)
        imageKO3 = Image.open('Resource/image/Kimor/Benzena_polisubstitusi.png')
        st.image(imageKO3, caption = "Sumber: fathchemical.blogspot.com")
        st.write(
            """
            Reaksi penting:
1.	Hidrogenasi
            """)
        imageKO4 = Image.open('Resource/image/Kimor/Hidrogenasi_benzena.png')
        st.image(imageKO4)
        st.write("2.	Sulfonasi")
        imageKO5 = Image.open('Resource/image/Kimor/Sulfonasi_benzena.png')
        st.image(imageKO5)
        
    if optionKO == "Alkohol dan Fenol":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Alkohol</h2>", unsafe_allow_html=True)
        st.write(
            """
            Alkohol (atau alkanol) adalah istilah umum untuk senyawa organik yang memiliki gugus hidroksil (-OH) terikat pada atom karbon.
            
Sifat Fisika:
1.	Alkohol merupakan cairan tidak berwarna (jernih) dan berbau khas.
2.	Hanya alkohol dengan struktur yang kecil/berat molekul ringan larut dalam air.
3.	Tidak larut dalam n-heksana. 
4.	Keasaman alkohol lebih rendah dibandingkan fenol
5.	Titik cair dan titik didihnya meningkat sesuai dengan bertambahnya Mr alkanol

-Tata nama IUPAC
1.	Nama alkohol diambil dari nama alkana dengan akhiran ˗a diganti dengan ˗ol. Alkohol dengan dua, tiga, dan empat gugus ˗OH di antara alkana dan ˗ol diberi sisipan di, tri, tetra sehingga namanya menjadi diol, triol, dan tetrol.
2.	Jika rantai pokok mengikat gugus alkil, penamaan dimulai dari ujung rantai yang mengandung gugus fungsi ˗OH yang paling dekat dengan gugus substitusinya

-Tata nama Trivial
1.	Pemberian namanya diawali dengan nama alkil diikuti kata alcohol
2.	Senyawa dengan lebih dari satu gugus ˗OH disebut glikol.

Reaksi penting:
1.	Dehidrogenasi alkohol
            """)
        imageKO1 = Image.open('Resource/image/Kimor/Dehidrogenasi_alkohol.png')
        st.image(imageKO1)
        
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Fenol</h2>", unsafe_allow_html=True)
        st.write(
            """
            Fenol adalah suatu rangkaian senyawa yang mengandung gugus hidroksil terikat langsung pada cincin aromatik.
            
Sifat Fisika:
1.	Kelarutan fenol dalam air akan berkurang jika gugus nonpolar terikat pada cincin aromatik.
2.	Tidak larut dalam n-heksana.
3.	Fenol bereaksi dengan FeCl3 dan memberikan warna merah-ungu.
4.	Keasaman fenol lebih tinggi dari alkohol.
                 """)

        
        
#Materi Fisika Dasar
with tab_5:
    st.caption('Pilih materi yang kamu mau')
    


