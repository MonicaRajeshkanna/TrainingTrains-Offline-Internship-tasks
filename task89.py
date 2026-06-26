import streamlit as st

age = st.number_input("Age")

if st.button("Predict"):
    st.write("Prediction Complete")