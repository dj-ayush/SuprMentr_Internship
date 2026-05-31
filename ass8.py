# Data Doctor

import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\Users\tanushree hiremath\Downloads\data_100_students.csv")

print("Original Dataset:")
print(df.head())

# 1. Handle missing values
# Fill missing Age values with the average age
df["Age"] = df["Age"].fillna(df["Age"].mean())

# 2. Remove duplicate rows
df = df.drop_duplicates()

# 3. Standardize text (convert names to lowercase)
df["Name"] = df["Name"].str.lower()

# Show cleaned dataset
print("\nCleaned Dataset:")
print(df.head())

# Save cleaned dataset
df.to_csv("cleaned_data.csv", index=False)

print("\nCleaned dataset saved as cleaned_data.csv")