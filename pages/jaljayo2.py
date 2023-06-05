import streamlit as st
from streamlit_extras.switch_page_button import switch_page


st.set_page_config(initial_sidebar_state="collapsed")
st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)


st.title('Jaljayo')
st.subheader('Diagnosis Awal Gangguan Mimpi Buruk')
st.write('Dengan Nightmare Disorder Index (NDI)')

st.markdown('##')
        
st.write('Halaman 2')

with st.form("NDI2"):
    q2 = st.radio("Seberapa sering Anda terbangun dari mimpi buruk DAN tersadar dengan cepat?",
                ('Tidak pernah', 'Jarang', 'Kadang-kadang', 'Sering', 'Selalu'))

    q3 = st.radio('Sejauh mana mimpi buruk mengganggu/meresahkan Anda secara umum?',
                ('Tidak menggangu sama sekali', 'Sedikit mengganggu', 
                'Agak mengganggu', 'Banyak mengganggu', 'Sangat mengganggu'))

    q4 = st.radio("Sejauh mana mimpi buruk menyebabkan kesulitan dalam sosial, pekerjaan, atau bidang lain dalam hidup Anda?",
                ('Tidak menggangu sama sekali', 'Sedikit mengganggu', 
                'Agak mengganggu', 'Banyak mengganggu', 'Sangat mengganggu'))

    q5 = st.radio("Sudah berapa lama Anda merasa terganggu oleh mimpi buruk?",
                ('<1 minggu', '<1 bulan', 
                '1-6 bulan', '6-12 bulan', '>12 bulan'))
    
    kirim = st.form_submit_button(label="Kirim")



# edit ini
if kirim:
    if ((q2 == 'Tidak pernah' or q2 == 'Jarang') or
        (q3 == 'Tidak menggangu sama sekali' or q3 == 'Sedikit mengganggu') or
        (q4 == 'Tidak menggangu sama sekali') or (q4 == 'Sedikit mengganggu')):
        st.subheader("Anda memiliki Gejala Gangguan Mimpi Buruk Sebagian/Subthreshold.")
    else:
        st.subheader('Anda memiliki Kemungkinan Gangguan Mimpi Buruk')

        if st.session_state.pilihan == '<1 malam per minggu':
            st.success('Dengan tingkat keparahan: Ringan')
        elif st.session_state.pilihan == '7 malam per minggu':
            st.error('Dengan tingkat keparahan: Parah')
        else:
            st.warning('Dengan tingkat keparahan: Sedang')


        if q5 == '<1 minggu':
            st.write('')        
        elif q5 == '<1 bulan':
            st.success('dan dengan tingkat keakutan: Akut')
        elif q5 == '1-6 bulan':
            st.warning('Dengan tingkat keakutan: Subakut')
        else:
            st.error('Dengan tingkat keakutan: Konstan')



back = st.button('Kembali ke Halaman Utama')

if back:
    switch_page("jaljayo")