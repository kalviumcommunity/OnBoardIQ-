import streamlit as st
from backend.database.database_utils import fetch_data

st.title("Database Test")

df = fetch_data("SELECT * FROM employees;")

st.dataframe(df)