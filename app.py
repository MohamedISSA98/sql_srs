import ast
import duckdb
import streamlit as st

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
    st.write("You selected: ", theme)

    exercice = con.execute(f"SELECT * FROM memory_state WHERE theme = '{theme}'").df()
    # st.write(exercice)

st.header("enter your code:")
query = st.text_area(label="Votre code SQL ici", key="user_input")
if query:
    result = con.execute(query).df()
    st.dataframe(result)

#     try:
#         result = result[solution.columns]
#         st.dataframe(result.compare(solution))
#     except KeyError as e:
#         st.write("Some columns are missing")

#     n_lines_diff = result.shape[0] - solution.shape[0]
#     if n_lines_diff != 0:
#         st.write(f"result has {n_lines_diff} lines difference with solution")


tab2, tab3 = st.tabs(["Tables", "Solutions"])

with tab2:
    exercice_tables = ast.literal_eval(exercice.iloc[0]["tables"])
    for table in exercice_tables:
        st.write(f"table: {table}")
        df_table = con.execute(f"SELECT * FROM {table}").df()
        st.dataframe(df_table)


with tab3:
    exercice_name = exercice.iloc[0]["exercice_name"]
    with open(f"answers/{exercice_name}.sql", "r") as f:
        answer = f.read()
    st.write(answer)
