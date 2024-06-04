from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def index():
    csv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'products.csv'))
    if not os.path.exists(csv_path):
        return "Error: products.csv file not found."

    try:
        df = pd.read_csv(csv_path)
        if df.empty:
            return "Error: products.csv file is empty."
    except pd.errors.EmptyDataError:
        return "Error: products.csv file is empty or improperly formatted."

    products = df.to_dict(orient='records')
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
