import streamlit as st
import pandas as pd
import plotly.express as px
from src.data_loading import load_data # Pastikan path import ini benar

def app():
    st.markdown("<h1 style='text-align: center;'>📊 Analisis Data Eksploratif</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94A3B8;'>Memahami karakteristik dan wawasan dari dataset harga properti Jakarta.</p>", unsafe_allow_html=True)
    st.divider()

    # Cache data untuk performa lebih cepat
    @st.cache_data
    def load_cached_data():
        # Memuat data dari file
        # Fungsi load_data() ini harus ada di src/data_loading.py
        return load_data()

    try:
        df = load_cached_data()
    except FileNotFoundError:
        st.error("File dataset tidak ditemukan. Pastikan Anda telah menjalankan `python main.py` terlebih dahulu.")
        return
    except Exception as e:
        st.error(f"Terjadi kesalahan saat memuat data: {e}")
        return

    # Menggunakan Tabs untuk organisasi yang lebih baik
    tab1, tab2, tab3 = st.tabs(["Distribusi Harga", "Hubungan Fitur", "Statistik Data"])

    with tab1:
        st.subheader("Distribusi Harga Properti per Kecamatan")
        st.write("Visualisasi ini menunjukkan rentang harga di berbagai kecamatan. Kecamatan dengan box yang lebih tinggi cenderung memiliki harga properti yang lebih mahal dan bervariasi.")
        
        # Mengurutkan kecamatan berdasarkan median harga
        if not df.empty:
            median_harga = df.groupby('Kecamatan')['Harga'].median().sort_values(ascending=False)
            
            # --- PERBAIKAN DI SINI ---
            # Mengganti argumen 'order_by' yang salah dengan 'category_orders' yang benar
            fig_dist = px.box(df, 
                             x='Kecamatan', 
                             y='Harga', 
                             color='Kecamatan',
                             category_orders={"Kecamatan": median_harga.index},
                             title="Sebaran Harga Properti di Berbagai Kecamatan Jakarta",
                             labels={'Harga': 'Harga (dalam Rupiah)', 'Kecamatan': 'Kecamatan'})
            fig_dist.update_layout(xaxis_tickangle=-45, showlegend=False)
            st.plotly_chart(fig_dist, use_container_width=True)
        else:
            st.warning("Data tidak tersedia untuk ditampilkan.")

    with tab2:
        st.subheader("Hubungan Antara Fitur dengan Harga")
        st.write("Gunakan pilihan di bawah untuk melihat bagaimana satu fitur berhubungan dengan harga, dengan diwarnai oleh fitur lainnya.")
        
        if not df.empty:
            # Pilihan fitur untuk sumbu x dan warna
            features = ['LT', 'LB', 'KT', 'KM', 'Garasi']
            x_axis = st.selectbox("Pilih Fitur untuk Sumbu X:", features, index=0)
            color_axis = st.selectbox("Pilih Fitur untuk Warna:", [f for f in features if f != x_axis], index=0)
            
            # Gunakan sample jika data terlalu besar untuk performa yang lebih baik
            sample_df = df.sample(min(1000, len(df)), random_state=1)
            
            fig_scatter = px.scatter(sample_df,
                                    x=x_axis, 
                                    y='Harga', 
                                    color=color_axis,
                                    title=f"Hubungan {x_axis} vs Harga, Diwarnai oleh {color_axis}",
                                    labels={'Harga': 'Harga (dalam Rupiah)', x_axis: x_axis},
                                    hover_data=['Kecamatan'])
            st.plotly_chart(fig_scatter, use_container_width=True)
        else:
            st.warning("Data tidak tersedia untuk ditampilkan.")

    with tab3:
        st.subheader("Statistik Deskriptif Dataset")
        st.write("Tabel ini memberikan ringkasan statistik untuk fitur-fitur numerik dalam dataset, seperti rata-rata, standar deviasi, dan nilai minimum/maksimum.")
        if not df.empty:
            st.dataframe(df.describe().style.format("{:,.2f}"), use_container_width=True)
        else:
            st.warning("Data tidak tersedia untuk ditampilkan.")
