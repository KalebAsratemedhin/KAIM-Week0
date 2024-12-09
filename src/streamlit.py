import streamlit as st
import pandas as pd

def load_data():
    return pd.read_csv("../data/benin_malanville.csv")

data = load_data()

st.title("Solar Radiation Dashboard")
st.write("### Summary Statistics")
st.write(data.describe())

