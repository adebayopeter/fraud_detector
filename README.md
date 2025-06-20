# 🕵️‍♂️ Fraud Detection API + Streamlit Dashboard

This project is a fully containerized machine learning pipeline for real-time credit card fraud detection. It combines a PyTorch model served via FastAPI with a sleek Streamlit UI, all orchestrated using Docker Compose.

## 📚 Table of Contents

- [Overview](#-fraud-detection-api--streamlit-dashboard)
- [Features](#-features)
- [Quick Start](#-quick-start)
  - [1️⃣ Clone the repo](#1️-clone-the-repo)
  - [2️⃣ Create a `.env` file](#2️-create-a-env-file)
  - [3️⃣ Launch with Docker Compose](#3️-launch-with-docker-compose)
- [API Usage](#️-api-usage)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Author](#-author)
- [License](#-license)
- [Contributing](#-want-to-contribute)

---

## 🔧 Features

- ✅ Model inference with FastAPI and PyTorch
- 📊 Streamlit dashboard with default transaction values
- 🛡️ API Key authentication for secure access
- 🐘 PostgreSQL logging with schema migrations
- 🐳 Full Dockerized stack for easy deployment
- 🌱 Clean .env configuration and modular project structure

---
## 🚀 Quick Start
### 1️⃣ Clone the repo

```pycon
git clone https://github.com/adebayopeter/fraud-detector.git
cd fraud-detector
```
### 2️⃣ Create a `.env` file
Use `.env.example` as your template:
```pycon
cp .env.example .env
```
Set values for:
```pycon
DB_TYPE=postgres
DB_HOST=db 
DB_USER=db_user
DB_PASSWORD=db_password
DB_NAME=db_name

BASE_URL=http://api:8000

API_KEY=API_KEY_HERE
```

### 3️⃣ Launch with Docker Compose
```pycon
docker compose up --build

# create database table
docker compose exec api python init_db.py
```
- Streamlit UI → http://localhost:8501
- FastAPI → http://localhost:8000/docs
- PostgreSQL database logs predictions
---

## ✉️ API Usage

Make a POST request to:
```pycon
POST /api/predict/transaction
```
Headers:
```pycon
x-api-key: your_api_key
```
Payload:
```pycon
{
  "V1": -1.3598071336738,
  "V2": 1.19185711131486,
  "V3": -0.358044855,
  "V4": 1.082,
  "V5": -0.385,
  "V6": 0.8777,
  "V7": 0.2151,
  "V8": -0.689,
  "V9": 1.1911,
  "V10": -0.635,
  "V11": 1.3771,
  "V12": -0.293,
  "V13": 0.389,
  "V14": -0.142,
  "V15": 0.935,
  "V16": -0.144,
  "V17": -0.168,
  "V18": 0.278,
  "V19": 0.403,
  "V20": -0.008,
  "V21": 0.261,
  "V22": 0.644,
  "V23": 0.101,
  "V24": -0.493,
  "V25": 0.009,
  "V26": 0.050,
  "V27": 0.104,
  "V28": 0.405,
  "Amount": 149.62
}

```
Response:
```pycon
{
  "fraud_probability": 0.9214,
  "prediction": 1,
  "label": "Fraud"
}
```
---
### 🛠 Tech Stack
- **FastAPI** — for scalable ML inference API
- **Streamlit** — for beautiful and interactive UI
- **PyTorch** — powering the binary classification model
- **PostgreSQL** — backend database for logging predictions
- **Docker Compose** — portable environment setup
- **python-dotenv** — for environment variable management
---

## 📂 Project Structure
```
📦 fraud_detector/
├─ app/
│  └─ models/
│    └─ fraud_model.pth
│    └─ scaler.pkl
│  ├─ api.py
│  └─ logger.py
│  └─ predict.py
│  └─ schemas.py
│  /azureml
│  ├─ training_pipeline.yml
├─ data/
│  └─ processed/
│    └─ X_test.npy
│    └─ X_train.npy
│    └─ y_test.npy
│    └─ X_train.npy
│  └─ creditcard.csv
├─ db/
│  └─ schema.sql
│ notebooks/
│  └─ 01_data_cleaning.ipynb
│  └─ 02_model_training.ipynb
├─ .gitignore
├─ docker-composer.yml
├─ Dockerfile
├─ Dockerfile.streamlit
├─ init_db.py
├─ nginx.conf
├─ README.md
├─ requirements.txt
└─ streamlit_app.py
```
---
## 🧠 Author
👤 Adebayo Olaonipekun Senior Data Analyst & ML Engineer | [LinkedIn](https://www.linkedin.com/in/adebayo-olaonipekun/)

---

## 📃 License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE)file for details.

## 🤝 Contributing
Pull requests are welcome! Feel free to fork this project, improve styling, add new features, or explore deployment integrations (e.g., Render, Azure, or Railway).

---