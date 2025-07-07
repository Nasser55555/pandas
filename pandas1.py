import pandas as pd
import numpy as np

# Create the data
data = [
    ["Amine", 28, "Casablanca"],
    ["Lina", 22, "Rabat"],
    ["Youssef", 35, "Fez"],
    ["Salma", 30, "Casablanca"],
    ["Nora", np.nan, "Tangier"]
]

# Create the DataFrame
df = pd.DataFrame(data, columns=["Nom", "Âge", "Ville"])

# Display the first 5 lines
print(df.head())

# Display structure
print(df.info())

# Display descriptive statistics
print(df.describe())
