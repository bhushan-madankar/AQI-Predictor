# AQI-Predictor

Engineered a real-time AQI prediction web app using Machine Learning, Streamlit, and Plotly, enhancing accessibility to air quality insights.

# Air Quality Index (AQI) Prediction App

A web-based Streamlit application to predict the _Air Quality Index (AQI)_ based on various pollutant concentrations using a _Linear Regression model_.

This project helps users understand the AQI of an area by inputting pollutant values, visualizes predictions, and promotes awareness of air quality issues.

---

## 🚀 Features

- Predict AQI based on real pollutant values
- Beautiful, interactive Streamlit dashboard
- Visualize AQI levels with bar chart
- Input form for user-friendly prediction
- Built with Linear Regression
- Easy deployment on Streamlit Cloud

---

## 📊 Model & Data

- _Model_: Linear Regression (Scikit-Learn)
- _Scaler_: StandardScaler for normalization
- _Dataset_: Central Pollution Control Board (CPCB) AQI data
- _Target Variable_: AQI (Air Quality Index)

---

## 📦 Files in the Repository

| File             | Description              |
| ---------------- | ------------------------ |
| aqi_app.py       | Main Streamlit app       |
| aqi_model.pkl    | Trained ML model         |
| scaler.pkl       | Fitted StandardScaler    |
| requirements.txt | Required Python packages |
| README.md        | Project documentation    |

---

## 🔧 How to Run Locally

1. _Clone the repository:_
   ```bash
   git clone https://github.com/yourusername/aqi-predictor.git
   cd aqi-predictor
   pip install -r requirements.txt
   ```
