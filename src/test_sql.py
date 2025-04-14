import sqlite3
import pandas as pd

conn = sqlite3.connect("nhl_draft.db")
df_check = pd.read_sql("SELECT * FROM draft2014 LIMIT 10", conn)
print(df_check)
conn.close()
