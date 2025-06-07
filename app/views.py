from flask import Blueprint, render_template, redirect, request, url_for, session, flash
from app import db
from .models import Task

views = Blueprint('views', __name__)

@views.route('/')
def view_tasks():
    if 'user' not in session:
        return redirect(url_for('auth.login'))

    tasks = Task.query.all()
    return render_template('home.html', tasks=tasks)

@views.route('/add_tasks', methods=["POST"])
def add_tasks():
    if 'user' not in session:
        return redirect(url_for('auth.login'))

    title = request.form.get('title')
    if title:
        new_task = Task(title=title, status='Pending')
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully!', 'success')

    return redirect(url_for('views.view_tasks'))

@views.route('/toggle/<int:task_id>', methods=['POST'])  
def toggle_status(task_id):
    task = Task.query.get(task_id)
    if task:
        if task.status == 'Pending':
            task.status = 'Working'
        elif task.status == 'Working':
            task.status = 'Done'
        else:
            task.status = 'Pending'
        db.session.commit()

    return redirect(url_for('views.view_tasks'))

@views.route('/delete/<int:task_id>', methods=['POST'])
def del_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
        flash('Task deleted successfully!', 'info')
    return redirect(url_for('views.view_tasks'))

@views.route('/clear', methods=['POST'])
def clear():
    Task.query.delete()
    db.session.commit()
    flash('All tasks cleared.', 'info')
    return redirect(url_for('views.view_tasks'))
