import torch
import torch.nn as nn
import joblib
import pandas as pd

scaler = joblib.load("app/models/scaler.pkl")


class FraudNet(nn.Module):
    def __init__(self, input_dim):
        super(FraudNet, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(input_dim, 32),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(32, 16),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(16, 1),
            nn.Sigmoid()
        )

    def forward(self, x):
        return self.model(x)


def load_model(model_path: str):
    model = FraudNet(input_dim=29)
    model.load_state_dict(torch.load(
        model_path,
        map_location=torch.device('cpu')
    ))
    model.eval()
    return model


def predict_fraud(model, features: dict) -> dict:
    df = pd.DataFrame([features])  # preserves column names
    scaled = scaler.transform(df)
    input_tensor = torch.tensor(scaled, dtype=torch.float32)
    with torch.no_grad():
        output = model(input_tensor)
        prob = output.item()
        prediction = int(prob > 0.5)
        return {
            "fraud_probability": round(prob, 4),
            "prediction": prediction,
            "label": "Fraud" if prediction == 1 else "Not Fraud"
        }
