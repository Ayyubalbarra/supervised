import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def calculate_metrics(y_true, y_pred):
    """Calculate evaluation metrics"""
    return {
        'MAE': mean_absolute_error(y_true, y_pred),
        'RMSE': np.sqrt(mean_squared_error(y_true, y_pred)),
        'R2': r2_score(y_true, y_pred)
    }

def plot_residuals(y_true, y_pred):
    """Create residual plot"""
    residuals = y_true - y_pred
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(residuals, kde=True, ax=ax)
    ax.set_title('Residual Distribution')
    ax.set_xlabel('Residuals')
    return fig