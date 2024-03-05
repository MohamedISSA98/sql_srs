import streamlit as st
import pandas as pd
import duckdb

st.write("""
# SQL SRS
Spaced Repetition System SQL Practice
         """)

with st.sidebar:
    option = st.selectbox(
        "What would you like to review?",
        ['Joins', 'GroupBy', 'Window Functions'],
        index=None,
        placeholder="Select a theme..."
    )
    st.write("You selected: ", option)

data = {"a":[1, 2, 3], "b":[4, 5, 6]}
df = pd.DataFrame(data)

query = st.text_area(label='Entrez votre input')
res = duckdb.query(query).df()
st.dataframe(df)
st.write(res)