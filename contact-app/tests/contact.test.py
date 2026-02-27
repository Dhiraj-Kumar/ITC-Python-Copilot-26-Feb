import pytest
import sqlite3
import os
from main import app, init_db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        init_db()
        yield client
    if os.path.exists('contacts.db'):
        os.remove('contacts.db')

@pytest.fixture
def sample_contact():
    return {
        'firstname': 'John',
        'lastname': 'Doe',
        'email': 'john@example.com',
        'phone': '123-456-7890',
        'city': 'New York'
    }

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200

def test_add_contact_get(client):
    response = client.get('/add')
    assert response.status_code == 200

def test_add_contact_post(client, sample_contact):
    response = client.post('/add', data=sample_contact, follow_redirects=True)
    assert response.status_code == 200
    
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('SELECT * FROM contacts WHERE firstname = ?', ('John',))
    contact = c.fetchone()
    conn.close()
    assert contact is not None
    assert contact[1] == 'John'

def test_edit_contact_get(client, sample_contact):
    client.post('/add', data=sample_contact)
    response = client.get('/edit/1')
    assert response.status_code == 200

def test_edit_contact_post(client, sample_contact):
    client.post('/add', data=sample_contact)
    updated_contact = sample_contact.copy()
    updated_contact['firstname'] = 'Jane'
    response = client.post('/edit/1', data=updated_contact, follow_redirects=True)
    assert response.status_code == 200
    
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('SELECT * FROM contacts WHERE id = 1')
    contact = c.fetchone()
    conn.close()
    assert contact[1] == 'Jane'

def test_delete_contact(client, sample_contact):
    client.post('/add', data=sample_contact)
    response = client.get('/delete/1', follow_redirects=True)
    assert response.status_code == 200
    
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('SELECT * FROM contacts WHERE id = 1')
    contact = c.fetchone()
    conn.close()
    assert contact is None