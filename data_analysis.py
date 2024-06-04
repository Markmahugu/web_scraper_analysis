import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from the CSV file
df = pd.read_csv('web_scraper_analysis/products.csv')

# Perform basic data analysis
print(df.describe())
print(df.info())

# Example: Price distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['Price'], bins=20, kde=True)
plt.title('Price Distribution')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

# Example: Average price by product category (if you have a category column)
plt.figure(figsize=(12, 8))
sns.barplot(x='Category', y='Price', data=df)
plt.title('Average Price by Category')
plt.xlabel('Category')
plt.ylabel('Average Price')
plt.xticks(rotation=45)
plt.show()
