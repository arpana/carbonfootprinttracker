import sqlite3

def get_connection():
    return sqlite3.connect("/Users/achopra/carbontracker")

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users1 (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        createdby TEXT,
        createdat DATETIME,
        updatedby TEXT,
        updatedat DATETIME
    )
    """)
    conn.commit()
    conn.close()