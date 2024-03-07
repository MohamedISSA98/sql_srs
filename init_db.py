import io

import duckdb
import pandas as pd

con = duckdb.connect(database="data/exercices_sql_tables.duckdb", read_only=False)

# -----------------------------------------
# EXERCICES LIST
# -----------------------------------------

data = {
    "theme": ["Joins", "Window Functions"],
    "exercices_name": ["beverages_and_food", "simple_window"],
    "tables": [["beverages", "food_items"], "simple_window"],
    "last_reviewed": ["1970-01-01", "1970-01-01"]
}
memory_state_df = pd.DataFrame(data)
conn.execute("CREATE TABLE IF NOT EXISTS memory_state AS SELECT * FROM memory_state_df")

# -----------------------------------------
# CROSS JOIN EXERCICES
# -----------------------------------------

CSV = """
beverage, price
orange juice, 2.5
Expresso, 2
Tea, 3
"""
beverages = pd.read_csv(io.StringIO(CSV))
con.execute("CREATE TABLE IF NOT EXISTS beverages AS SELECT * FROM beverages")

CSV2 = """
food_item, food_price
cookie, 2.5
chocolatine, 2
muffin, 3
"""
food_items = pd.read_csv(io.StringIO(CSV2))
con.execute("CREATE TABLE IF NOT EXISTS food_items AS SELECT * FROM food_items")

# ANSWER = """
# SELECT * FROM beverages
# CROSS JOIN food_items
# """
# solution = duckdb.sql(ANSWER).df()
# con.execute("CREATE TABLE IF NOT EXISTS solution AS SELECT * FROM solution")
