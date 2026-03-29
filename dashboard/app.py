import streamlit as st
import requests

st.title("A/B Testing Dashboard")

api_url = "http://localhost:8000/ab-test"
response = requests.get(api_url).json()

st.metric("Conversion A", response["conversion_A"])
st.metric("Conversion B", response["conversion_B"])
st.write("P-value:", response["p_value"])
st.write("Decision:", response["decision"])
