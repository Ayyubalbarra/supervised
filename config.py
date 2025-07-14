import os

# Direktori dasar
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Konfigurasi path
DATA_PATH = os.path.join(BASE_DIR, "data/")
MODELS_PATH = os.path.join(BASE_DIR, "models/")
RESULTS_PATH = os.path.join(BASE_DIR, "results/")

# Buat folder jika belum ada
os.makedirs(DATA_PATH, exist_ok=True)
os.makedirs(MODELS_PATH, exist_ok=True)
os.makedirs(RESULTS_PATH, exist_ok=True)

# Parameter model
RANDOM_STATE = 42
TEST_SIZE = 0.2