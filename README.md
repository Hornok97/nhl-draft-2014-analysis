
# NHL Draft 2014 – Data Analysis Project

Tento projekt analyzuje draft NHL z roku 2014 a sleduje, jak si jednotliví hráči vedli po svém výběru. Data jsou získána ze serveru EliteProspects, uložena do databáze, analyzována pomocí SQL a Pythonu. Výsledkem je také čistý Excelový report se všemi klíčovými přehledy. Ůvodní myšlenka pro mě byla zjistit, jak si vede David Pastrňák.

---

## Co se naučíte / ukážete

- Web scraping a zpracování dat
- Uložení dat do relační databáze (MySQL, SQLite)
- Pokročilá práce s SQL dotazy
- Analýza pomocí Pythonu (pandas, matplotlib, seaborn)
- Export profesionálních vícelistových Excel reportů
- Vhodná struktura projektu pro GitHub

---

## Instalace a spuštění

### 1️ Klonuj projekt nebo si jej stáhni(Doporučuji stahovat):

```bash
git clone https://github.com/tvuj-username/nhl-draft-2014-analysis.git
cd nhl-draft-2014-analysis
```

### 2️ Nainstaluj potřebné knihovny:

```bash
pip install pandas matplotlib seaborn openpyxl mysql-connector-python
```

### 3️ Získej data (pokud je chceš stáhnout znova):

```bash
python src/elite_prospect.py
```

 Uloží data do `data/nhl_draft_2014.csv`

---

## Práce s databází

> Můžeš použít MySQL nebo SQLite

### Varianta 1 – MySQL

- Importuj data do tabulky `draft2014` v databázi `nhl_draft` (SQL skripty v `sql/`)
- Používej dotazy ze souboru `analysis_queries.sql`

### Varianta 2 – SQLite (offline)

- Otevři `db/nhl_draft.db` – obsahuje stejná data připravená k použití
- Můžeš číst pomocí `sqlite3` nebo Pandas

---

##  Vizualizace

Spusť grafy přes:

```bash
python src/visualization.py
```

Ukázky:
- Top 10 hráčů podle bodů

---

## Excelový report

Všechny výsledky exportovány do naformátovaného Excel souboru:

```bash
python src/export_draft_to_excel.py
```

Listy obsahují:
1. Kompletní draft
2. Seřazení podle bodů
3. Seřazení podle počtu zápasů
4. Obránci (označeni „(D)“) seřazení podle bodů

Výstup: `excel/nhl_draft_2014_analýza.xlsx`

---

## Struktura projektu

```
nhl-draft-2014-analysis/
├── data/         # Zdrojová data
├── db/           # SQL databáze
├── excel/        # Výstupní Excel report
├── sql/          # SQL dotazy
├── src/          # Python skripty
├── README.md     # Popis
└── .gitignore
```

---

## Možné rozšíření

- Porovnání více ročníků draftu (např. 2013 vs. 2014 vs. 2015)
- Výpočet „draft steal indexu“ (výkon vs. pořadí)
- Automatický scraping vícero let
- Vytvoření dashboardu (např. Streamlit nebo Tableau)

---

## Autor

[Hornok97](https://github.com/Hornok97)
