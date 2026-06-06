import pandas as pd

# Wczytanie danych

df = pd.read_csv("analiza_danych/dane_zawodnikow.csv")

# Sortowanie po ocenie scoutingowej

ranking = df.sort_values(
by="ocena_scoutingowa",
ascending=False
)

print("=== RANKING ZAWODNIKÓW ===")
print(ranking[
[
"imie_nazwisko",
"pozycja",
"wiek",
"ocena_scoutingowa"
]
])
