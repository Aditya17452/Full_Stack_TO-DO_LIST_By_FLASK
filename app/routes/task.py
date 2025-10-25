from flask import Blueprint, redirect, request, render_template, flash, url_for, session
from app import db
from app.models import User

task_bp = Blueprint('task_bp', __name__)

@task_bp.route("/")
def view_task():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    current_user = User.query.filter_by(username=session['user']).first()
    return render_template("task.html", task=current_user)

@task_bp.route("/add_task", methods=['POST'])
def add_task():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    current_user = User.query.filter_by(username=session['user']).first()
    title = request.form.get('title')
    current_user.task_title = title
    current_user.task_status = 'Pending'
    db.session.commit()
    flash('Task Added Successfully!', 'success')
    return redirect(url_for('task_bp.view_task'))

@task_bp.route("/toggle_status", methods=['POST'])
def toggle_status():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    current_user = User.query.filter_by(username=session['user']).first()
    if current_user.task_status == 'Pending':
        current_user.task_status = 'Completed'
    else:
        current_user.task_status = 'Pending'
    db.session.commit()
    flash('Task status toggled successfully!', 'success')
    return redirect(url_for('task_bp.view_task'))

@task_bp.route("/clear_task", methods=['POST'])
def clear_task():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    current_user = User.query.filter_by(username=session['user']).first()
    current_user.task_title = None
    current_user.task_status = None
    db.session.commit()
    flash('Task cleared successfully!', 'success')
    return redirect(url_for('task_bp.view_task'))
