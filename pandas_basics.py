import pandas as pd

# Create DataFrame
data = {
    "Name": ["Ravi", "Anu", "Kiran", "Meena"],
    "Marks": [85, 78, 90, 70]
}

df = pd.DataFrame(data)

# Display data
print("Data:\n", df)

# Basic operations
print("Head:\n", df.head())
print("Columns:", df.columns)

# Select column
print("Names:\n", df["Name"])
print("Marks:\n", df["Marks"])