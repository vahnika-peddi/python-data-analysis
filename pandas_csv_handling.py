import pandas as pd

# Read CSV file
df = pd.read_csv("data.csv")

print("Data:\n", df)

print("\nHead:\n", df.head())

print("\nInfo:\n")
print(df.info())

print("\nStatistics:\n", df.describe())

print("\nMarks:\n", df["Marks"])