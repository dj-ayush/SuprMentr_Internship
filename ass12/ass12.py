# Import libraries
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv(r"C:\Users\tanushree hiremath\OneDrive\Desktop\internship assignments\ass12\house_price_dataset_1000.csv")

# Display first rows
print("Dataset Preview:")
print(df.head())

# Features (inputs)
X = df[["Size_sqft", "Bedrooms", "House_Age"]]

# Label (target)
y = df["Price"]

# Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create Linear Regression model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predict prices for test data
predictions = model.predict(X_test)

print("\nSample Predictions:")
print(predictions[:5])

# Test with new input
size = float(input("Enter house size (sqft): "))
bedrooms = int(input("Enter number of bedrooms: "))
age = int(input("Enter house age: "))

new_house = pd.DataFrame({
    "Size_sqft": [size],
    "Bedrooms": [bedrooms],
    "House_Age": [age]
})

predicted_price = model.predict(new_house)

print("\nPredicted House Price:", predicted_price[0])