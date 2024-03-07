import io

import duckdb
import pandas as pd
import streamlit as st

st.write(
    """
# SQL SRS
Spaced Repetition System SQL Practice
         """
)

with st.sidebar:
    option = st.selectbox(
        "What would you like to review?",
        ["Joins", "GroupBy", "Window Functions"],
        index=None,
        placeholder="Select a theme...",
    )
    st.write("You selected: ", option)

CSV = """
beverage, price
orange juice, 2.5
Expresso, 2
Tea, 3
"""
beverages = pd.read_csv(io.StringIO(CSV))

CSV2 = """
food_item, food_price
cookie, 2.5
chocolatine, 2
muffin, 3
"""
food_items = pd.read_csv(io.StringIO(CSV2))

ANSWER = """
SELECT * FROM beverages
CROSS JOIN food_items
"""
solution = duckdb.sql(ANSWER).df()

st.header("enter your code:")
query = st.text_area(label="Votre code SQL ici", key="user_input")
if query:
    result = duckdb.sql(query).df()
    st.dataframe(result)

    try:
        result = result[solution.columns]
        st.dataframe(result.compare(solution))
    except KeyError as e:
        st.write("Some columns are missing")

    n_lines_diff = result.shape[0] - solution.shape[0]
    if n_lines_diff != 0:
        st.write(f"result has {n_lines_diff} lines difference with solution")


tab2, tab3 = st.tabs(["Tables", "Solutions"])

with tab2:
    st.write("table: beverages")
    st.dataframe(beverages)
    st.write("table: food_items")
    st.dataframe(food_items)
    st.write("table: expected")
    st.dataframe(solution)

with tab3:
    st.write(ANSWER)
