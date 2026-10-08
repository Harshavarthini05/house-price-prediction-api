from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import joblib
import pandas as pd
import os

app = FastAPI(title="House Price Prediction API")

# Paths to model and metadata
BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, "model", "house_price_model.joblib")
META_PATH = os.path.join(BASE_DIR, "model", "model_metadata.joblib")

# Load once at startup
model = joblib.load(MODEL_PATH)
meta = joblib.load(META_PATH)


class HouseInput(BaseModel):
    date: str
    bedrooms: int
    bathrooms: float
    sqft_living: float
    sqft_lot: float
    floors: float
    waterfront: int
    view: int
    condition: int
    sqft_above: float
    sqft_basement: float
    yr_built: int
    yr_renovated: int
    street: str
    city: str
    statezip: str
    country: str


@app.post("/predict")
def predict_price(house: HouseInput):
    try:
        row = house.model_dump()  # for Pydantic v2; use .dict() for v1
        df = pd.DataFrame([row])[meta["feature_cols"]]
        pred = float(model.predict(df)[0])
        return {"predicted_price": pred, "currency": "USD"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/")
def root():
    return {
        "service": "House Price Prediction API",
        "endpoints": {
            "predict": "POST /predict"
        }
    }