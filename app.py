import streamlit as st

con = duckdb.connect(database="data/exercices_sql_tables.duckdb", read_only=False)

st.write(
    """
# SQL SRS
Spaced Repetition System SQL Practice
         """
)

with st.sidebar:
    theme = st.selectbox(
        "What would you like to review?",
        ["Joins", "GroupBy", "Window Functions"],
        index=None,
        placeholder="Select a theme...",
    )
    st.write("You selected: ", theme)

    exercice = con.execute(f"SELECT * FROM memory_state WHERE theme = '{theme}'").df()
    st.write(exercice)

st.header("enter your code:")
query = st.text_area(label="Votre code SQL ici", key="user_input")
# if query:
#     result = duckdb.sql(query).df()
#     st.dataframe(result)

#     try:
#         result = result[solution.columns]
#         st.dataframe(result.compare(solution))
#     except KeyError as e:
#         st.write("Some columns are missing")

#     n_lines_diff = result.shape[0] - solution.shape[0]
#     if n_lines_diff != 0:
#         st.write(f"result has {n_lines_diff} lines difference with solution")


# tab2, tab3 = st.tabs(["Tables", "Solutions"])

# with tab2:
#     st.write("table: beverages")
#     st.dataframe(beverages)
#     st.write("table: food_items")
#     st.dataframe(food_items)
#     st.write("table: expected")
#     st.dataframe(solution)

# with tab3:
#     st.write(ANSWER)
