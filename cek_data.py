import pandas as pd
import os

DATA_FILE = os.path.join("data", "Jabodetabek_harga_properti.csv")

print(f"--- Mengecek file: {DATA_FILE} ---")

if not os.path.exists(DATA_FILE):
    print("\nERROR: File tidak ditemukan! Pastikan file ada di folder 'data' dan nama sudah benar.")
else:
    print("\n--- Percobaan 1: Membaca dengan pemisah KOMA (,) ---")
    try:
        df_comma = pd.read_csv(DATA_FILE, sep=',')
        print("Kolom yang terdeteksi:")
        print(list(df_comma.columns))
        print("\n5 baris pertama:")
        print(df_comma.head())
    except Exception as e:
        print(f"Gagal membaca dengan koma: {e}")

    print("\n" + "="*50 + "\n")

    print("--- Percobaan 2: Membaca dengan pemisah TITIK KOMA (;) ---")
    try:
        df_semicolon = pd.read_csv(DATA_FILE, sep=';')
        print("Kolom yang terdeteksi:")
        print(list(df_semicolon.columns))
        print("\n5 baris pertama:")
        print(df_semicolon.head())
    except Exception as e:
        print(f"Gagal membaca dengan titik koma: {e}")