import pandas as pd

# Create data with missing values
data = {
    "Name": ["Ravi", "Anu", "Kiran", "Meena"],
    "Marks": [85, None, 90, None]
}

df = pd.DataFrame(data)

print("Original Data:\n", df)

# Check missing
print("\nMissing Values:\n", df.isnull())

# Drop missing
print("\nAfter Drop:\n", df.dropna())

# Fill with 0
print("\nFill with 0:\n", df.fillna(0))

# Fill with mean
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
print("\nFill with Mean:\n", df)