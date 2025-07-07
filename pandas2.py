import pandas as pd
import numpy as np

# Step 1: Create the data
data = [
    ["Amine", 28, "Casablanca"],
    ["Lina", 22, "Rabat"],
    ["Youssef", 35, "Fez"],
    ["Salma", 30, "Casablanca"],
    ["Nora", np.nan, "Tangier"]
]

# Step 2: Create DataFrame
df = pd.DataFrame(data, columns=["Nom", "Âge", "Ville"])

# 1. Select the Ville column
print("📍 Column 'Ville':")
print(df["Ville"])

# 2. Rows where Âge > 25
print("\n📍 People older than 25:")
print(df[df["Âge"] > 25])

# 3. Name and City of people in Casablanca
print("\n📍 People in Casablanca (Nom & Ville):")
print(df[df["Ville"] == "Casablanca"][["Nom", "Ville"]])
