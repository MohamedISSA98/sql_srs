import streamlit as st
import pandas as pd
import duckdb

st.write('Hello world!')
data = {"a":[1, 2, 3], "b":[4, 5, 6]}
df = pd.DataFrame(data)

query = st.text_area(label='Entrez votre input')
res = duckdb.query(query).df()
st.dataframe(df)
st.write(res)