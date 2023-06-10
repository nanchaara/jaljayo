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
    
    st.markdown(
        """<style>
    div[class*="stRadio"] > label > div[data-testid="stMarkdownContainer"] > p {
        font-size: 20px;
        font-weight: 500;
    }
        </style>
        """, unsafe_allow_html=True)
    
    
    q2 = st.radio("Seberapa sering Anda terbangun dari mimpi buruk DAN tersadar dengan cepat?",
                ('Tidak pernah', 'Jarang', 'Kadang-kadang', 'Sering', 'Selalu'))
    
    st.markdown("##")

    q3 = st.radio('Sejauh mana mimpi buruk mengganggu/meresahkan Anda secara umum?',
                ('Tidak menggangu sama sekali', 'Sedikit mengganggu', 
                'Agak mengganggu', 'Banyak mengganggu', 'Sangat mengganggu'))
    
    st.markdown("##")

    q4 = st.radio("Sejauh mana mimpi buruk menyebabkan kesulitan dalam sosial, pekerjaan, atau bidang lain dalam hidup Anda?",
                ('Tidak menggangu sama sekali', 'Sedikit mengganggu', 
                'Agak mengganggu', 'Banyak mengganggu', 'Sangat mengganggu'))

    st.markdown("##")

    q5 = st.radio("Sudah berapa lama Anda merasa terganggu oleh mimpi buruk?",
                ('<1 minggu', '<1 bulan', 
                '1-6 bulan', '6-12 bulan', '>12 bulan'))
    
    st.markdown("##")

    kirim = st.form_submit_button(label="Kirim")



# edit ini
if kirim:
    if ((q2 == 'Tidak pernah' or q2 == 'Jarang') or
        (q3 == 'Tidak menggangu sama sekali' or q3 == 'Sedikit mengganggu') or
        (q4 == 'Tidak menggangu sama sekali') or (q4 == 'Sedikit mengganggu')):
        st.subheader("Anda memiliki Gejala Gangguan Mimpi Buruk Sebagian/Subthreshold.")

        st.write('Mohon submit hasil diagnosis ke form Usability Testing berikut ini: [Google Form](https://forms.gle/1PNAYjbGrnpNCcrQ6)')

    else:
        st.subheader('Anda memiliki Kemungkinan Gangguan Mimpi Buruk')

        if st.session_state.pilihan == '<1 malam per minggu':
            st.success('Tingkat keparahan: Ringan')
        elif st.session_state.pilihan == '7 malam per minggu':
            st.error('Tingkat keparahan: Parah')
        else:
            st.warning('Tingkat keparahan: Sedang')


        if q5 == '<1 minggu':
            st.write('')        
        elif q5 == '<1 bulan':
            st.success('Tingkat keakutan: Akut')
        elif q5 == '1-6 bulan':
            st.warning('Tingkat keakutan: Subakut')
        else:
            st.error('Tingkat keakutan: Konstan')
        
        st.write('Untuk langkah selanjutnya, silakan lakukan wawancara klinis dengan ahli yang terkait.')
        st.write('Dan mohon submit hasil diagnosis ke form Usability Testing berikut ini: [Google Form](https://forms.gle/1PNAYjbGrnpNCcrQ6)')

st.markdown('##')

back = st.button('Kembali ke Halaman Utama', use_container_width=True)

if back:
    switch_page("jaljayo")