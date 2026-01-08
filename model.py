import joblib

MODEL_PATH = "backend/models/production_model.pkl"

def load_model():
    return joblib.load(MODEL_PATH)
