import pandas as pd
df = pd.read_csv("SampleSuperstore.csv")
print(df.head())
print(df.info())
print(df.describe())
print(df.groupby("Category")["Profit"].sum())
print(df.groupby("Region")["Profit"].sum().sort_values())