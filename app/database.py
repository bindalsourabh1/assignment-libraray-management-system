import sqlite3

def create_tables():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        published_date TEXT,
        is_available INTEGER DEFAULT 1
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS members (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        join_date TEXT NOT NULL
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS tokens (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        token TEXT NOT NULL UNIQUE,
        user TEXT NOT NULL
    )''')

    conn.commit()
    conn.close()

create_tables()
