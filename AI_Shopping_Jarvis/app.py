from flask import Flask, render_template, request
from scraper import get_all_products
from ai_summary import generate_summary
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    products = []
    summary = ""
    if request.method == 'POST':
        query = request.form['query']
        products = get_all_products(query)
        summary = generate_summary(products)
    return render_template('index.html', products=products, summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
