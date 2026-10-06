import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="Sales Predictor", page_icon="📈")

st.title("📈 Simple Sales Predictor")
st.write("A basic Streamlit app for practicing GitHub and deployment.")

# Load dataset
df = pd.read_csv("sales_data.csv")

st.subheader("Dataset")
st.dataframe(df, use_container_width=True)

# Train a simple model
X = df[["advertising_spend"]]
y = df["sales"]

model = LinearRegression()
model.fit(X, y)

st.subheader("Predict Sales")

spend = st.number_input(
    "Enter advertising spend:",
    min_value=0.0,
    max_value=500.0,
    value=100.0,
    step=5.0
)

if st.button("Predict"):
    prediction = model.predict([[spend]])[0]
    st.success(f"Predicted sales: {prediction:.2f}")

st.caption("Practice project — built with Streamlit and scikit-learn.")
