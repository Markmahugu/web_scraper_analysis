import os

csv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'products.csv'))

if os.path.exists(csv_path):
    print("File exists")
else:
    print("File not found:", csv_path)
