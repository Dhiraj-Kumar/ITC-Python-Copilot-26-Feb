# Generate a basic flask application with two routes - home, joke
from flask import Flask, render_template, request, redirect, url_for
import requests
app = Flask(__name__)

@app.route('/')
def home():
    # Fetch the joke categories from an API - https://v2.jokeapi.dev/categories and pass it to the template
    response = requests.get("https://v2.jokeapi.dev/categories")
    categories = response.json() if response.status_code == 200 else []
    return render_template('index.html', categories=categories.get('categories', []))

@app.route('/joke/<category>')
def joke(category):
    response = requests.get(f"https://v2.jokeapi.dev/joke/{category}?type=single")
    joke_data = response.json() if response.status_code == 200 else {}
    return render_template('joke.html', joke=joke_data.get('joke', 'No joke found.'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # if email is equal to dhiraj.kumar@gmail.com and password is 123456 then redirect to home page else show error message
        if email == 'dhiraj.kumar@gmail.com' and password == '123456':
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error="Invalid email or password. Please try again.")
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)