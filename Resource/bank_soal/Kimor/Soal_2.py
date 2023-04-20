imageKO2 = Image.open('Resource/image/Quiz_Kimor/Soal_2.png')
st.image(imageKO2)
opsi1 = st. button("Ceritanya opsi 1")
opsi2 = st. button("Ceritanya opsi 2")
if opsi1:
    st.write("ya")
elif opsi2:
    st.markdown("<h2 style='text-align: center; color: green;'>Benar!!</h2>", unsafe_allow_html=True)
    st.success("soal selanjutnya!")
Next = st.button ("Next >>")
if Next:
    Kimor("Resource/bank_soal/Kimor/Soal_2.py")