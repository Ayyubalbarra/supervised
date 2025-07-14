import matplotlib.pyplot as plt
import numpy as np
import os
from sklearn.metrics import (
    mean_absolute_error, 
    mean_squared_error, 
    r2_score
)
from config import RESULTS_PATH

def evaluate_model(model, X_test, y_test, model_name="Model"):
    """Evaluasi performa model dan buat visualisasi."""
    # 1. Buat prediksi
    y_pred = model.predict(X_test)
    
    # 2. Hitung metrik
    metrics = {
        'R2': r2_score(y_test, y_pred),
        'MAE': mean_absolute_error(y_test, y_pred),
        'RMSE': np.sqrt(mean_squared_error(y_test, y_pred))
    }
    
    print(f"\n--- Metrik Evaluasi untuk {model_name} ---")
    for metric, value in metrics.items():
        if metric == 'R2':
            print(f"{metric}: {value:.4f}")
        else:
            print(f"{metric}: Rp {value:,.0f}")
    
    # 3. Plot aktual vs prediksi
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred, alpha=0.5, edgecolors='k')
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
    plt.xlabel('Harga Aktual (Rp)')
    plt.ylabel('Harga Prediksi (Rp)')
    plt.title(f'Aktual vs. Prediksi Harga ({model_name})')
    plt.ticklabel_format(style='plain', axis='both')
    plt.savefig(os.path.join(RESULTS_PATH, f"{model_name}_actual_vs_predicted.png"))
    plt.close()
    
    # 4. Plot residual
    residuals = y_test - y_pred
    plt.figure(figsize=(10, 6))
    plt.scatter(y_pred, residuals, alpha=0.5, edgecolors='k')
    plt.hlines(y=0, xmin=y_pred.min(), xmax=y_pred.max(), colors='r', lw=2, linestyles='--')
    plt.xlabel('Harga Prediksi (Rp)')
    plt.ylabel('Residuals (Aktual - Prediksi)')
    plt.title(f'Plot Residual ({model_name})')
    plt.ticklabel_format(style='plain', axis='both')
    plt.savefig(os.path.join(RESULTS_PATH, f"{model_name}_residuals.png"))
    plt.close()
    
    return metrics