#!/usr/bin/env python3
"""Flask application displaying product data from JSON or CSV files."""

import csv
import json

from flask import Flask, render_template, request

app = Flask(__name__)


def read_json_products():
    """Read and return the list of products from products.json."""
    with open('products.json', 'r', encoding='utf-8') as json_file:
        return json.load(json_file)


def read_csv_products():
    """Read and return the list of products from products.csv."""
    with open('products.csv', 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        products = []
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price']),
            })
        return products


@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')


@app.route('/items')
def items():
    """Render the items page with a list of items read from JSON."""
    with open('items.json', 'r', encoding='utf-8') as items_file:
        data = json.load(items_file)
    return render_template('items.html', items=data.get('items', []))


@app.route('/products')
def products():
    """Render the products page, filtered by source and optional id."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        product_list = read_json_products()
    elif source == 'csv':
        product_list = read_csv_products()
    else:
        return render_template('product_display.html', error='Wrong source')

    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template(
                'product_display.html', error='Product not found')

        product_list = [
            product for product in product_list
            if product['id'] == product_id
        ]
        if not product_list:
            return render_template(
                'product_display.html', error='Product not found')

    return render_template('product_display.html', products=product_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
