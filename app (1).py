
import streamlit as st
import numpy as np
import pickle

# Load model and scaler
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

st.title("🌿 Plant Health Monitoring App")

st.write("Enter plant parameters below to predict if the plant is healthy.")

temperature = st.number_input("🌡️ Temperature (°C)", min_value=0.0, step=0.1)
humidity = st.number_input("💧 Humidity (%)", min_value=0.0, step=0.1)
soil_moisture = st.number_input("🌱 Soil Moisture (%)", min_value=0.0, step=0.1)
soil_ph = st.number_input("🧪 Soil pH", min_value=0.0, step=0.1)
nutrient = st.selectbox("🧬 Nutrient Level", ['Low', 'Medium', 'High'])
light_intensity = st.number_input("🔆 Light Intensity (lux)", min_value=0.0, step=1.0)

# Encode categorical feature
nutrient_map = {'Low': 0, 'Medium': 1, 'High': 2}
nutrient_encoded = nutrient_map[nutrient]

# Make prediction
if st.button("Check Plant Health"):
    features = np.array([[temperature, humidity, soil_moisture, soil_ph, nutrient_encoded, light_intensity]])
    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)
    result = "✅ Healthy" if prediction[0] == 1 else "⚠️ Unhealthy"
    st.success(f"Prediction: {result}")
