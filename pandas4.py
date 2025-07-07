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