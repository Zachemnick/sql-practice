import pandas as pd
import sqlite3

conn = sqlite3.connect("llm.db")
pd.read_csv("prompts.csv").to_sql(
    "prompts", conn, if_exists="replace", index=False
)

pd.read_csv("passages.csv").to_sql(
    "passages", conn, if_exists="replace", index=False
)
conn.close()
print("Готово")