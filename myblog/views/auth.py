from flask import (
    render_template, Blueprint, flash, g, redirect, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash

from myblog.models.user import User

from myblog import db

import functools

auth = Blueprint('auth', __name__, url_prefix = '/auth')

#Register a User

@auth.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User(username, generate_password_hash(password))

        error = None
        if not username:
            error = 'Username required'
        elif not password:
            error = 'Password required'

        user_name = User.query.filter_by(username = username).first()
        if user_name == None:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        else:
            error = f'User {username} is already registered'
        flash(error)

    return render_template('auth/register.html')

#Login

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User(username, generate_password_hash(password))

        error = None

        user_name = User.query.filter_by(username = username).first()

        if user == None:
            error = 'Incorrect Username'
        elif not check_password_hash(user.password, password):
            error = 'Incorrect Password'

        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('blog.index'))
        
        flash(error)

    return render_template('auth/login.html')

@auth.before_app_request
def load_logger_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get_or_404(user_id)

@auth.route('/')
def logout():
    session.clear()
    return redirect(url_for('blog.index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view