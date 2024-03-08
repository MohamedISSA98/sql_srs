import os
import logging
import duckdb
import streamlit as st


if "data" not in os.listdir():
    logging.error(os.listdir())
    logging.error("creating folder data")
    os.mkdir("data")

if "exercices_sql_tables.duckdb" not in os.listdir("data"):
    exec(open("init_db.py").read())

con = duckdb.connect(database="data/exercices_sql_tables.duckdb", read_only=True)

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
    if theme:
        st.write("You selected: ", theme)
        select_exercice_query = f"SELECT * FROM memory_state WHERE theme = '{theme}'"
    else:
        select_exercice_query = "SELECT * FROM memory_state"

    exercice = con.execute(select_exercice_query).df()
    exercice = exercice.sort_values("last_reviewed")

    st.write(exercice)
    exercice_name = exercice.iloc[0]["exercice_name"]
    with open(f"answers/{exercice_name}.sql", "r") as f:
        answer = f.read()

    solution = con.execute(answer).df()


st.header("enter your code:")
query = st.text_area(label="Votre code SQL ici", key="user_input")
if query:
    result = con.execute(query).df()
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
    exercice_tables = exercice.iloc[0]["tables"]
    for table in exercice_tables:
        st.write(f"table: {table}")
        df_table = con.execute(f"SELECT * FROM {table}").df()
        st.dataframe(df_table)


with tab3:

    st.write(answer)
