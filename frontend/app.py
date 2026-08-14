import streamlit as st
import pandas as pd
import requests

# Backend URL (Docker Compose will replace this with the backend service name)
BACKEND_URL = "http://backend:5000"

st.set_page_config(page_title="SuperKart Price Predictor", layout="wide")

st.title("🚀 SuperKart Regression Model — Price Prediction UI")
st.write("Enter features manually or upload a CSV for batch predictions.")

# -----------------------------
# SINGLE PREDICTION
# -----------------------------
st.header("🔹 Single Prediction")

# Replace these with your actual model features
feature_names = [
    "feature_1", "feature_2", "feature_3",
    "feature_4", "feature_5"
]

inputs = []
for name in feature_names:
    val = st.number_input(f"{name}", value=0.0)
    inputs.append(val)

if st.button("Predict Price"):
    try:
        response = requests.post(
            f"{BACKEND_URL}/predict",
            json={"features": inputs}
        )
        result = response.json()
        st.success(f"Predicted Price: **{result['prediction']}**")
    except Exception as e:
        st.error(f"Error: {e}")

# -----------------------------
# BATCH PREDICTION
# -----------------------------
st.header("🔹 Batch Prediction (CSV Upload)")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("📄 Uploaded Data:")
    st.dataframe(df)

    if st.button("Predict Batch"):
        try:
            files = {"file": uploaded_file}
            response = requests.post(f"{BACKEND_URL}/predict_batch", files=files)
            results = response.json()

            result_df = pd.DataFrame(results)
            st.write("📊 Predictions:")
            st.dataframe(result_df)

        except Exception as e:
            st.error(f"Error: {e}")
