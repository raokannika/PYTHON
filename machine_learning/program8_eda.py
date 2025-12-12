# Program 8: Basic EDA
import pandas as pd

df = pd.read_csv("titanic.csv")  # Use a Titanic dataset CSV
print(df.head())
print("Survival rate:", df["Survived"].mean())
print("Age Stats:\n", df["Age"].describe())
