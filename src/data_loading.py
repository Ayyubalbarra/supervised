import pandas as pd
import os

# Nama file dataset
DATA_FILE = os.path.join("data", "Jabodetabek_harga_properti.csv")

def load_data():
    """Memuat dan membersihkan dataset harga properti Jabodetabek."""
    if not os.path.exists(DATA_FILE):
        raise FileNotFoundError(f"Dataset tidak ditemukan di '{DATA_FILE}'.")

    # 1. Baca file dengan separator KOMA (,)
    df = pd.read_csv(DATA_FILE, sep=',')

    # 2. Definisikan nama kolom ASLI dari file CSV yang akan digunakan
    original_cols = [
        'price_in_rp', 
        'land_size_m2', 
        'building_size_m2', 
        'bedrooms', 
        'bathrooms', 
        'garages', 
        'district',
        'city' # Kita butuh kolom city untuk memfilter Jakarta
    ]
    df = df[original_cols]

    # 3. Ganti nama kolom ke format Bahasa Indonesia agar konsisten
    rename_map = {
        'price_in_rp': 'Harga',
        'land_size_m2': 'LT',
        'building_size_m2': 'LB',
        'bedrooms': 'KT',
        'bathrooms': 'KM',
        'garages': 'Garasi',
        'district': 'Kecamatan'
    }
    df.rename(columns=rename_map, inplace=True)
    
    # 4. Fokus pada data Jakarta saja
    # Menggunakan contains 'Jakarta' untuk mencakup semua wilayah Jakarta
    df = df[df['city'].str.contains("Jakarta", na=False)].copy()
    df.drop(columns=['city'], inplace=True) # Hapus kolom city setelah filtering

    # 5. Hapus baris dengan data kosong/null
    df.dropna(inplace=True)
    
    # 6. Pastikan tipe data numerik sudah benar
    numeric_cols = ['Harga', 'LT', 'LB', 'KT', 'KM', 'Garasi']
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    
    df.dropna(inplace=True) # Hapus lagi jika ada null setelah konversi

    # 7. Hapus data yang tidak masuk akal (opsional, tapi baik untuk kualitas model)
    df = df[df['Harga'] > 100_000_000] # Harga di atas 100 juta
    df = df[df['LT'] > 10]
    df = df[df['LB'] > 10]

    print("Dataset Harga Properti Jakarta berhasil dimuat dan dibersihkan.")
    print(f"Jumlah data yang akan digunakan: {len(df)} baris.")
    
    return df