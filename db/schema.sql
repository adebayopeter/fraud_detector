CREATE TABLE IF NOT EXISTS predictions (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    features JSONB,
    fraud_probability FLOAT,
    prediction INT,
    label TEXT
);
