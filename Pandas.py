# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv("sales_data.csv")  # Replace with your actual file name

# Display first 5 rows of the dataset
print("Sample Data:")
print(df.head())

# Basic summary
print("\nDataset Info:")
print(df.info())

# Group by Product and sum the Sales
product_sales = df.groupby("Product")["Sales"].sum().reset_index()

# Display grouped data
print("\nTotal Sales per Product:")
print(product_sales)

# Plot the total sales per product
plt.figure(figsize=(10, 6))
plt.bar(product_sales["Product"], product_sales["Sales"], color='skyblue')
plt.title("Total Sales per Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

