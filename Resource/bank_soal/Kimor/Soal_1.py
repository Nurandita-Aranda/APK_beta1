imageKO1 = Image.open('Resource/image/Quiz_Kimor/Soal_1.png')
st.image(imageKO1)
opsi1 = st. button("2-metil-1,3,5-trinitrobenzena")
opsi2 = st. button("1,3,5-trinitro-2-metilbenzena")
if opsi1:
    st.markdown("<h2 style='text-align: center; color: green;'>Benar!!</h2>", unsafe_allow_html=True)
    st.success("soal selanjutnya!")
elif opsi2:
    st.write("Salah cuy")
            
def Kimor(file_name):
    with open(file_name) as f:
        st.markdown(f"{f.read()}", unsafe_allow_html=True)
        
Next = st.button ("Next >>")
if Next:
Kimor("Resource/bank_soal/Kimor/Soal_2.py)