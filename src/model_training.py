from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import make_scorer, mean_absolute_error
import joblib
from config import MODELS_PATH, RANDOM_STATE
import os

def train_models(X_train, y_train):
    """Latih dan tuning model RandomForestRegressor."""
    
    print("Memulai tuning hyperparameter dengan GridSearchCV...")
    
    # Penalaan hiperparameter
    param_grid = {
        'n_estimators': [100, 200],
        'max_depth': [10, 20, None],
        'min_samples_split': [2, 5],
        'min_samples_leaf': [1, 2]
    }
    
    grid_search = GridSearchCV(
        estimator=RandomForestRegressor(random_state=RANDOM_STATE),
        param_grid=param_grid,
        cv=5, # 5-fold cross-validation
        scoring='neg_mean_absolute_error', # Metrik untuk optimisasi
        n_jobs=-1, # Gunakan semua core CPU
        verbose=2
    )
    
    grid_search.fit(X_train, y_train)
    
    best_model = grid_search.best_estimator_
    
    # Simpan model terbaik
    os.makedirs(MODELS_PATH, exist_ok=True)
    joblib.dump(best_model, os.path.join(MODELS_PATH, "best_model.pkl"))
    
    print(f"Parameter model terbaik: {grid_search.best_params_}")
    print(f"Model terbaik disimpan di {os.path.join(MODELS_PATH, 'best_model.pkl')}")
    
    # Mengembalikan dictionary untuk konsistensi (opsional)
    return {'RandomForest': best_model}, best_model