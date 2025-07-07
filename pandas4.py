import pandas as pd
import numpy as np
data = [
    ["Amina", 28, "casablanca"],
    ["Lina", 22, "rabat"],
    ["youssef", 35, "fez"],
    ["salma", 30, "casablanca"],
    ["nora", np.nan, "tanger"],
]
df = pd.DataFrame(data, columns=["Nom", "Age", "Ville"])
df.loc[4, "Age"] = np.nan

print("📍 Missing ages:")
print(df[df["Age"].isnull()])

mean_age = df["Age"].mean()
df["Age"] = df["Age"].fillna(mean_age)

print(df)