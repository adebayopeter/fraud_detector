# Use Python 3.12 as base
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# System dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy app
COPY . .

# Expose app port
EXPOSE 8000

# Run API
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000"]
