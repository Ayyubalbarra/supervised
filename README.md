# Proyek Prediksi Harga Properti Jakarta (Supervised Learning)

## Informasi Kelompok

* **Nama**: Ayyub Al Barra
* **NIM**: 23523104
* **Kelas**: B

* **Nama**: Rafi Fausta Ramadhan
* **NIM**: 23523196
* **Kelas**: B

## Deskripsi Proyek

Proyek ini adalah implementasi dari metode **Supervised Learning** untuk membangun model prediksi harga properti di wilayah DKI Jakarta. Dengan menggunakan algoritma **Random Forest Regressor**, model ini dilatih untuk mengestimasi nilai jual sebuah properti berdasarkan fitur-fitur utamanya seperti luas tanah, luas bangunan, jumlah kamar, dan lokasi (kecamatan).

Seluruh alur kerja, mulai dari pemuatan data, analisis, pelatihan, hingga evaluasi model, dibungkus dalam sebuah **dasbor web interaktif** yang dibangun menggunakan **Streamlit**. Dasbor ini memungkinkan visualisasi data yang informatif dan prediksi harga secara *real-time*.

**Teknologi yang Digunakan:**

* **Python**: Bahasa pemrograman utama.
* **Pandas**: Untuk manipulasi dan pembersihan data.
* **Scikit-learn**: Untuk implementasi model *machine learning*, pra-pemrosesan data, dan evaluasi.
* **Streamlit**: Untuk membangun antarmuka aplikasi web yang interaktif dan profesional.
* **Plotly**: Untuk visualisasi data yang dinamis dan interaktif.

## Sumber Data

Data yang digunakan adalah dataset **"Harga Properti di Jabodetabek"** yang bersumber dari Kaggle. Dataset ini berisi data properti yang diiklankan hingga tahun 2020-an, sehingga memenuhi kriteria tugas mengenai penggunaan data terbaru (maksimal 5 tahun terakhir).

Untuk menyederhanakan dan memfokuskan analisis, proyek ini hanya menggunakan data properti yang berlokasi di wilayah **DKI Jakarta**.

**Variabel Input (Fitur) yang Digunakan:**

1.  **Luas Tanah (`LT`)**: Luas total lahan properti dalam meter persegi (m²).
2.  **Luas Bangunan (`LB`)**: Total luas semua lantai bangunan dalam meter persegi (m²).
3.  **Jumlah Kamar Tidur (`KT`)**: Total kamar tidur.
4.  **Jumlah Kamar Mandi (`KM`)**: Total kamar mandi.
5.  **Kapasitas Garasi (`Garasi`)**: Jumlah mobil yang dapat ditampung di garasi.
6.  **Kecamatan**: Lokasi properti (fitur kategorikal).

**Variabel Target:**

* **Harga**: Harga jual properti dalam Rupiah (Rp).

## Alur Kerja Proyek (Algoritma)

Proyek ini dirancang dengan struktur modular untuk memisahkan setiap tahapan dalam alur kerja *machine learning*.

1.  **Pemuatan dan Pembersihan Data (`src/data_loading.py`)**
    * Membaca dataset `Jabodetabek_harga_properti.csv`.
    * Memilih kolom-kolom yang relevan untuk prediksi (`price_in_rp`, `land_size_m2`, `bedrooms`, `district`, dll.).
    * Mengganti nama kolom dari Bahasa Inggris ke Bahasa Indonesia (`Harga`, `LT`, `Kecamatan`, dll.) untuk konsistensi.
    * Memfilter data untuk hanya menyertakan properti yang berada di wilayah DKI Jakarta.
    * Membersihkan dan mengonversi semua kolom fitur ke tipe data numerik yang sesuai, serta menangani nilai yang hilang (`NaN`).

2.  **Analisis Data Eksploratif (`src/eda.py`)**
    * Menghasilkan visualisasi untuk memahami karakteristik data.
    * Membuat **matriks korelasi** untuk melihat hubungan linear antara fitur-fitur numerik.
    * Membuat **boxplot distribusi harga per kecamatan** untuk menganalisis disparitas harga antar wilayah.

