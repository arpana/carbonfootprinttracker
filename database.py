import sqlite3


def get_connection():
    # Use project-local SQLite file
    return sqlite3.connect(
        "/Users/achopra/Documents/CarbonFootPrintTracker/carbonfootprinttracker-4/users.db"
    )


def init_db():
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                createdby TEXT,
                createdat DATETIME,
                updatedby TEXT,
                updatedat DATETIME
            )
            """
        )
        conn.commit()
    finally:
        conn.close()