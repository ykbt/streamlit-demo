import streamlit as st
import pandas as pd

df = pd.read_csv("curry.csv", header=0)

st.map(df)