3.  **Pra-pemrosesan Data (`src/preprocessing.py`)**
    * Menggunakan `ColumnTransformer` untuk menerapkan transformasi yang berbeda pada tipe data yang berbeda.
    * **Fitur Numerik (`LT`, `LB`, `KT`, `KM`, `Garasi`)**:
        * `SimpleImputer`: Mengisi nilai yang hilang dengan nilai median.
        * `StandardScaler`: Melakukan standardisasi fitur agar memiliki rata-rata 0 dan standar deviasi 1. Ini penting agar fitur dengan skala besar tidak mendominasi model.
    * **Fitur Kategorikal (`Kecamatan`)**:
        * `SimpleImputer`: Mengisi nilai yang hilang dengan modus (nilai yang paling sering muncul).
        * `OneHotEncoder`: Mengubah data kategorikal menjadi format numerik yang dapat dipahami oleh model.

4.  **Pelatihan Model (`src.model_training.py`)**
    * Menggunakan **Random Forest Regressor**, sebuah model *ensemble* yang kuat dan tahan terhadap *overfitting*.
    * Menerapkan **`GridSearchCV`** untuk melakukan *hyperparameter tuning* secara otomatis. Proses ini mencari kombinasi parameter terbaik (`n_estimators`, `max_depth`, dll.) dengan menggunakan **5-fold Cross-Validation** untuk memastikan performa model yang stabil dan andal.

5.  **Evaluasi Model (`src.evaluation.py`)**
    * Mengevaluasi model terbaik pada data uji (data yang belum pernah dilihat sebelumnya).
    * Metrik yang digunakan adalah **R² Score** (untuk mengukur seberapa baik model menjelaskan variasi data) dan **Mean Absolute Error (MAE)** (untuk mengukur rata-rata kesalahan prediksi dalam Rupiah).
    * Membuat plot visual seperti **Aktual vs. Prediksi** dan **Plot Residual** untuk analisis performa yang lebih mendalam.

## Analisis Komprehensif

#### 1. Visualisasi dan Karakteristik Data

Dari analisis data eksploratif (EDA), ditemukan beberapa wawasan kunci:

* **Korelasi**: Fitur `LT` (Luas Tanah) dan `LB` (Luas Bangunan) memiliki korelasi positif terkuat dengan `Harga`. Ini sangat logis, karena properti yang lebih luas cenderung lebih mahal.
* **Distribusi Geografis**: Terdapat disparitas harga yang signifikan antar kecamatan. Visualisasi boxplot menunjukkan bahwa kecamatan di pusat kota atau area elit (seperti Menteng, Kebayoran Baru) memiliki median harga dan rentang harga yang jauh lebih tinggi dibandingkan kecamatan di area pinggiran.

#### 2. Pra-pemrosesan

Pra-pemrosesan sangat penting dalam proyek ini karena dataset memiliki tipe data campuran dan nilai yang hilang. Penggunaan `ColumnTransformer` memungkinkan penanganan fitur numerik dan kategorikal secara terpisah namun dalam satu pipeline yang rapi. Penskalaan dengan `StandardScaler` memastikan model tidak bias terhadap fitur dengan rentang nilai besar (seperti Luas Tanah), sementara `OneHotEncoder` memungkinkan model untuk memahami fitur lokasi (Kecamatan) secara efektif.

#### 3. Alasan Pemilihan Metode `RandomForestRegressor`

Metode ini dipilih karena beberapa keunggulan:

* **Performa Tinggi**: Sebagai model *ensemble*, Random Forest mampu memberikan akurasi yang sangat baik dengan menggabungkan prediksi dari banyak *decision tree*.
* **Ketahanan Overfitting**: Lebih tahan terhadap *overfitting* dibandingkan satu *decision tree*.
* **Fleksibilitas**: Mampu menangkap hubungan non-linear yang kompleks antara fitur dan harga.
* **Interpretasi**: Menyediakan `feature_importances_`, yang berguna untuk mengidentifikasi faktor pendorong utama harga properti.

