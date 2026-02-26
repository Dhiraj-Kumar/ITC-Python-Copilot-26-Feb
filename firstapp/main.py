# Write a simple flask application with a single route that returns "Hello, World!" when accessed.
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', username="Dhiraj")

@app.route('/about')
def about():
    return render_template('about.html')

# generate contact route
@app.route('/contact')
def contact():
    return render_template('contact.html')

# generate a route for products
@app.route('/products')
def products():
    return render_template('products.html', products=["Laptop", "Smartphone", "Tablet", "Headphones", "Smartwatch"])

if __name__ == '__main__':
    app.run(debug=True)