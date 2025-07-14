import streamlit as st

def app():
    # --- HERO SECTION ---
    st.markdown(
        """
        <div style='text-align: center;'>
            <h1 style='font-size: 3.5rem; font-weight: 700; color: #E2E8F0;'>
                Selamat Datang di <span style='color: #00A9FF;'>PropertyAI</span>
            </h1>
            <p style='font-size: 1.25rem; color: #94A3B8; max-width: 800px; margin: auto;'>
                Platform cerdas untuk memprediksi harga properti di Jakarta secara akurat dan cepat. 
                Buat keputusan investasi properti Anda berdasarkan data.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.divider()

    # --- KEY METRICS ---
    st.subheader("Sekilas Performa Model & Data")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Akurasi Model (R² Score)", value="~85%")
    with col2:
        st.metric(label="Jumlah Data Latih", value="5,000+")
    with col3:
        st.metric(label="Area Cakupan", value="DKI Jakarta")

    st.divider()

    # --- FITUR UTAMA ---
    st.subheader("Fitur Unggulan Kami")
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.markdown("#### 💸 Prediksi Harga Real-time")
            st.write("Dapatkan estimasi harga properti secara instan hanya dengan memasukkan beberapa detail kunci.")
    
    with col2:
        with st.container(border=True):
            st.markdown("#### 📊 Analisis Data Interaktif")
            st.write("Jelajahi korelasi antar fitur dan distribusi harga di berbagai kecamatan melalui visualisasi yang dinamis.")

    # --- PANDUAN PENGGUNAAN ---
    st.subheader("Cara Menggunakan Aplikasi")
    st.markdown(
        """
        1.  **Pilih Halaman di Sidebar Kiri**
            - **🏠 Beranda**: Halaman yang sedang Anda lihat.
            - **📊 Analisis Data (EDA)**: Untuk melihat visualisasi dan wawasan dari data.
            - **💸 Prediksi Harga**: Untuk mulai melakukan prediksi.

        2.  **Jelajahi Analisis Data**
            - Lihat bagaimana luas tanah, luas bangunan, dan lokasi mempengaruhi harga properti.

        3.  **Lakukan Prediksi**
            - Masukkan detail properti pada form yang tersedia dan klik tombol prediksi untuk melihat hasilnya.
        """
    )

    # --- CALL TO ACTION ---
    st.info("Siap memulai? Pilih halaman **💸 Prediksi Harga** di sidebar untuk mencoba!")
