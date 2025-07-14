import matplotlib.pyplot as plt
import seaborn as sns
from config import RESULTS_PATH
import os

def perform_eda(df):
    """Lakukan eksplorasi data pada dataset harga properti Jakarta."""
    # 1. Statistik dasar
    print("Informasi Dataset:")
    df.info()
    print("\nStatistik Deskriptif:")
    print(df.describe())
    
    # 2. Matriks korelasi
    plt.figure(figsize=(10, 7))
    # Hanya hitung korelasi untuk kolom numerik
    corr = df[['Harga', 'LT', 'LB', 'KT', 'KM', 'Garasi']].corr()
    sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm')
    plt.title('Matriks Korelasi Fitur Properti')
    plt.savefig(os.path.join(RESULTS_PATH, "correlation_matrix.png"))
    plt.close()
    
    # 3. Distribusi harga per kecamatan (menggantikan plot geografis)
    plt.figure(figsize=(15, 8))
    # Urutkan kecamatan berdasarkan median harga untuk visualisasi yang lebih baik
    order = df.groupby('Kecamatan')['Harga'].median().sort_values(ascending=False).index
    sns.boxplot(x='Kecamatan', y='Harga', data=df, order=order)
    plt.xticks(rotation=90)
    plt.title('Distribusi Harga Properti per Kecamatan di Jakarta')
    plt.ylabel('Harga (dalam Miliar Rupiah)')
    plt.xlabel('Kecamatan')
    plt.tight_layout()
    plt.savefig(os.path.join(RESULTS_PATH, "harga_per_kecamatan.png"))
    plt.close()
    
    print("Analisis Data Eksploratif (EDA) selesai. Plot disimpan di folder 'results/'.")
    return df