import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Selamat Datang", page_icon="👋", layout="centered")

# Data pengguna
nama_user = "Faldo Afandi Saputra"

# Tampilan halaman
st.title("👋 Selamat Datang!")
st.header(nama_user)
st.write("Senang melihatmu di website Streamlit ini. Semoga harimu menyenangkan!")

st.divider()

if st.button("Mulai"):
    st.success(f"Halo, {nama_user}! Selamat belajar dan berkreasi.")
    st.balloons()