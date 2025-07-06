
 <h2> # 📝 Flask To-Do App with Authentication </h2>

A simple Flask-based To-Do List web application that supports login, task tracking with status updates, deletion, and clearing — all backed by SQLite and SQLAlchemy.

---


![Screenshot 2025-07-06 130205](https://github.com/user-attachments/assets/eb9b696b-d49e-479c-a1ce-df4aa95e383b)<br> <br>

![Screenshot 2025-07-06 130257](https://github.com/user-attachments/assets/2a890f03-cb75-40f0-a968-af889d1a5a2f)<br> <br>


![Screenshot 2025-07-06 130314](https://github.com/user-attachments/assets/d1c51ece-d62a-4eee-9cf5-53509a1b7cf2) <br> <br>



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
│ ├── home.html                  <br>
│ └── login.html                <br>
| └── base.html                <br>
| └── register.html          <br>
│                           <br>
├── static/ # Optional: styles/scripts  <br>
├── main.py # App entry point         <br>
├── requirements.txt # Dependencies  <br>
└── README.md                    <br>


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
Username	:- admin <br>
Password :- 1234<br>

<h2> 🧩 Future Improvements </h2>

User registration system  <br>
Password hashing for security <br>
Task due dates and priorities<br>
UI enhancements (CSS/JS)<br>


