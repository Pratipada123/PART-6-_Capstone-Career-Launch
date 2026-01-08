from fastapi import FastAPI, HTTPException
from schema import PropertyRequest
from model import load_model
from utils import preprocess_input
import uuid
from datetime import datetime

app = FastAPI(
    title="Real Estate Price Prediction API",
    version="1.0.0"
)

model = load_model()

@app.get("/api/v1/health")
def health_check():
    return {"status": "OK", "message": "Service running"}

@app.post("/api/v1/predict")
def predict_price(request: PropertyRequest):
    try:
        if request.area <= 0:
            raise HTTPException(status_code=400, detail="Area must be positive")

        input_df = preprocess_input(request.dict())
        prediction = model.predict(input_df)[0]

        margin = prediction * 0.1

        return {
            "prediction_id": str(uuid.uuid4()),
            "timestamp": datetime.now().isoformat(),
            "predicted_price": round(prediction, 2),
            "currency": "INR",
            "confidence_interval": {
                "lower": round(prediction - margin, 2),
                "upper": round(prediction + margin, 2)
            },
            "model_version": "v1.0"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
