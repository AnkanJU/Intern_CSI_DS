import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load trained model
model = joblib.load("iris_model.pkl")

st.title("🌸 Iris Flower Prediction App")

# Input sliders
sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.1)
sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.5)
petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 1.4)
petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 0.2)

# Predict
if st.button("Predict"):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_data)[0]
    class_map = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}

    st.success(f"Predicted Iris Class: {prediction} ({class_map[prediction]})")

    # Show prediction probabilities
    st.subheader("Prediction Probabilities")
    proba = model.predict_proba(input_data)[0]
    st.bar_chart(proba)
