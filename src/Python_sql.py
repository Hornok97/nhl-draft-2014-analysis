import sqlite3
import pandas as pd

# Načteme data z CSV
df = pd.read_csv("nhl_draft_2014.csv")

# Zobrazíme prvních 5 řádků pro kontrolu
print(df.head())

# Vytvoříme (nebo připojíme se k) SQLite databázi
conn = sqlite3.connect("nhl_draft.db")

# Importujeme data z DataFrame do SQL databáze
df.to_sql("draft2014", conn, if_exists="replace", index=False)

# Zkontrolujeme, zda data byla vložena správně
df_check = pd.read_sql("SELECT * FROM draft2014 LIMIT 5", conn)
print("Kontrola importu:")
print(df_check)

# Zavřeme spojení s databází
conn.close()
