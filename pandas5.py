import pandas as pd
import numpy as np

data = [
    ["Amine", 28, "Casablanca"],
    ["Lina", 22, "Rabat"],
    ["Youssef", 35, "Fez"],
    ["Salma", 30, "Casablanca"],
    ["Nora", 28.75, "Tangier"]
]

df = pd.DataFrame(data, columns=["Nom", "Âge", "Ville"])

df["Année de Naissance"] = 2025 - df["Âge"]

print("📊 Sorted by age (high to low):")
print(df.sort_values(by="Âge", ascending=False))

df = df.drop("Année de Naissance", axis=1)

df = df.drop(index=0)

print(df)
