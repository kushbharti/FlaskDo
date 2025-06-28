
 <h2> login.html# 📝 Flask To-Do App with Authentication </h2>

A simple Flask-based To-Do List web application that supports login, task tracking with status updates, deletion, and clearing — all backed by SQLite and SQLAlchemy.

---

## 🚀 Features

- ✅ User Login (Session-based)
- ➕ Add tasks
- 🔁 Toggle task status: Pending → Working → Done
- 🗑️ Delete tasks
- ❌ Clear all tasks
- 🔒 Session-protected routes

---

## 🧱 Tech Stack

- Python (Flask)
- Flask Blueprints
- SQLite (via SQLAlchemy)
- Jinja2 Templates (HTML)

---

## 📁 Project Structure

project/
│
├── app/
│ ├── init.py # App & DB setup
│ ├── models.py # Task model
│ ├── views.py # Task routes
│ └── auth.py # Login/logout logic
│
├── templates/
│ ├── home.html
│ └── login.html
| └── base.html
| └── register.html
│
├── static/ # Optional: styles/scripts
├── main.py # App entry point
├── requirements.txt # Dependencies
└── README.md


<h2>Create & activate virtual environment</h2>

python -m venv env
 .\env\Scripts\activate  # Windows
 source env/bin/activate  # macOS/Linux

<h2> Install dependencies </h2>

pip install -r requirements.txt

<h2> Run the app </h2>

python main.py

<h2> 🔐 Login Credentials </h2>
Username	      Password
admin	           1234

<h2> 🧩 Future Improvements </h2>

User registration system
Password hashing for security
Task due dates and priorities
UI enhancements (CSS/JS)


