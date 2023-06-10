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

with st.expander("Deskripsi"):
    st.write("""
            Nightmare Disorder Index (NDI) adalah sebuah alat skrining untuk penyakit Gangguan Mimpi Buruk.
            Ada 3 kategori hasil dari alat skrining ini:
            1. Tidak Memiliki Gangguan Mimpi Buruk
            2. Gejala Gangguan Mimpi Buruk Sebagian/Subthreshold
            3. Kemungkinan Gangguan Mimpi Buruk
            """)
    st.markdown('##')
    st.warning("""Harap dicatat bahwa NDI dimaksudkan sebagai alat skrining
                dan **TIDAK BOLEH** digunakan untuk menetapkan diagnosis definitif.
                Silakan melakukan wawancara klinis dengan ahli yang terkait."""
    )



if 'pilihan' not in st.session_state:
    st.session_state.pilihan = '0'


def up_pil():
    st.session_state.pilihan = st.session_state.pil1


with st.form("NDI"):

    st.markdown(
        """<style>
    div[class*="stRadio"] > label > div[data-testid="stMarkdownContainer"] > p {
        font-size: 20px;
        font-weight: 500;
    }
        </style>
        """, unsafe_allow_html=True)
    
    st.write('Pikirkan dalam sebulan terakhir…')
    q1 = st.radio("Berapa malam dalam seminggu, Anda mengalami mimpi buruk (yang mengganggu, berkepanjangan, membekas dalam ingatan)?",
                ('0 malam per minggu', '<1 malam per minggu', 
                '1-3 malam per minggu', '4-6 malam per minggu',
                '7 malam per minggu'), key='pil1')
    
    kirim = st.form_submit_button(label="Kirim", on_click=up_pil)


if kirim:
    if q1 == '0 malam per minggu':
        st.subheader("Anda Tidak Memiliki Gangguan Mimpi Buruk.")
        st.write('Selanjutnya, mohon submit hasil diagnosis ke form Usability Testing berikut ini: [Google Form](https://forms.gle/1PNAYjbGrnpNCcrQ6)')
    else:
         switch_page("Jaljayo2")