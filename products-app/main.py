# Generate a basic flask application setup with 4 routes: home, about, contact and products
from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html') 

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/products')
def products():
    # Fetch products data from an API - https://dummyjson.com/products
    response = requests.get("https://dummyjson.com/products")
    products_data = response.json()
    return render_template('products.html', products=products_data['products'])

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    # Fetch product details from an API - https://dummyjson.com/products/{id}
    try:
        response = requests.get(f"https://dummyjson.com/products/{product_id}", timeout=5)
        response.raise_for_status()
        product_data = response.json()
        return render_template('product.html', product=product_data)
    except requests.exceptions.Timeout:
        return render_template('error.html', message='Request timed out'), 504
    except requests.exceptions.HTTPError:
        return render_template('error.html', message='Product not found'), 404
    except requests.exceptions.RequestException:
        return render_template('error.html', message='Failed to fetch product'), 500
    except ValueError:
        return render_template('error.html', message='Invalid response format'), 500

if __name__ == '__main__':
    app.run(debug=True)