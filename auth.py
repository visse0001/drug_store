from flask import render_template, request, session, redirect, flash, get_flashed_messages, Blueprint
from db_utils import get_connection
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        messages = get_flashed_messages()
        return render_template('login.html', messages=messages)

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_connection()
        c = conn.cursor()

        result = c.execute('SELECT * FROM users WHERE username = ?', (username,))
        user_data = result.fetchone()

        if user_data:
            hashed_password = user_data['password']

            if check_password_hash(hashed_password, password):
                session['username'] = user_data['username']
                return redirect('/')

        flash('Wrong login or password. Please try again.')
        return redirect('/login')


@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect('/login')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        messages = get_flashed_messages()
        return render_template('register.html', messages=messages)

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)
        password = hashed_password

        conn = get_connection()
        c = conn.cursor()

        c.execute('INSERT INTO users VALUES (NULL, ?, ?)', (username, password,))
        data_username = c.execute('SELECT username FROM users')
        conn.commit()

        if username == '' or password == '' or username in data_username:
            flash('Please try again. Enter your username and password.')
            return redirect('/register')
        else:
            return redirect('/')


def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if session:
            return view(*args, **kwargs)
        else:
            return redirect('/login')

    return wrapped_view
