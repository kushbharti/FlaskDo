
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

project/  <br>
│        <br>
├── app/  <br>
│ ├── init.py # App & DB setup   <br>
│ ├── models.py # Task model     <br>
│ ├── views.py # Task routes     <br>
│ └── auth.py # Login/logout logic    <br>
│                                   <br>
├── templates/                     <br>
│ ├── home.html                      <br>
│ └── login.html                  <br>
| └── base.html                  <br>
| └── register.html           <br>
│                              <br>
├── static/ # Optional: styles/scripts  <br>
├── main.py # App entry point          <br>
├── requirements.txt # Dependencies     <br>
└── README.md                        <br>


<h2>Create & activate virtual environment</h2>

python -m venv env
 .\env\Scripts\activate  # Windows <br>
 or <br>
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


