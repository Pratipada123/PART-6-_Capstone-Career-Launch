import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000/api/v1/predict"

st.set_page_config(page_title="Real Estate Price Predictor", layout="centered")

st.title("🏠 Real Estate Price Prediction System")
st.markdown("Production-ready ML Capstone Project")

st.sidebar.header("Property Details")

area = st.sidebar.number_input("Area (sqft)", 300, 5000, 1200)
bedrooms = st.sidebar.selectbox("Bedrooms", [1,2,3,4,5])
bathrooms = st.sidebar.selectbox("Bathrooms", [1,2,3,4])
age = st.sidebar.number_input("Property Age (years)", 0, 50, 5)
floor = st.sidebar.number_input("Floor", 1, 50, 2)
location = st.sidebar.selectbox("Location", ["Mumbai", "Pune", "Bangalore", "Delhi"])
property_type = st.sidebar.selectbox("Property Type", ["Apartment", "Villa", "Independent"])

if st.button("🔮 Predict Price"):
    payload = {
        "area": area,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "age": age,
        "floor": floor,
        "location": location,
        "property_type": property_type
    }

    response = requests.post(API_URL, json=payload)

    if response.status_code == 200:
        result = response.json()

        st.success("Prediction Successful 🎉")
        st.metric("Estimated Price (INR)", f"₹ {result['predicted_price']:,.0f}")

        st.write("### Confidence Interval")
        st.write(f"₹ {result['confidence_interval']['lower']:,.0f}  -  ₹ {result['confidence_interval']['upper']:,.0f}")

        st.write("### Metadata")
        st.json(result)

    else:
        st.error("Prediction failed")
