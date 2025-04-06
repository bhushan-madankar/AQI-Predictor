#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import numpy as np
import pickle
import matplotlib.pyplot as plt
import pandas as pd

# Load trained model and scaler
model = pickle.load(open("aqi_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# Define Features (Update as per your model)
features = ["PM2.5", "PM10", "NO2", "SO2", "CO", "O3", "NH3"]

# Streamlit UI
st.set_page_config(page_title="AQI Prediction", page_icon="\U0001F30D", layout="centered")
st.title("🌎 Air Quality Index (AQI) Prediction")
st.markdown("### Enter pollution levels to predict AQI")

# User Input with Text Fields
user_input = {}
col1, col2 = st.columns(2)
for i, feature in enumerate(features):
    if i % 2 == 0:
        user_input[feature] = col1.text_input(f"{feature} (µg/m³)", "50")
    else:
        user_input[feature] = col2.text_input(f"{feature} (µg/m³)", "50")

# Convert input values to float
try:
    input_data = np.array([[float(user_input[feature]) for feature in features]])
    input_data_scaled = scaler.transform(input_data)
    
    if st.button("🚀 Predict AQI"):
        predicted_aqi = model.predict(input_data_scaled)[0]
        st.success(f"Predicted AQI: **{predicted_aqi:.2f}**")
        
        # Visualization - Bar Chart
        df = pd.DataFrame({"Feature": features, "Value": input_data[0]})
        fig, ax = plt.subplots()
        ax.barh(df["Feature"], df["Value"], color="skyblue")
        ax.set_xlabel("Concentration (µg/m³)")
        ax.set_title("Pollutant Levels")
        st.pyplot(fig)
except ValueError:
    st.error("Please enter valid numeric values for all fields.")

# Footer
st.markdown("---")
st.markdown(" Made with ❤️ by Bhushan & Saidhiraj")


# In[ ]:




