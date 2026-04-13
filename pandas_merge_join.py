import pandas as pd

df1 = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Ravi", "Anu", "Kiran"]
})

df2 = pd.DataFrame({
    "ID": [1, 2, 4],
    "Marks": [85, 78, 90]
})

print("DF1:\n", df1)
print("\nDF2:\n", df2)

# Inner Join
print("\nInner Join:\n", pd.merge(df1, df2, on="ID", how="inner"))

# Left Join
print("\nLeft Join:\n", pd.merge(df1, df2, on="ID", how="left"))

# Right Join
print("\nRight Join:\n", pd.merge(df1, df2, on="ID", how="right"))

# Outer Join
print("\nOuter Join:\n", pd.merge(df1, df2, on="ID", how="outer"))