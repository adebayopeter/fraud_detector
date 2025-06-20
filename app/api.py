import uvicorn
from fastapi import FastAPI, Depends, HTTPException, Header, status

from app.schemas import TransactionalFeatures, PredictionResponse
from app.predict import load_model, predict_fraud
from app.logger import log_to_postgres
import os

app = FastAPI(
    title="Fraud Detection API",
    description="Real-time fraud prediction using PyTorch model",
    version="1.0"
)

model_path = os.path.join("app/models", "fraud_model.pth")
model = load_model(model_path)
API_KEY = os.getenv("API_KEY")


def verify_api_key(x_api_key: str = Header(...)):
    if not API_KEY:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="API key not configured on server")
    if x_api_key != API_KEY:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid API Key")


@app.post("/api/predict/transaction", response_model=PredictionResponse)
def predict_transaction(payload: TransactionalFeatures, api_key: str = Depends(verify_api_key)):
    features = payload.model_dump()
    result = predict_fraud(model, features)
    log_to_postgres(features, result)
    return result


# Run with: uvicorn app.api:app --reload
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
