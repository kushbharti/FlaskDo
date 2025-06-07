from flask import Blueprint, render_template, redirect, request, url_for, session, flash

auth = Blueprint('auth', __name__)

USER_CREDENTIAL = {
    'username': 'admin',
    'password': '1234'
}

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == USER_CREDENTIAL['username'] and password == USER_CREDENTIAL['password']:
            session['user'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('views.view_tasks'))  
        else:
            flash("Invalid username or password. Try again!", 'danger')
    
    return render_template('login.html')

@auth.route('/logout')
def logout():
    session.pop('user', None)
    flash('Logged out successfully!', 'info')
    return redirect(url_for('auth.login'))  

            
    