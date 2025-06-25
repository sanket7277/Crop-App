import streamlit as st
import pandas as pd
import joblib

model = joblib.load('model.pkl')
le = joblib.load('label_encoder.pkl')

st.title("🌱 Smart Crop Suggestion")


N = st.number_input("Nitrogen (N)", 0, 150)
P = st.number_input("Phosphorus (P)", 0, 150)
K = st.number_input("Potassium (K)", 0, 150)
Temperature = st.number_input("Temperature (°C)", 10.0, 50.0)
Humidity = st.number_input("Humidity (%)", 10.0, 100.0)
ph = st.number_input("pH", 3.5, 9.5)
Rainfall = st.number_input("Rainfall (mm)", 0.0, 1000.0)
Latitude = st.number_input("Latitude", -90.0, 90.0)
Longitude = st.number_input("Longitude", -180.0, 180.0)


if st.button("Suggest Crop"):
    input_data = pd.DataFrame([[N, P, K, Temperature, Humidity, ph, Rainfall, Latitude, Longitude]],
                              columns=['N', 'P', 'K', 'Temperature', 'Humidity', 'pH', 'Rainfall', 'Latitude', 'Longitude'])
    prediction = model.predict(input_data)
    crop = le.inverse_transform(prediction)[0]
    st.success(f"✅ Recommended Crop: **{crop}**")
