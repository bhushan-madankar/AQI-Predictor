import streamlit as st
import pickle
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Load model and scaler
with open('aqi_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

st.set_page_config(page_title="AQI Predictor", layout="centered")
st.title("Air Quality Index (AQI) Prediction")
st.markdown("Enter the values of pollutants below to predict the AQI level.")

# Features
features = ['CO', 'NH3', 'NO2', 'OZONE', 'PM10', 'PM2.5', 'SO2']

# Input form
user_input = {}
cols = st.columns(3)
for i, feature in enumerate(features):
    with cols[i % 3]:
        user_input[feature] = st.number_input(f"{feature} (µg/m³)", min_value=0.0, max_value=500.0, value=50.0, step=1.0)

# Convert to array and scale
input_data = np.array([[user_input[feature] for feature in features]])
input_data_scaled = scaler.transform(input_data)

# AQI Classification Logic
def classify_aqi(aqi_value):
    if aqi_value <= 50:
        return "Good", "✅ Safe", "green", "Air quality is considered satisfactory."
    elif aqi_value <= 100:
        return "Satisfactory", "✅ Safe", "lime", "Air quality is acceptable. Some pollutants may mildly affect sensitive individuals."
    elif aqi_value <= 200:
        return "Moderate", "⚠ Caution", "orange", "Sensitive groups should reduce prolonged outdoor exertion."
    elif aqi_value <= 300:
        return "Poor", "❌ Unhealthy", "red", "Limit outdoor activities. Sensitive groups at risk."
    elif aqi_value <= 400:
        return "Very Poor", "❌ Very Unhealthy", "darkred", "Avoid outdoor activity. Health effects likely."
    else:
        return "Severe", "❌ Hazardous", "maroon", "Emergency conditions. Everyone may be affected."

# Display AQI Scale
def display_aqi_scale():
    st.subheader("AQI Category Scale")
    colors = ['green', 'lime', 'orange', 'red', 'darkred', 'maroon']
    levels = ['Good (0–50)', 'Satisfactory (51–100)', 'Moderate (101–200)',
              'Poor (201–300)', 'Very Poor (301–400)', 'Severe (401–500)']
    patches = [mpatches.Patch(color=colors[i], label=levels[i]) for i in range(len(colors))]
    fig, ax = plt.subplots()
    ax.axis('off')
    ax.legend(handles=patches, loc='center', fontsize=10)
    st.pyplot(fig)

# Predict Button
if st.button("Predict AQI"):
    predicted_aqi = model.predict(input_data_scaled)[0]
    category, message, color, recommendation = classify_aqi(predicted_aqi)

    st.markdown(f"### Predicted AQI: {predicted_aqi:.2f}")
    st.markdown(f"*Category*: {category}")
    st.markdown(f"<span style='color:{color}; font-size:18px;'>{message}</span>", unsafe_allow_html=True)
    st.markdown(f"*Health Recommendation:* {recommendation}")

    display_aqi_scale()

st.markdown("---")
st.markdown("<div style='text-align: center; font-size: 14px;'>Made with love by <b>Bhushan</b></div>", unsafe_allow_html=True)