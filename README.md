# 📈 Retail Forecasting Platform

## Overview

Retail Forecasting Platform is an end-to-end machine learning project designed to analyze retail transaction data, generate sales forecasts, and provide actionable business insights through an interactive dashboard.

The project transforms raw retail transactions into forecasting-ready datasets using data preprocessing, feature engineering, and time-series modeling techniques. Forecasts and analytics are delivered through a Streamlit-based web application.

---

## 🚀 Features

- Automated retail data ingestion
- Data quality validation and cleaning
- Time-series feature engineering
- Daily revenue aggregation
- XGBoost-based forecasting
- Model persistence using Joblib
- Interactive Streamlit dashboard
- Forecast performance monitoring
- Feature importance analysis
- Modular, production-style Python codebase

---

## 🏗️ Architecture

```text
Retail Transaction Data
            │
            ▼
     Data Ingestion
            │
            ▼
   Data Quality Checks
            │
            ▼
   Feature Engineering
            │
            ▼
 Daily Revenue Aggregation
            │
            ▼
 Lag & Rolling Features
            │
            ▼
     XGBoost Model
            │
            ▼
   Forecast Generation
            │
            ▼
   Model Serialization
            │
            ▼
   Streamlit Dashboard
```

---

## 🛠️ Tech Stack

### Programming

- Python

### Data Processing

- Pandas
- NumPy

### Machine Learning

- XGBoost
- Scikit-learn
- Joblib

### Visualization

- Plotly
- Streamlit

### Data Storage

- Supabase

### Development

- Git
- GitHub
- Virtual Environments

---

## 📂 Project Structure

```text
retail-forecast-repo/
│
├── app.py
├── train_model.py
├── daily_sales_features.csv
├── requirements.txt
├── README.md
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── ingest.py
│   ├── quality.py
│   ├── features.py
│   ├── preprocess.py
│   ├── train_xgb.py
│   ├── model_registry.py
│   └── supabase_utils.py
│
├── models/
│   └── xgb_forecast.pkl
│
├── pages/
│   ├── 1_Sales_Analytics.py
│   ├── 2_Forecasting.py
│   └── 3_Model_Metrics.py
│
└── .streamlit/
    └── config.toml
```

---

## 🔄 Data Pipeline

### Data Ingestion

- Load retail transaction dataset
- Validate schema and structure
- Generate raw dataset snapshot

### Data Quality

- Duplicate detection and removal
- Missing value analysis
- Dataset validation checks

### Feature Engineering

Generated forecasting features include:

- Year
- Month
- Week
- Day of Week
- Lag-1 Revenue
- Lag-7 Revenue
- 7-Day Rolling Average
- 30-Day Rolling Average

### Data Aggregation

Individual transactions are aggregated into daily revenue values to support time-series forecasting.

---

## 🤖 Machine Learning Pipeline

### Forecasting Model

**XGBoost Regressor**

The model predicts future sales using engineered temporal and historical revenue features.

### Evaluation Metrics

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

### Model Persistence

Models are saved using Joblib to support reproducibility and deployment without retraining.

---

## 📊 Dashboard Features

### Sales Analytics

- Total Revenue
- Average Daily Revenue
- Peak Revenue
- Revenue Trend Visualization
- Monthly Revenue Analysis

### Forecasting

- Actual vs Predicted Revenue
- Forecast Trends
- Historical Revenue Analysis

### Model Monitoring

- MAE
- RMSE
- R² Score
- Feature Importance Visualization

---

## 📈 Sample Business Use Cases

- Demand Forecasting
- Inventory Planning
- Revenue Trend Analysis
- Business Performance Monitoring
- Operational Decision Support

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/purvasuresh8/retail-forecast-repo.git
cd retail-forecast-repo
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

### macOS/Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🏃 Run the Machine Learning Pipeline

Train and save the forecasting model:

```bash
python train_model.py
```

This will:

- Load engineered features
- Train the XGBoost model
- Evaluate forecasting performance
- Save the trained model

---

## 🌐 Run the Dashboard

Start Streamlit:

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## 📌 Key Learning Outcomes

- Built a modular machine learning pipeline from scratch
- Applied time-series feature engineering techniques
- Developed an XGBoost forecasting model
- Implemented model persistence using Joblib
- Created a multi-page Streamlit analytics application
- Connected data engineering and machine learning workflows into a production-oriented solution

---

## 🔮 Future Enhancements

- MLflow experiment tracking
- Automated model retraining
- Advanced forecasting models (Prophet, LightGBM)
- AI-powered Retail Copilot
- Real-time forecasting APIs
- Cloud deployment
- Forecast storage and retrieval through Supabase

---

## 👩‍💻 Author

**Purva Suresh**

GitHub: https://github.com/purvasuresh8

---

## 📄 License

This project is intended for educational, research, and portfolio purposes.
