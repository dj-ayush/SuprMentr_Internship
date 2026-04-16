# Storytelling with Graphs

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data_100_students.csv")

# -------- Bar Chart --------
# Average marks by age
avg_marks = df.groupby("Age")["Marks"].mean()

plt.figure()
avg_marks.plot(kind="bar")
plt.title("Average Marks by Age")
plt.xlabel("Age")
plt.ylabel("Average Marks")
plt.show()

# -------- Pie Chart --------
# Grade distribution
def grade(m):
    if m >= 90:
        return "A"
    elif m >= 75:
        return "B"
    elif m >= 60:
        return "C"
    else:
        return "D"

df["Grade"] = df["Marks"].apply(grade)
grade_counts = df["Grade"].value_counts()

plt.figure()
plt.pie(grade_counts, labels=grade_counts.index, autopct='%1.1f%%')
plt.title("Grade Distribution")
plt.show()

# -------- Histogram --------
plt.figure()
plt.hist(df["Marks"], bins=10)
plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()