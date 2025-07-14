import streamlit as st
# Pastikan semua halaman bisa diimpor dari folder app/pages
from app.pages import Home, EDA, Predict

# --- KONFIGURASI HALAMAN ---
# Harus menjadi perintah Streamlit pertama yang dijalankan
st.set_page_config(
    page_title="PropertyAI Jakarta | Prediksi Harga Properti",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- FUNGSI UNTUK MEMUAT CSS ---
def load_css(file_name):
    """Fungsi untuk memuat file CSS kustom."""
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Memuat file style.css
load_css("style.css")

# --- STRUKTUR NAVIGASI ---
PAGES = {
    "🏠 Beranda": Home,
    "📊 Analisis Data (EDA)": EDA,
    "💸 Prediksi Harga": Predict
}

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #00A9FF;'>PropertyAI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94A3B8; margin-top: -10px; margin-bottom: 30px;'>Prediksi Harga Properti Jakarta</p>", unsafe_allow_html=True)
    
    selection = st.radio(
        "Pilih Halaman:",
        list(PAGES.keys()),
        label_visibility="collapsed" # Sembunyikan label "Pilih Halaman:"
    )

    st.divider()
    st.info(
        "**Tentang Aplikasi:**\n\n"
        "Aplikasi ini menggunakan model *Random Forest* untuk memberikan estimasi harga properti di Jakarta."
    )
    st.markdown(
        "<p style='text-align: center; font-size: 0.8rem; color: #334155;'>Versi 1.0.0 | Dibuat oleh Ayyub Al Barra</p>",
        unsafe_allow_html=True
    )


# --- MENJALANKAN HALAMAN YANG DIPILIH ---
page = PAGES[selection]
page.app()
