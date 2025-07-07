import pandas as pd
import numpy as np

data = [
    ["Amine", 28, "Casablanca"],
    ["Lina", 22, "Rabat"],
    ["Youssef", 35, "Fez"],
    ["Salma", 30, "Casablanca"],
    ["Nora", np.nan, "Tangier"]
]

df = pd.DataFrame(data, columns=["Nom", "Âge", "Ville"])

df["Année de Naissance"] = 2025 - df["Âge"]

df["Nom"] = df["Nom"].str.upper()

df = df.rename(columns={"Ville": "Localisation"})

print(df)