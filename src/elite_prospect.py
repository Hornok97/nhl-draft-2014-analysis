import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_nhl_draft_data(year):
    # Adresa AJAX endpointu s daty
    url = f"https://www.eliteprospects.com/ajax/draft.players?type=NHL+Entry+Draft&year={year}&league=NHL"
    
    # Stáhneme data přímo z této URL
    response = requests.get(url)
    
    # Kontrola správného načtení
    if response.status_code != 200:
        print(f"Chyba při načtení dat. Status: {response.status_code}")
        return None
    
    # Parsujeme HTML pomocí BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Najdeme tabulku s hráči
    table = soup.find("table", class_="players")

    # Kontrola, zda tabulka existuje
    if table is None:
        print("Tabulka s hráči nenalezena!")
        return None

    # Inicializace seznamu pro ukládání dat
    players_data = []

    # Projdeme každý řádek tabulky a uložíme data
    for row in table.find_all("tr"):
        cols = row.find_all("td")
        
        # Přeskočíme řádky bez dostatečného počtu sloupců (např. záhlaví)
        if len(cols) < 10:
            continue

        # Extrakce dat
        position = cols[0].text.strip()
        team = cols[2].text.strip()
        player = cols[3].text.strip()
        seasons = cols[4].text.strip()
        gp = cols[5].text.strip()
        goals = cols[6].text.strip()
        assists = cols[7].text.strip()
        points = cols[8].text.strip()
        pim = cols[9].text.strip()

        # Přidáme data hráče do seznamu
        players_data.append({
            "Position": position,
            "Player": player,
            "Team": team,
            "Seasons": seasons,
            "GP": gp,
            "Goals": goals,
            "Assists": assists,
            "Points": points,
            "PIM": pim
        })

    # Vytvoříme DataFrame pomocí pandas
    df = pd.DataFrame(players_data)
    
    return df

# Zavoláme funkci pro rok 2014
df_draft2014 = get_nhl_draft_data(2014)

# Zkontrolujeme data (prvních 10 řádků)
if df_draft2014 is not None:
    print(df_draft2014.head(10))

    # Uložení do CSV
    df_draft2014.to_csv("nhl_draft_2014.csv", index=False)
else:
    print("Data se nepodařilo získat.")
