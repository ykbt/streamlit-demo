import streamlit as st
import pandas as pd

st.write("""
# Daily Emotion Chart
私がその日感じたエモさ
""")

st.markdown("""
# こんなんとか
### こんなんとか

- いいよいいよ
- それそれ

以下のコードで書いてるよ
```
import streamlit as st
import pandas as pd

df = pd.read_csv("emotion.csv", header=0, index_col=0)
st.line_chart(df)
```
""")


df = pd.read_csv("emotion.csv", header=0, index_col=0)

print(df)

st.write("""
# グラフ集
## 線グラフ
""")
st.line_chart(df)

st.write("## 棒グラフ")
st.bar_chart(df)

st.write("## 面グラフ")
st.area_chart(df)