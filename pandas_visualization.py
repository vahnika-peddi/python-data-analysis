import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Name": ["Ravi", "Anu", "Kiran", "Meena", "Ajay"],
    "Marks": [85, 78, 90, 70, 88]
}

df = pd.DataFrame(data)

# Bar Chart
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks")
plt.xlabel("Name")
plt.ylabel("Marks")
plt.show()

# Line Chart
plt.plot(df["Name"], df["Marks"])
plt.title("Marks Trend")
plt.show()

# Seaborn Plot
sns.barplot(x="Name", y="Marks", data=df)
plt.title("Seaborn Chart")
plt.show()