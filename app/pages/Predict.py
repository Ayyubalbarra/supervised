import streamlit as st
import pandas as pd
import joblib
import os
import time

def app():
    st.markdown("<h1 style='text-align: center;'>💸 Prediksi Harga Properti</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94A3B8;'>Masukkan detail properti untuk mendapatkan estimasi harga berbasis AI.</p>", unsafe_allow_html=True)
    st.divider()

    # --- MEMUAT MODEL DAN PREPROCESSOR ---
    @st.cache_resource
    def load_model_assets():
        """Memuat model dan preprocessor dari file."""
        try:
            model = joblib.load(os.path.join("models", "best_model.pkl"))
            preprocessor = joblib.load(os.path.join("models", "preprocessor.pkl"))
            
            # Ekstrak daftar kecamatan dari preprocessor
            onehot_encoder = preprocessor.named_transformers_['cat']['onehot']
            kecamatan_list = onehot_encoder.get_feature_names_out(['Kecamatan'])
            kecamatan_list = sorted([name.split('_')[-1] for name in kecamatan_list])
            
            return model, preprocessor, kecamatan_list
        except FileNotFoundError:
            return None, None, None

    model, preprocessor, kecamatan_list = load_model_assets()

    if not model or not preprocessor:
        st.error("Model atau preprocessor tidak ditemukan. Harap jalankan `python main.py` terlebih dahulu untuk melatih dan menyimpan model.")
        return

    # --- FORM INPUT PENGGUNA ---
    with st.form(key='prediction_form'):
        st.subheader("Masukkan Detail Properti")
        
        # Layout 2 kolom untuk form
        col1, col2 = st.columns(2)

        with col1:
            lt = st.number_input("Luas Tanah (m²)", min_value=20, max_value=5000, value=120, help="Luas total lahan properti.")
            lb = st.number_input("Luas Bangunan (m²)", min_value=20, max_value=3000, value=100, help="Total luas semua lantai bangunan.")
            kecamatan = st.selectbox("Kecamatan", kecamatan_list, help="Lokasi properti di Jakarta.")

        with col2:
            kt = st.number_input("Jumlah Kamar Tidur", min_value=1, max_value=20, value=3, step=1)
            km = st.number_input("Jumlah Kamar Mandi", min_value=1, max_value=20, value=2, step=1)
            garasi = st.number_input("Kapasitas Garasi (mobil)", min_value=0, max_value=10, value=1, step=1)

        # Tombol submit di tengah
        st.divider()
        submit_button = st.form_submit_button(label='Prediksi Harga Sekarang', use_container_width=True)

    # --- PROSES DAN TAMPILKAN HASIL PREDIKSI ---
    if submit_button:
        if lb > lt:
            st.warning("Luas bangunan lebih besar dari luas tanah. Hasil prediksi mungkin tidak akurat.")
        
        # Buat DataFrame dari input
        input_data = pd.DataFrame({
            'LT': [lt], 'LB': [lb], 'KT': [kt],
            'KM': [km], 'Garasi': [garasi], 'Kecamatan': [kecamatan]
        })

        # Tampilkan ringkasan input
        st.subheader("Ringkasan Properti Anda")
        st.dataframe(input_data, use_container_width=True, hide_index=True)

        # Proses prediksi dengan spinner
        with st.spinner("Model AI sedang menganalisis dan menghitung estimasi..."):
            time.sleep(1) # Simulasi waktu proses
            try:
                input_processed = preprocessor.transform(input_data)
                prediction = model.predict(input_processed)[0]

                # Tampilkan hasil utama
                st.subheader("Hasil Estimasi Harga")
                st.metric(label="Harga Prediksi", value=f"Rp {prediction:,.0f}")
                
                # Berikan rentang kepercayaan
                lower_bound = prediction * 0.90
                upper_bound = prediction * 1.10
                st.info(f"Berdasarkan analisis, harga pasar wajar diperkirakan berada di antara **Rp {lower_bound:,.0f}** dan **Rp {upper_bound:,.0f}**.")

            except Exception as e:
                st.error(f"Terjadi kesalahan saat melakukan prediksi: {e}")

