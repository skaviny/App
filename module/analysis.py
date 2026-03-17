import pandas as pd

def load_data():
    df = pd.read_csv("data/processed/cleaned_data.csv")
    return df

def sum_of_marks(df):
    return df.groupby("Name")[["Math","Science","English"]].sum()

def top_performers(df, n=5):
    return df.sort_values(by="Total", ascending=False).head(n)

def hours_vs_sum(df):
    return df[["Hours_Studied"]], df[["Math","Science","English"]].sum(axis=1)



