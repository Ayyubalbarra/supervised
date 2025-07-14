import matplotlib
matplotlib.use('Agg')

from src.data_loading import load_data
from src.eda import perform_eda
from src.preprocessing import preprocess_data
from src.model_training import train_models
from src.evaluation import evaluate_model
import joblib
import os
import sys

def main():
    print("Memulai proyek prediksi harga properti Jakarta...")
    
    try:
        print("\nLangkah 1: Memuat data...")
        df = load_data()
        
        print("\nLangkah 2: Melakukan eksplorasi data...")
        perform_eda(df)
        
        print("\nLangkah 3: Melakukan pra-pemrosesan data...")
        X_train, X_test, y_train, y_test, preprocessor = preprocess_data(df)
        
        joblib.dump(preprocessor, os.path.join("models", "preprocessor.pkl"))
        print("Preprocessor disimpan di models/preprocessor.pkl")
        
        print("\nLangkah 4: Melatih model...")
        models, best_model = train_models(X_train, y_train)
        
        print("\nLangkah 5: Mengevaluasi model terbaik...")
        metrics = evaluate_model(best_model, X_test, y_test, "Model Terbaik")
        
        print("\nProyek berhasil diselesaikan!")
        print(f"R² Score: {metrics['R2']:.4f}")
        print(f"Mean Absolute Error (MAE): Rp {metrics['MAE']:,.0f}")
        
    except Exception as e:
        print(f"\nTerjadi kesalahan: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()