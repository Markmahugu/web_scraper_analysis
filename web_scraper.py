import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the website to scrape
url = 'https://best.aliexpress.com'

# Send a request to the website
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Print the soup object to understand the structure
print(soup.prettify())

# Example: Extract product information
products = soup.find_all('div', class_='product-item')

data = []

for product in products:
    name = product.find('h2', class_='product-name').text.strip()
    price = product.find('span', class_='product-price').text.strip()
    description = product.find('p', class_='product-description').text.strip()

    data.append({
        'Name': name,
        'Price': price,
        'Description': description
    })

# Convert the data into a Pandas DataFrame
df = pd.DataFrame(data)

# Save the data to a CSV file
df.to_csv('products.csv', index=False)

print(df.head())
