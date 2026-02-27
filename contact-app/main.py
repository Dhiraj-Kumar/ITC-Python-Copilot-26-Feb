# Generate a basic flask app with home page, add contact page, edit contact page, and delete contact functionality.
from flask import Flask, render_template, request, redirect, url_for

# Setup the connection to the database. Use sqlite3 for simplicity.
import sqlite3

app = Flask(__name__)

def init_db():
    """
    Initialize the SQLite database for the contact application.
    
    Creates a new SQLite database file named 'contacts.db' if it doesn't already exist.
    Establishes a table named 'contacts' with the following columns:
    - id: Integer primary key with auto-increment
    - firstname: Text field for contact's first name (required)
    - lastname: Text field for contact's last name (required)
    - email: Text field for contact's email address (required)
    - phone: Text field for contact's phone number (required)
    - city: Text field for contact's city (required)
    
    Returns:
        None
    """
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            firstname TEXT NOT NULL,
            lastname TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            city TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('SELECT * FROM contacts')
    contacts = c.fetchall()
    conn.close()
    return render_template('index.html', contacts=contacts)

@app.route('/add', methods=['GET', 'POST'])
def add_contact():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        phone = request.form['phone']
        city = request.form['city']

        conn = sqlite3.connect('contacts.db')
        c = conn.cursor()
        c.execute('INSERT INTO contacts (firstname, lastname, email, phone, city) VALUES (?, ?, ?, ?, ?)',
                  (firstname, lastname, email, phone, city))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('addcontact.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_contact(id):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('SELECT * FROM contacts WHERE id = ?', (id,))
    contact = c.fetchone()
    conn.close()

    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        phone = request.form['phone']
        city = request.form['city']

        conn = sqlite3.connect('contacts.db')
        c = conn.cursor()
        c.execute('''
            UPDATE contacts
            SET firstname = ?, lastname = ?, email = ?, phone = ?, city = ?
            WHERE id = ?
        ''', (firstname, lastname, email, phone, city, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    return render_template('editcontact.html', contact=contact)

@app.route('/delete/<int:id>')
def delete_contact(id):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('DELETE FROM contacts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)