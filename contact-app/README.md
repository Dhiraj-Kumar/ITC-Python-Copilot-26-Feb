# Contact App

A simple Flask-based web application to manage contacts. Users can add, edit, view, and delete contacts. Data is stored in a local SQLite database.

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [Database Schema](#database-schema)
- [User Handbook](#user-handbook)
  - [Home Page](#home-page)
  - [Add Contact](#add-contact)
  - [Edit Contact](#edit-contact)
  - [Delete Contact](#delete-contact)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## Features

- View all contacts in a table.
- Add new contacts.
- Edit existing contacts.
- Delete contacts with confirmation.
- Responsive UI using Bootstrap 5.

---

## Installation

1. **Clone the repository:**
   ```sh
   git clone <repository-url>
   cd contact-app
   ```

2. **Create a virtual environment (optional but recommended):**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```sh
   pip install flask
   ```

---

## Running the Application

1. **Initialize and start the app:**
   ```sh
   python main.py
   ```

2. **Access the app:**
   - Open your browser and go to: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## Project Structure

```
contact-app/
│
├── main.py
├── pyproject.toml
├── README.md
├── .python-version
└── templates/
    ├── base.html
    ├── index.html
    ├── addcontact.html
    └── editcontact.html
```

- **main.py**: Main Flask application.
- **templates/**: HTML templates for the app.

---

## Database Schema

The app uses a SQLite database named `contacts.db` with a single table:

| Column     | Type    | Description                |
|------------|---------|---------------------------|
| id         | INTEGER | Primary key, auto-increment|
| firstname  | TEXT    | Contact's first name      |
| lastname   | TEXT    | Contact's last name       |
| email      | TEXT    | Contact's email address   |
| phone      | TEXT    | Contact's phone number    |
| city       | TEXT    | Contact's city            |

---

## User Handbook

### Home Page

- **URL:** `/`
- **Description:** Displays a table of all contacts.
- **Actions:**
  - Click **Add New Contact** to add a new contact.
  - Click **Edit** to modify a contact.
  - Click **Delete** to remove a contact (confirmation required).

### Add Contact

- **URL:** `/add`
- **How to Use:**
  1. Click **Add New Contact** on the home page.
  2. Fill in all fields: First Name, Last Name, Email, Phone Number, City.
  3. Click **Add Contact**.
  4. You will be redirected to the home page with the new contact listed.

### Edit Contact

- **URL:** `/edit/<id>`
- **How to Use:**
  1. Click **Edit** next to the contact you wish to modify.
  2. Update the fields as needed.
  3. Click **Update Contact**.
  4. You will be redirected to the home page with the updated information.

### Delete Contact

- **URL:** `/delete/<id>`
- **How to Use:**
  1. Click **Delete** next to the contact you wish to remove.
  2. A confirmation dialog will appear.
  3. Click **Yes** to confirm deletion, or **No** to cancel.
  4. After confirmation, the contact will be removed from the list.

---

## Troubleshooting

- **Database not created:** The database is automatically created on first run.
- **Port already in use:** Change the port in `main.py` by modifying `app.run(debug=True, port=YOUR_PORT)`.
- **Dependencies missing:** Ensure Flask is installed (`pip install flask`).

---

## License

This project is for educational purposes.

---

**For any issues, please contact the project maintainer.**