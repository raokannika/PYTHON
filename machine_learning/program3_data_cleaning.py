# Program 3: Handle missing values
import pandas as pd

data = {"Name": ["A", "B", "C"], "Marks": [90, None, 85]}
df = pd.DataFrame(data)

print("Before Cleaning:\n", df)
df["Marks"].fillna(df["Marks"].mean(), inplace=True)
print("After Cleaning:\n", df)
