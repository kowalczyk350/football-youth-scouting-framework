import pandas as pd
import matplotlib.pyplot as plt

# Wczytanie danych

df = pd.read_csv("analiza_danych/dane_zawodnikow.csv")

# Sortowanie

df = df.sort_values(
by="ocena_scoutingowa",
ascending=False
)

# Wykres

plt.figure(figsize=(8,5))

plt.bar(
df["imie_nazwisko"],
df["ocena_scoutingowa"]
)

plt.xlabel("Zawodnik")
plt.ylabel("Ocena scoutingowa")
plt.title("Porównanie ocen zawodników")

plt.show()
