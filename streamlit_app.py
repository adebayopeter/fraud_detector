import streamlit as st
import requests
from dotenv import load_dotenv
import os

load_dotenv()
BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")
headers = {"x-api-key": os.getenv("API_KEY")}

st.set_page_config(page_title="Fraud Detector", page_icon="🕵️‍♂️", layout="wide")

st.title("🔍 Real-Time Fraud Detection")
st.markdown("Enter transaction features below. The model will assess fraud risk based on the inputs.")

with st.container():
    st.subheader("📊 Transaction Features")

    default_values = [
        -1.3598071336738, 1.19185711131486, -0.358044855, 1.082, -0.385,
        0.8777, 0.2151, -0.689, 1.1911, -0.635, 1.3771, -0.293, 0.389, -0.142,
        0.935, -0.144, -0.168, 0.278, 0.403, -0.008, 0.261, 0.644, 0.101,
        -0.493, 0.009, 0.050, 0.104, 0.405, 149.62
    ]

    feature_columns = [f"V{i}" for i in range(1, 29)] + ["Amount"]
    features = {}

    cols = st.columns(3)
    for i, col_name in enumerate(feature_columns):
        with cols[i % 3]:
            val = st.number_input(
                label=col_name,
                value=default_values[i],
                key=col_name,
                format="%.6f"
            )
            features[col_name] = val

st.divider()

if st.button("🚀 Predict Transaction"):
    payload = features
    with st.spinner("Analyzing..."):
        try:
            response = requests.post(f"{BASE_URL}/api/predict/transaction", json=payload, headers=headers)
            if response.status_code == 200:
                result = response.json()
                st.success(f"🎯 Prediction: {result['label']}")
                st.metric("Fraud Probability", f"{result['fraud_probability']:.4f}")
            else:
                st.error(f"❌ Server responded with: {response.status_code}")
        except Exception as e:
            st.error(f"⚠️ Could not connect to API: {e}")
