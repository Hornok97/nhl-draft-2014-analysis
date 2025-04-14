import mysql.connector
import pandas as pd

# Připojení k databázi
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="********",  # nahraď svým heslem
    database="nhl_draft"
)

# Funkce pro spuštění SQL dotazu a vrácení výsledků
def run_query(query):
    return pd.read_sql(query, conn)

# 1️⃣ Top 10 hráčů podle bodů
query1 = """
SELECT Player, Team, Points
FROM draft2014
ORDER BY CAST(Points AS UNSIGNED) DESC
LIMIT 10;
"""
df_top10 = run_query(query1)
print("Top 10 hráčů podle bodů:")
print(df_top10)

# 2️⃣ Draftová pozice vs. body
query2 = """
SELECT
  CAST(REPLACE(Position, '#', '') AS UNSIGNED) AS DraftPosition,
  Player,
  Points
FROM draft2014
WHERE Points IS NOT NULL AND Points != ''
ORDER BY DraftPosition;
"""
df_draft_vs_points = run_query(query2)
print("\nDraft pozice vs body:")
print(df_draft_vs_points.head())

# Zavřeme spojení
conn.close()
