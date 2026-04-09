import pandas as pd

data = {
    "Name": ["Ravi", "Anu", "Kiran", "Meena", "Ajay"],
    "Marks": [85, 78, 90, 70, 88],
    "Course": ["Python", "SQL", "Python", "Excel", "SQL"]
}

df = pd.DataFrame(data)

print("Data:\n", df)

# Filtering
print("\nMarks > 80:\n", df[df["Marks"] > 80])

# AND condition
print("\nPython & Marks > 80:\n", df[(df["Course"] == "Python") & (df["Marks"] > 80)])

# OR condition
print("\nSQL or Excel:\n", df[(df["Course"] == "SQL") | (df["Course"] == "Excel")])

# Sorting
print("\nSorted by Marks:\n", df.sort_values(by="Marks", ascending=False))

# Select
print("\nSelected Columns:\n", df[["Name", "Marks"]])
print("\nFirst Row:\n", df.iloc[0])