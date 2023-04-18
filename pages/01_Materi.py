import streamlit as st

st.markdown("<h1 style='text-align: center; color: raisin black;'>Gaia Library</h1>", unsafe_allow_html=True)
st.subheader("Apa yang mau kamu pelajari hari ini?")

#Tab mata kuliah
tab_1, tab_2, tab_3, tab_4, tab_5 = st.tabs(["Kimia Dasar","Analisis Jenis", "Titrimetri", "Kimia Organik", "Fisika Dasar"])

#Materi Kimia Dasar
with tab_1:
    optionkimdas = st.selectbox(
            "Pilih materi yang kamu mau",
            ("--- Pilih Materi ---", "Atom, Molekul, dan Ion", "Stoikiometri","Ikatan Kimia","Sifat Fisis Larutan","Kinetika Kimia","Kesetimbangan Kimia","Asam Basa"))
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
        st.image("https://lh3.googleusercontent.com/Dpa6_SGiJeIeSfBCz0-JRD5GkMpAIbclqfSjcOigh8n3cFjzpJv_TFqWenYrr0-6gAS1BFSv32np17zNz6FURI7rU3GQH3X_Bh2YpOKJ6d15ekLvC6Snbh0pWqMkLLVGGmwH15FQz65sGiX0HvwHb6pqIch9OXy35ZfbkLLeBoN5KRB0dm6Jm3lBj2RiK26rhCqxPDLV_35nHTYMKVCu-JgnTRbP6dW7Gf4vvk1Iu9tMzWJknLHUWyCnqbFI9f9QCG-gilc1ozsWF1_cQTjjnhaQggoVwRYLOMss9CgZ0TtsmfM-6CNAO3EEb9pHvB1oWD97A07OQOCucPQcRoKjugNK8BxohAWIvpMY851B0XKP8dXAOAvJGl_CDNjGZKksW2Ass47WU0niLHzWEs3Ke3-H4BlttGF4sQb5VObbqb-tR4ZLdVbq3wzEPMaPweAZ_if3yi0uAT7tDunWpUtjSyQ_HoyyMs3JKkADtliNt6z9dlpe3V9QBQUiwEzUcQOVX3uiL7LjaKWVysamkEw5H4oZkrT4he8OJRlNqQRG4_IqS6QhplpAxdeEPTxa6VztZ69kTWo73BtbgQ7b2X58TnCPoLhTKzil2kkZQFPJ3eu3WWERih9gM3DXcafQ6TBTyIC9Y5Allml1ZtXEGaQxeuHkEQcOe7-cmws0vDiTWICrJi6muT_v779T7c0p5L2ZvtpZ5zZa7ccO8T5O0LQOA-LO4tO3U8vqqq6VfaNaKVOH0FRxG19ejA0T0NAxeEkZwmxt3RkT-wFin0gwxEJGnmjAbKPgOK_IaF2Do3YJzmimocVBiRzfqLRzXsIvHHMzBHFFHpRhztHbHQuk9Mm3orw6XABKeLe31KgvPrplUtniU-UwMA8-PsSigpfSqpRnXXeqlXATHziAfWN_pIw9rCIeAVh1vJCrGgotIhkirVU=w151-h320-s-no?authuser=0")
        st.write(
            """
            •	Teori Thomson

Setelah tahun 1897 Joseph John Thomson berhasil membuktikan dengan tabung sinar katode bahwa sinar katode adalah berkas partikel yang bermuatan negarif yang ada pada setiap materi maka tahun 1898 J.J Thomson membuat suatu teori atom. Menurut Thomson, atom berbentuk bulat dimana muatan listrik positif yang tersebar merata dalam atom dinetralkan oleh elektron-elektron yang berbeda di antara muatan positif. Elektron-elektron dalam atom diumpamakan seperti butiran kismis dalam roti, maka teori atom Thomson juga sering dikenal teori roti kismis.

Kelebihan: 

Membuktikan adanya partikel lain yang bermuatan negatif dalam atom. Berarti atom bukan merupakan bagian terkecil dari suatu unsur. Selain itu juga memastikan bahwa atom tersusun dari partikel yang bermuatan positif dan negatif untuk membentuk atom netral. Juga membuktikan bahwa elektron terdapat dalam semua unsur.

Kelemahan:

Belum dapat menerangkan bagaimana susunan muatan positif dan jumlah elektron dalam bola.
            """)
        st.image("https://lh3.googleusercontent.com/ggTz_zX8FAvn9TdSDsLu0zSEuGjwAZnoDFMC6pbSTsdC5TYD7-Od1-c6_7SJIo42K_-9EONsDAK2O1Zw6-xrrXqi8wxbiA91yscsomhtCZKQ6oPcoJ6816W6KtCZlovAzY6SUaK1FDzTOPYUAWNrufWJ7DLvAhV-VxC6mFuqqy9who3j5hgPXKyDwBRtgcffvSyQF4D3pnNAgo5J1abnJbXpVhJJOwsi2kZ-Sg9xJ6xEfshUZ_OKBQd2Dzvy74U_p2lxIwS9EeeteXRjAqmrNpvxecsArywlIzUHAXpYvjTpmWp7IqF_dRPyKBekcxtVrwkHwPKSBbMxS4V3ufAZhTPoS0AqaTN_qklE5xooDGknpWcLmuRtuB5WFdZT0j-BSfj_8CEGmGrrHtPnZXBs3LA2f5P2nWXe-Ntl6dMZsinSoSA127lT4LADEj7e3YLguI134bEY8-hWc6N6d3VU9UaCIG7Qzn3so4SC3F0Us-ikC_vLUGYF4TXfrSE4oEVZ-xw5iEIy6IRK9eAjRYiZ6wQUFz9m8i7mR-otRHIswdcxfdbz-U00TJfLoQqbVKpgKYrRWCnL1gX2xzJapBVxrf00rdzP9N8t_cZ43u53yHtZOGbOrsEBT5yJ-i5fGhWldSdLFPHhIdG1VuhJqXqy1XAqmXkUwoq4OxEp7mOcTEu2evChv47vvHj9dqlYVu5sNm1252h5WMNEpE0L7Fb8afAQCgiDrLhphBOMk6pxKXYqoRn5tmsZlgxi9l9XYTmDOaQ3L03D6AkHxWkgCPOwicEczLzJ_Qjvw19c8TPGk-4LapZze0dRTDi8ETj5oCwZ2JBm4OVwFTT9VYJHZdVS8yld1mrEGtPfI_kznJ7t4IdWSI8kkd1HeaSQd04FQnFCK2vmLLQwtlVaAO--RaZHxLdTdJIehKrObKdChvImjjY=w320-h253-s-no?authuser=0")
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
        st.image("https://lh3.googleusercontent.com/E-KXyUbelh2JObbxqtd_IfHJ2R1HAobVWP3FpWj1jdU1u7nO_vjuNSPzc5Cq7qPpg1sXEjRbzyLx8nevrez4xduWWznsmg6PJr40px0VNYriWpYIxELXR53S_XdX235YNBl449csZODin55FMaZlbWcBY1MzaocrgAEOTJeGEAe-kzKJJJaeUEPoSCpA5m3BxYY4TawGIsy5GDLwqZrROPnJP2GIX1T8Z5tLDlOBXs7dr0DVFzkNcsrEviybSqQ9wNI1ZuXowb4btnpwX2kOIkWWwovjEZc5XpcerN-E8HPf7tOabOgztvRsPjHj_y9mqZUZyCezChhjwlfSTDuhkzCAT-M33CsQQgDqdH6mIOOmG_1a0KppQ55AlJywAuNQCqK4S5o9sbSiJvHBXz_wUtkNKTmpiiIEB9OTaVy4ILuEmBL80tM9XDq0zgg7w2pTMY6rzvxnSOxoZe3KgW04IUY0gSTA6bm01duHJYDRPaow7g2qydFQEZq0YiYX1lK8IRA0_buXTomf90iD7cg3oTCQx7FYtMGnWP_2QDFrkWSVuPfInAaiQBpYm_x1HCMzRBqIT0zCp9i7iDWUYWoLRBaRebiynk7OH1RAgOWYn95NsQM6G0-mSkaaP5O2TfI6TnoW5gRnvYH-5NWSCG73Uq9wyOdBv_aqlNs7ESahxFbEQUYYQFS7jldTDRCxVrezd5NoW_e-GUq51ikvXMsn-XzocTWWVuxQdM05lCAm_c8chPGdX9hHjmy2FmO7YtIzbskLxseaiwDwfz1JIJX65DOJSBG5OTqyXjhJZzG6nYMmnr2LzpnjegxWjCA1vUpXWYC1q71e51ukLCXlvx8uj50tcGlBUp3AjttUdeoyTlv13kKYyri5AFr34fIyxriAAprhs0pCNs1sTNIT4bBOKnLSt_tFgEwjY2FX52RBF7A=w311-h264-s-no?authuser=0")
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
        st.image("https://lh3.googleusercontent.com/d2FudpfuSIr4NJIyqSVP18ZpPKwIf4RLLkr00Z1qgiJLVTa37HpnsfjexBbaGKZ-2BvS1y61PKPEtL9VKmm9-U7vW9caahlLKJsQ7gfgZXqhkSwG8JBmyolnRvzVnqsMu0mBlKVQFp3Pt1X0BSLcTMRyabX-JsKFpjNCl7kY5U3Odr8txN0DUR7csrO_7gs6eNuzMdlhM9-YUD6ccUBp3Y5H_MiK45CjnyjHT_JE70U93BLN9VgWRcHnmVLhpIDw1Xo_wGgK-HAliENOQI95sKLpvYVDqnCGjekRkCK9i-bH65YypdvDyslXEUtAZN-NJbPJ9yh3Mt8zoyvYWjYTwZxARw5RnCF7vFrYVg-HsFlOMlyx5FSQbtTYCaILH_YNSur-Lj83Sy689XCQMaKY6MnxbtdtXS9QpllJiXUP5osCfVgreIifmUHfTCmm8OT6McrTvkfv6VqGpK9RwcozPaJyAwUy-w4mA9nB1OvITzlkCFlgRIaAIHdh6PdIFM-K6t2tC-Ypx_1Fs4HeXt6xj0x_Q5fSA6eqCy7tKOwjAobZqBUzAMrXiNV4FW1RRqKVwjnNUv30ZkY3bTFU9O73Uihz7ED8XZd7S4Jppy4ONF08Y_WNrnbQr852IP00-27sxEt8WnOsF92hcZUKpONNhiNZaLCHBl7eP2kfMVlzu4iTRliW7nX3BdIW64tZ_c-Zx1Z3E3U8vLaf5ExuZz8IMHk37YZw4I6rHU1eVeyU6EaNfnHjw12xQ-rQVt-ez3Kuk3Kb7pRsth5QHsH19pULW70lQ23nWL5mlGEvUB9CY-ResqDMsKBVFzH8dUApSbWQbJDCidVRChEPxtaIo6bP4QlDl3BvQRN-jw0LqrVGbau6ethI6bCq00IKLlCiM5P7u0ZzygntPEC9Rdqdo8aUPniVCxryX5P2TokoD1obeH8=w230-h248-s-no?authuser=0")
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
        """)
    
    
    
            


       
            
                
                
#Materi Analisis Jenis            
with tab_2:
    optionanjen = st.selectbox(
            "Pilih materi yang kamu mau",
            ("--- Pilih Materi ---", "Reaksi Kimia dan Persamaan Reaksi", "Satuan Konsentrasi", "Pemisahan Kation Golongan I-V", "Identifikasi Zat Dengan Cara Kering"))
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
  
        BE garam = (BM garam)/(Muatan anion×jumlah anion )
  
      BE garam = (BM garam)/(Muatan kation×jumlah kation )
        
        """) 
                      
    if optionanjen == "Pemisahan Kation Golongan I-V":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Pemisahan Kation Golongan I-V</h2>", unsafe_allow_html=True)
        st.write(
            """
            Kation-kation diklasifikasikan dalam 5 golongan berdasarkan sifat-sifat kation itu terhadap beberapa reagensia, penggolongan ini didasarkan pada terbentuk atau tidaknya endapan jika suatu kation bereaksi dengan reagensia tertentu, reagensia golongan yang dipakai untuk klasifikasi kation yang paling umum, adalah asam klorida, hidrogen sulfida, amonium sulfida dan amonium karbonat.

     Proses analisis kation dan anion dilakukan dengan dua cara yaitu pemisahan dan identifikasi. Pemisahan dilakukan dengan mengendapkan kation dari larutannya. Endapan yang dihasilkan dipisahkan dengan mencuci larutannya dan dibuat larutan dengan jalan mengaduk menggunakan alat sentrifuge lalu membagi dua hasil penyaringan. Larutan yang masih mengandung kation lain lalu diendapkan juga sehingga terbentuk grup kation baru. Apabila di dalam grup tersebut masih terdapat kation lain, proses pengendapan dilakukan lagi sehingga tertinggal hanya satu kation saja.

     Jadi boleh dikatakan bahwa klasifikasi kation yang paling umum didasarkan atas perbedaan kelarutan dari klorida, sulfida, dan karbonat dari kation tersebut. Kelima golongan Kation dan ciri khas golongan-golongan ini adalah sebagai berikut:
            """)
        st.image("https://lh3.googleusercontent.com/knukFM1Dh0Rty2iINjc91YuUlRQX4PC14x0WpDHK5EKvB_e-u5Yd5SQPwtetdSEQSoXBxnLLFEUYUwb_BnGGHUgi6tFNxwuA9pfnAEifL45ZdbjAspKAK0OfZCLHxkU4s5tMoYfUvS_Nn9x23XiVKRfZJphdHtY9V8xf7vgjQw3AzbZ1_eEdGEd3x-wdrL4iSTyxycR27-90WaduGX-pRfrZvi0aUuBnojnrKk6n3OV7Erzf6IMsFesWws_j6NBh4X2i9kaKuLUwZX9GmqtOV3s45k3SXQH_8JZTxWNvARrvFSpCeF66lm2b4knzBit26-6bJQZc6rmmYFMfb4c4vFk2_ghdR4UiuXVX8u2bDqGZ1L2LJCHgplx1z12xGjDcsxGEImLMJI1FYvLxXdyGNVTuacXJkG_RlO1jgqJRtwpJdKCqjCFrsrdvQ7AzQ9pJdaSalgaEk3Ts1evfBzKu3CD5ESoDVKakwOzcjTtFpTIFq71gV_9KSJnqYzIWnNhhkxdpwiUabtynzDuQ9pe3f0MpxbvoeYYVICJ0Jgucr5-wQ9sWojLvuPbhkHAV9k63BkKjG8dzGoPvJUNHGnDhaL2sMiQ0_dZprlPuzeQ1bGETMPgHeOSpBrGC_L-BH7MSSxrB4MavmzCvSPxsroX4sle1Kx1Pc4Np4zW7jPqpI8PPf4_CgsOkwCbHcU0alwTRJtHP-LNAIsk0GFaD7oNIXTcilKu6ZcVdlDGQOnLB8vO24HOERcRuOIWBzKJtejP-YI5M_tHwVFS5qxcgUPAWTeA9qQg-EwW6yjKP-16h2UjPt9za8I1nGEfBBtNMZM-8pX3W_lNebCo7rcKkz9IfaoFeqyW8lYi1moDbKaw1HISSUR4nQuoxfPWLGZD3u08D3MxJcW_rn1zRhSheg4_3Flq1G__1-3PvfZl-r4FRVpaHLONUO14mUgl2ciaELkYYtU5GN9AuiTR4_W6MjoM=w1124-h657-s-no?authuser=1")   
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
        st.write (
            """
          Setelah ditambahkan hidrogen sulfida, kemudian saring menghasilkan filtrat dan residu (Golongan III). Filtrat ini mungkin terdiri dari sulfida-sulfida logam logam IIA (HgS, PbS, Bi2S3, CuS) dan sulfida-sulfda logam golongan IIB (As2S3, Sb2S3, Sb2S5, SnS2). Pemisahan golongan IIA dan IIB dilakukan dengan mencuci dengan sulfida yang diendapkan dengan sedikit larutan NH4Cl yang telah dijenuhi H2S.
          """)
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Pemisahan kation golongan III</h2>", unsafe_allow_html=True)
        st.write(
            """
          Pemisahan kation-kation golongan IIIdan golongan-golongan lain yaitu dengan menambahkan H2O dan Panaskan, kemudian saring menghasilkan residu dan filtrat (Golongan IV). Endapan yang dihasilkan tersebut ditambahkan sedikit air, NH4Cl serta larutan NH3 dan panaskan hingga mendidih, kemudian saring menghasilkan residu dan filtrat. Residu mungkin mengandung golongan III.A yaitu MnO- , Fe(OH)3, Cr(OH)3, dan Al(OH)3, dan filtrat mungkin mengandung CoS, NiS, MnS, dan ZnS.
          """)
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Pemisahan kation golongan IV</h2>", unsafe_allow_html=True)
        st. write(
            """
          Hasil filtrat yang diperoleh dari pemisahan kation golongan III, mungkin mengandung golongan IV dan V. Cara pemishananya dilakukan dengan penambahan reagen natrium heksanitritokobaltat(III) sebanyak 5 mL, kemudian saring menghasilkan residu dan filtrat (mungkin golongan V). Pemisahan Kation Golongan IV dengan Metode Sulfat yaitu residu yang dihasilkan mungkin mengandung BaCO3, SrCO3 dan CaCO3
          """)
        st.write(
            """
            
            Daftar Pustaka:
            
        Svehla,G.1990.Buku Teks Analisis Anorganik Kualitatif Makro dan Semimikro.Jakarta: PT. Kalman Media Pustaka 
        
        """)
 
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
    if optionanjen == "Pemisahan Anion Golongan I-V":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Pemisahan Anion Golongan I-V</h2>", unsafe_allow_html=True)
        st.write(
            """
            Klasifikasi anion ini adalah salah satu contoh pengelompokan anion yang dibagi berdasarkan reaksinya dengan asam klorida encer (HCl(aq) ) dan perbedaan kelarutannya sebagai garam barium dan perak. Empat golongan anion dan karakteristiknya adalah sebagai berikut:
            """)
        


        


          
            



