import streamlit as st

file = st.file_uploader("Upload CSV")

if file:
    st.success("File Uploaded")