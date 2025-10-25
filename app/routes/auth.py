from flask import Blueprint, redirect, request, render_template, flash, url_for, session
from app import db
from app.models import User  # Make sure your model class is named 'User'

auth = Blueprint('auth', __name__)

# LOGIN ROUTE
@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Check if user exists
        existing_user = User.query.filter_by(username=username).first()

        if existing_user:
            # For real apps, use hashed passwords (e.g., Werkzeug)
            if existing_user.password == password:
                session['user'] = username
                flash('Login Successful!', 'success')
                return redirect(url_for('task_bp.view_task'))
            else:
                flash('Incorrect password. Try again.', 'danger')
        else:
            flash('User does not exist. Please register.', 'warning')

    return render_template('login.html')

# LOGOUT ROUTE
@auth.route("/logout")
def logout():
    session.pop('user', None)
    flash('Logout Successful!', 'success')
    return redirect(url_for('auth.login'))

# REGISTER ROUTE
@auth.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Check if username is already taken
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists. Please choose a different one.', 'warning')
            return redirect(url_for('auth.register'))

        # Add new user (hash password in real apps!)
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')
