import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Připojení k databázi
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Barcelona97",  # nahraď svým heslem
    database="nhl_draft"
)

# 1️⃣ Dotaz: Top 10 hráčů podle bodů
query = """
SELECT Player, Team, Points
FROM draft2014
ORDER BY CAST(Points AS UNSIGNED) DESC
LIMIT 10;
"""

# Načti data do pandas DataFrame
df = pd.read_sql(query, conn)
df['Points'] = df['Points'].astype(int)

# Zavři připojení
conn.close()

# 2️⃣ Vykresli graf
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Points', y='Player', palette='Blues_d')
plt.title('Top 10 hráčů draftu 2014 podle bodů')
plt.xlabel('Body')
plt.ylabel('Hráč')
plt.tight_layout()
plt.show()
