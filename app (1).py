
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

st.title("🌿 Plant Health Monitoring App")

st.write("Enter plant parameters below to predict if the plant is healthy.")

# Input fields
temperature = st.number_input("🌡️ Temperature (°C)", min_value=0.0, step=0.1)
humidity = st.number_input("💧 Humidity (%)", min_value=0.0, step=0.1)
soil_moisture = st.number_input("🌱 Soil Moisture (%)", min_value=0.0, step=0.1)
soil_ph = st.number_input("🧪 Soil pH", min_value=0.0, step=0.1)
nutrient = st.selectbox("🧬 Nutrient Level", ['Low', 'Medium', 'High'])
light_intensity = st.number_input("🔆 Light Intensity (lux)", min_value=0.0, step=1.0)

# Encode nutrient level
nutrient_map = {'Low': 0, 'Medium': 1, 'High': 2}
nutrient_encoded = nutrient_map[nutrient]

# Train model inside the app using dummy data
@st.cache_resource
def train_model():
    np.random.seed(42)
    data = {
        'Temperature_C': np.random.uniform(15, 35, 100),
        'Humidity_%': np.random.uniform(30, 90, 100),
        'Soil_Moisture_%': np.random.uniform(10, 60, 100),
        'Soil_pH': np.random.uniform(4.5, 8.5, 100),
        'Nutrient_Level': np.random.randint(0, 3, 100),
        'Light_Intensity_lux': np.random.uniform(2000, 10000, 100),
        'Health_Status': np.random.randint(0, 2, 100)
    }
    df = pd.DataFrame(data)
    X = df.drop('Health_Status', axis=1)
    y = df['Health_Status']
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    model = RandomForestClassifier(random_state=42)
    model.fit(X_scaled, y)
    return model, scaler

model, scaler = train_model()

# Prediction
if st.button("Check Plant Health"):
    features = np.array([[temperature, humidity, soil_moisture, soil_ph, nutrient_encoded, light_intensity]])
    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)
    result = "✅ Healthy" if prediction[0] == 1 else "⚠️ Unhealthy"
    st.success(f"Prediction: {result}")
