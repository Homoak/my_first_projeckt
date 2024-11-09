import sqlite3

def add_column():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    try:
        # Додаємо новий стовпчик, якщо він ще не існує
        cursor.execute("ALTER TABLE users ADD COLUMN repl_password TEXT")
        connection.commit()
        print("Column 'repl_password' added successfully.")
    except sqlite3.OperationalError as e:
        # Може бути помилка, якщо стовпчик уже існує
        print(f"Error: {e}")
    finally:
        connection.close()

add_column()