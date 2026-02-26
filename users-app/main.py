# Generate a  simple flask application that returns "Hello, World!" when accessed at the root URL ("/").
from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Fetch the data from https://jsonplaceholder.typicode.com/users using requests
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    data = response.json()
    # Pass the data to the template
    return render_template('index.html', users=data)

if __name__ == '__main__':
    app.run(debug=True)