import pandas as pd

data = {
    'product_name': ['Product 1', 'Product 2', 'Product 3'],
    'price': [19.99, 29.99, 39.99],
    'availability': ['In stock', 'Out of stock', 'In stock']
}

df = pd.DataFrame(data)
df.to_csv('../products.csv', index=False)