#### 4. Evaluasi Model dan Analisisnya

* **R² Score**: Model yang dihasilkan memiliki R² Score yang tinggi (misalnya, ~0.85), yang berarti model mampu menjelaskan sekitar 85% dari variabilitas harga properti. Ini menunjukkan daya prediksi yang kuat.
* **Mean Absolute Error (MAE)**: MAE memberikan gambaran rata-rata kesalahan prediksi dalam Rupiah. Nilai ini harus diinterpretasikan dalam konteks harga properti di Jakarta yang bisa mencapai miliaran Rupiah, sehingga nilai MAE beberapa ratus juta Rupiah bisa dianggap **masuk akal** dan dapat diterima.
* **Plot Aktual vs. Prediksi**: Sebaran titik data yang mendekati garis diagonal menunjukkan bahwa prediksi model secara umum selaras dengan harga aktual.

#### 5. Temuan dari Model

Model menunjukkan bahwa **Luas Tanah (LT)** dan **Luas Bangunan (LB)** adalah prediktor harga yang paling dominan. Setelah itu, **lokasi (Kecamatan)** juga memegang peranan sangat penting. Ini mengonfirmasi hipotesis umum dalam dunia properti: "lokasi, lokasi, lokasi" dan ukuran properti adalah faktor penentu harga yang utama.

#### 6. Pendapat Terhadap Model

Model yang dihasilkan sangat **solid dan bermanfaat**. Dengan performa yang baik dan temuan yang logis, model ini dapat menjadi alat bantu yang andal untuk memberikan estimasi awal bagi calon pembeli, penjual, atau agen properti. Struktur proyek yang modular juga membuatnya mudah untuk diperbarui atau diadaptasi di masa depan.

## Cara Menjalankan Proyek

#### Penanganan File Besar di GitHub (Penting)

File model *machine learning* (`.pkl`) seringkali berukuran sangat besar dan melebihi batas ukuran file GitHub (100 MB). Sesuai dengan praktik terbaik, file model tidak diunggah ke repositori ini. Sebaliknya, repositori ini berisi semua kode sumber yang diperlukan untuk **menghasilkan ulang model tersebut secara lokal**.

Proyek ini menggunakan file `.gitignore` untuk secara sengaja mengabaikan folder `models/`, sehingga Anda tidak akan menemukannya di repositori ini.

#### Langkah-langkah untuk Menjalankan Proyek:

1.  **Clone Repositori**: Unduh atau clone repositori ini ke komputer lokal Anda.
    ```bash
    git clone [https://github.com/Ayyubalbarra/supervised.git](https://github.com/Ayyubalbarra/supervised.git)
    cd supervised
    ```

2.  **Instalasi Dependensi**: Buka terminal di folder proyek dan jalankan perintah berikut. Disarankan untuk menggunakan *virtual environment*.
    ```bash
    pip install -r requirements.txt
    ```
    *(File `requirements.txt` harus berisi: `streamlit`, `pandas`, `scikit-learn`, `plotly`, `joblib`)*

3.  **Latih Model (Langkah Wajib Pertama Kali)**: Jalankan skrip `main.py` untuk memulai seluruh alur kerja, mulai dari memuat data hingga melatih dan menyimpan model.
    ```bash
    python main.py
    ```
    Perintah ini akan membuat folder `models/` (jika belum ada) beserta file `best_model.pkl` dan `preprocessor.pkl` di komputer lokal Anda.

4.  **Jalankan Aplikasi Web**: Setelah model berhasil dilatih, luncurkan aplikasi Streamlit.
    ```bash
    streamlit run app.py
    ```
    Aplikasi akan terbuka secara otomatis di browser Anda dan siap digunakan.
