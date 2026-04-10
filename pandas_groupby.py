import pandas as pd

data = {
    "Name": ["Ravi", "Anu", "Kiran", "Meena", "Ajay"],
    "Marks": [85, 78, 90, 70, 88],
    "Course": ["Python", "SQL", "Python", "Excel", "SQL"]
}

df = pd.DataFrame(data)

print("Data:\n", df)

# GroupBy Sum
print("\nTotal Marks by Course:\n", df.groupby("Course")["Marks"].sum())

# GroupBy Mean
print("\nAverage Marks by Course:\n", df.groupby("Course")["Marks"].mean())

# GroupBy Count
print("\nCount by Course:\n", df.groupby("Course")["Name"].count())

# Multiple Aggregations
print("\nMultiple Stats:\n", df.groupby("Course")["Marks"].agg(["sum", "mean", "max"]))