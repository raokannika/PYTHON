# Program 2: Pandas Series and DataFrame
import pandas as pd

data = {"Name": ["Alice", "Bob", "Charlie"], "Marks": [85, 90, 78]}
df = pd.DataFrame(data)
print(df)
print("Average Marks:", df["Marks"].mean())
