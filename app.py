import sqlite3

from flask import Flask, render_template, request, redirect, url_for, flash, g
from werkzeug.security import generate_password_hash
#===========================
#imports
#===========================
app = Flask(__name__)
app.secret_key = ''

DATABASE = 'database.db'


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.before_request
def before_request():
    get_db()


@app.teardown_appcontext
def close_db(error):
    db = g.pop('db', None)
    if db is not None:
        db.close()


@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/admin')
def amin():
    return render_template('admin.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/home')
def home():
    db = get_db()
    result = db.execute('SELECT name FROM users WHERE id = 1').fetchone()
    if result:
        name = result['name']  # Доступ по имени колонки благодаря row_factory
        return f'Имя: {name}'
    return 'Имя не найдено'
    return render_template('home.html')


@app.route('/cabinet')
def cabinet():
    return render_template('cabinet.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/news')
def hello():
    return render_template('news.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        repl_password = request.form.get('repl_password')

        # Перевірка заповнення полів і збігу паролів
        if not all([name, email, password, repl_password]):
            flash('Please fill in all the fields', 'error')
        elif password != repl_password:
            flash('Passwords do not match', 'error')
        else:
            try:
                db = get_db()
                # Перевірка на наявність користувача з таким же email
                cursor = db.execute("SELECT id FROM users WHERE email = ?", (email,))
                if cursor.fetchone():
                    flash('Email is already registered', 'error')
                else:
                    # Хешування пароля
                    hashed_password = generate_password_hash(password, method='scrypt')
                    hashed_repl_password = generate_password_hash(repl_password, method='scrypt')

                    # Вставка даних в базу
                    db.execute("INSERT INTO users (name, email, password, repl_password) VALUES (?, ?, ?, ?)",
                               (name, email, hashed_password, hashed_repl_password))
                    db.commit()
                    flash('Registration successful', 'success')
                    return redirect(url_for('home'))
            except sqlite3.Error as e:
                flash(f"An error occurred: {e}", 'error')


    return render_template('register.html')


if __name__ == "__main__":
    app.run(port=19019, debug=True)
