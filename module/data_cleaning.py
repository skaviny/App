import pandas as pd

df = pd.read_csv("data/raw/data.csv")

print(df.shape)
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())

print(df.isnull())
print(df.isnull().sum())

df = df.drop_duplicates()
df = df.dropna()

print(df.isnull().sum())

df["Total"] = df["Math"] + df["Science"] + df["English"]
df["Average"] = df["Total"] / 3

df.to_csv("data/processed/cleaned_data.csv", index=False)