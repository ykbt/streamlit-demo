import streamlit as st
import pandas as pd

st.write("""
# Daily Emotion Chart
""")


df = pd.read_csv("emotion.csv", header=0, index_col=0)

print(df)
st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)