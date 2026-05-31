# Dataset Detective

import pandas as pd

# Load dataset (example: CSV file)
df = pd.read_csv(r"C:\Users\tanushree hiremath\Downloads\data_100_students.csv")

# Display top rows
print("Top 5 rows of dataset:")
print(df.head())

# Find column with highest maximum value
max_values = df.max(numeric_only=True)
highest_column = max_values.idxmax()

print("\nColumn with highest value:", highest_column)
print("Highest value:", max_values.max())

# Count missing values
print("\nMissing values in each column:")
print(df.isnull().sum())