#Materi Titrimetri
with tab_3:
    optiontitri = st.selectbox(
            "Pilih materi yang kamu mau",
            ("--- Pilih Materi ---", "Pengenalan Analisis Titrimetri"))
    if optiontitri == "Pengenalan Analisis Titrimetri":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Pengenalan Analisis Titrimetri</h2>", unsafe_allow_html=True)
        st.write(
            """
            **Definisi**

Analisis volumetri /analisis titrimetri adalah teknis analisis yang berdasarkan pada volume suatu larutan yang sudah diketahui konsentrasinya yang diperlukan untuk bereaksi sempurna dengan sejumlah tertentu komponen cuplikan (sampel).
            """)
        st.image( "https://lh3.googleusercontent.com/98gichc05P2wpKSwG3bKYBqS6qWV5QLDRsB7AfWUoziAelCmOUq7p4jLaSi80jy_TosulRPrXGU4Vb6nLy30zMXaiZiwMhovyRULQcDgibjGF6RfURfYgUJnf0JgoRJY2DPg_JIP6SY7l5nFQjKmB21ctUwYEbQkPCuyhn6TxRyI1aeKb2pTxqY2iazihA1v7NbO3Th1-5TmIf7PAtl0y0nW_DnTEBWybTz9e9JnlM1gXre78eK3etV07qVeGEajaA0hx_gOuKQjv3U5bWV0VEfwsME3uExsjLJwwtKto6Eti09CoSflIo7llbUOo9v4TZO1OccPxvrUFIbg6e_2d9NwCZD_FGpXSge44ZZMYHk3JQ-835TwY7l1JrXD7TcT4zzVid8neR7hBkgABqKZwixrr8NLoF2D1U5PPZ2qQWWr4rpI3PG8jZmoV_yfNHhXgBJc6nKjMXRnsbU4ckCCcVeh86xeq9WSkN5EGQigP-PNOvb7QTHjQrx_j_Eia40ARGpRugxKC1H0j3Eh27f39zIZVQrE3yXYyG8HzlmKjonXrrKMO-6Hzry0zGzN8D6nJM725rKtAv8icJAu10mRYWgfODPPHiL871cTvlUgiiWcBVaU6tIxnzk14XT9mto6VKIeleRQ6EJlXo-yxuvnR-wJuDjWNfi4lpxLrJ1IlOLJw1sbRcX3AhdsYtQLuxyQfBP8e0j1bK2IplIEh9oCM-r9Ou0jv6QfbIV0vuIYxVQMVitw9R0cVt83pZD9YjWp2OX4wR9FG6JBTdJ2IcdDjeMHx24r_94C0ATgZR9frPoZP_Xm6LwPHZ3jLvEiG5LnC-7ysSl5abaOPAO7WM4cq8D_69tC0OLqitl9Z6wSjqJ1_4QnbmblR8ywEwXZCb2JKb2YoQ-RyonKbdfPqQehp4OnUevdpPQPcH7sCHa67Irn=w1167-h862-s-no?authuser=0")
        st.markdown(
            """
            Istilah dalam analisis volumetri/titrimetri:
•	Titrasi adalah proses penambahan larutan standar dari buret sedikit demi    sedikit sampai jumlah zat yang direaksikan tepat ekuivalen satu sama lain.
•	Titran adalah zat yang diketahui konsentrasinya yang digunakan untuk menitar zat lain
•	Titrat adalah zat yang dititrasi
•	Titik ekuivalen ( setara) adalah titik pada saat titran yang ditambahkan tepat ekuivalen dengan titrat maka penambahan titran harus dihentikan
•	Titik akhir titrasi adalah titik pada saat titrasi dihentikan yang ditandai oleh perubahan warna dari indikator
•	Indikator : Zat yang ditambahkan ke dalam titrat sebagai penunjuk titik akhir titrasi
•	Larutan standar ( larutan baku) adalah larutan yang konsentrasinya diketahui secara pasti

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


        
#Materi Kimia Organik
with tab_4:
    optionKO = st.selectbox(
            "Pilih materi yang kamu mau",
            ("--- Pilih Materi ---", "Pendahuluan", "Alkana dan Sikloalkana", "Alkena, Siklodiena, dan Alkuna", "Stereokimia", "Senyawa Aromatik", "Alkohol dan Fenol"))
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
        st.image("https://lh3.googleusercontent.com/N4b4wt-ZhYeNIk2N7NoUrhYSQ65BxWjDJ1QbxXPAX4srb0ysTU-KAaTm3thn9_6FvvMaPrBI_BYZESuIXoAolap3YsBf9K8HOOmnOPk53fOtZ50g8hPb4xXFvwZKL5Bxpdhd_MdujSVi9LaQOynUnAYlVAVS_mbV40xceEGkt7Apm-lhlHNQFwVRCliR_iPNHOSobw_toD9WqLSWOtI3qmVYmls1N0QZJH-n_5oB_uE4yv1_oSGm8UV0g1rrnDMZ0nlI5m9gDV_TBEEFjnd_9dOmlf9V7AVFVeDZQ0XAiC-Ngmm0Qq4-r4tnN3cvKuQAlG2MNOgQDCZJJ8Ra4GJ6_vQf-RmqmeCrRq5GNJivvOLR_K619DBMRQJyzP1ee2xuNMBVKmLsR0AjxnELcN11EHqSwV_BRpi9tkRbPxJBDNm1aeWeWQpdfs-rIRRxEmgIy7tzy7_6g_ZdujzvJKyshVsnElxbpGURA4_Gn-H70n9N3crTA48aJ5fiewKJ8EMCMCuGI26irtwbqHY9qcJymdMfLpg-wzvastySZ8ul73pVF12F8bqSq0X1bulPuhjL35KYU89TbQVZAu9CJUYxSWcmxBaXQzEml10DMjhl4ss5uS4VrI6n5MPRMalFRZzE3_20B-Jmp16AEmHA-HqMbnOmQr_t4Lir91xHE1rzDaU1UrRIkqeUVA2WPKr8JIa-EAqkgSEbfbMbSGaxZ48UEK8EjxpV3eb-L-ciptl7wA3vdfLF8bjk54M0cf3jI9qhbWJvZp3q9LdDFNyQPee-8GOfZG7-HkTzUNSrIic5ShFJCi5Tf2gbuU_TyVgyrs2l1VAqOjp5RPIe1gBp8suhTsfnrt1Hra-zJrdKh5DZaf7TO_OuWKO8CbpZNzyXif4ZJ7ElwUKGks1C7TPfPMkHQpYmtvLSNtzyZWssweAb4w6U=w1481-h390-s-no?authuser=0")
        st.write(
            """
            Dalam hidrokarbon, berdasarkan jumlah atom C yang terikat pada suatu atom C dibedakan menjadi 4:
1.	Atom C primer (1°)
2.	Atom C sekunder (2°)
3.	Atom C tersier (3°)
4.	Atom C kuartener (4°)
            """)
        st.image("https://lh3.googleusercontent.com/lPpgG193slre_Zj7oz7gO173qyGZI5uPtTAacxlNf2KaCiH4b0r_3RlQ98EcSrCK-QhYiVuLEgWn7ncuxe6BLIffUDraWCwcfPxh5YHJUGRP58sYh1JYpfiKjr-0YSzrvodFbg1tarHu-Z21Yao6CsXs21dEC4tkuOk5r0dd3t4To0egxYVtQU-8rdWwLaVPcWgamOkkA1hqglggDbm-o6jWfFIKNwVDkWDPIZcWmnDlmaDNJTh8K10xjS87D_PAqpkJOjcr9Y5m2j_AiTLHK-Oy6q9nZGaUdjJX83vIk9iqiQAKH6OS5hEjnPr9lAUqHjRHYfzScgQj1IFRylzHsGLs3beWYNqQpyLh-h6UfFp1fTI_2MynSfYdmgeveDFb_Tu6ksDFuJOda90h-4SxOkJAzjz7jBOrEn0arMgDViF0ogY0kSZtI_f6lsLIHsas-JrjQ7dx3scKKaWILkCaJ8hLgtBklD50Mqgejs83yFoXtc5mlt7EWlkR46UUvp75xxHe5wbR0po4-VVZTHruSWVT3wQmT1asOPwAnC5jQQtZT_GsGsYCKrlMK6HHev9U5Sp3xwgkn8GeFmHhlnw9zqk50BM3_LemKo-TSjRU_auTc5h3v98SIywRpwCQUZTuBLHlDEA1pNY-lLFps-iat3sKx2yXUL6lBCYkacovy-UStWa32td_aYsAqnx7A8y1K8Fj1j_GzZNq9_GN0x2ljN1C13WHZlDTduSyKsZwanVcvrMEVH5TahMeafkaaMJkm73DqJMMydnB3BJBNrz7itH63STm6Asblvu3so3_f9K2_PUelwCKfk62pq63NpBO7tSi9_NHB-GIL7H26DL1OM5wLMiqkhFuFL6XXdsztAkdxyzwqm14EQSNzXnB4i764pH0JduaU4RdgrXf23WzfwhBZHp4ScVEsXKqOcocktqm=w1481-h390-s-no?authuser=0")
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

Aturan-aturan pemberian nama sikloalkana bercabang menurut sistem IUPAC:
1.	Jika terdapat substituen, maka nama cabang disebutkan terlebih dahulu diikuti dengan nama sikloalkananya
2.	Jika terdapat lebih dari dua substituen, nomor pada cincin dimulai dari substituen yang memiliki urutan abjad pertama, dan arah penomorannya memberikan nomor terendah untuk substituen selanjutnya

            """)
        st.image("https://lh3.googleusercontent.com/XAcjpKSETswVLs_Nr_ROHA8cXhuqOprYT3zkz0cmmXTHGUV6KQQufUzoD9qgO7viiAAi-rKP_qsPhRdW7GISJCVjOgeQXRpnFbJehdcKsC3CRcGQ8-BmTxtF6rKYutOzNwU0J8q-6ZoZuyrCQLGrLnS_W1VQegjUNUCTwpe6BwBVgF69TqDRuI48vZhtIOhikOsU8d6Dl0UC7dlzz3PtmGCeAOGZsoarR97zdQDRfVCKxZV9iGV1_fm81pKrN9s--AjxJ4ooZssA5XaX3dtzwsy_k-OqFSyUAa66wX1tlyZq4kfYFtoTqzU3StL3DcT5SjNO4O_fzbGr87nS4qP6az7c5VTcsafmn1rSwhRzwU7q3LPlFRuy2CjkHrw17XE132MPwSC-xLvZh3x6HqoLgiuNVB4OHnAKp7O_MKlJh1F9FvldItbG5v2z0-PPEsVCre7SRLd1Krh2dv8VZ-4oEw3xc1TZmyzQMwZRKZE5KFd0GcxyI4XEinvb_8Tt5Vn0ATBKhX7qZa5RguM9CodqjESf22w4RVJHcUEd08GUt13aIfRc4NbF5niCUcygADD9_6LD0j-fpZyFGb0nMWxMBCR9676_2U9RtpWmWCXjJJCXp4x7Z7D9OQs01dGkQOTKLS8BuCnIm_8Z3jfQSIy6cyxIRZ1M809c_3HVac3YEJvhUBoNod6mgS3AiD9gicy46gqjxNzsT4b8gjfnOw0G3wUZE_ZndPV_ROoSXl8ZCMKOA7DS1xd9KRm4Ua0kSiPhCMjjytgoSEsu5P2Wm8hbmN-OE1WQ3Y_JNEAEY_qjX9EaAMKxV3eAH_R4LhGw276eJMGJiHcgfSBLolD3sJgUgBjDl25_byqvddY_NMrRcDZ3vTxpWUJ1rqSGXOWLq1OROvwr2AY4PTwHIEm2vg8WYgRc4jZzCFnKSdQW2K3HI0VO=w1479-h422-s-no?authuser=0")
        st.markdown(
            """
            Daftar Pustaka: 
            
            SOLOMONS, T. W. G., C. B. FRYHLE, & S. A. SNYDER. 2008. _Organic Chemistry_. Edisi ke-12. John Wiley & Sons, Inc. Hoboken.
            """)
        st.write(" ")
        st.caption("Download Materi")
        st.write("Google Drive: [link](https://drive.google.com/file/d/1bLafimHyPEi7Mmci325iffq8MrxC0nVM/view?usp=sharing)")
        
    if optionKO == "Alkena, Siklodiena, dan Alkuna":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Alkena dan Siklodiena</h2>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Alkuna</h2>", unsafe_allow_html=True)
    if optionKO == "Stereokimia":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Streokimia</h2>", unsafe_allow_html=True)
    if optionKO == "Senyawa Aromatik":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Senyawa Aromatik</h2>", unsafe_allow_html=True)
    if optionKO == "Alkohol dan Fenol":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Alkohol dan Fenol</h2>", unsafe_allow_html=True)

        
#Materi Fisika Dasar
with tab_5:
    st.caption('Pilih materi yang kamu mau')
    


