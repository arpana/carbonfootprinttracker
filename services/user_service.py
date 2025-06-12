from datetime import datetime
import bcrypt
from models.users import User
from database import get_connection

class UserService:
    # existing methods...

    @staticmethod
    def register(user: User):
        try:
            hashed_pw = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
            now = datetime.now().isoformat()
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO users (email, password, createdby, createdat, updatedby, updatedat)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (user.email, hashed_pw, user.email, now, user.email, now))
            conn.commit()
            return True, "User registered successfully."
        except sqlite3.IntegrityError:
            return False, "Email already registered."
        except Exception as e:
            return False, f"Error: {e}"
        finally:
            conn.close()

    @staticmethod
    def login(email: str, password: str):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM users WHERE email = ?", (email,))
        row = cursor.fetchone()
        conn.close()

        if row and bcrypt.checkpw(password.encode('utf-8'), row[0]):
            return True, "Login successful."
        else:
            return False, "Invalid email or password."

    @staticmethod
    def update_password(email: str, new_password: str):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM users WHERE email = ?", (email,))
        if cursor.fetchone():
            hashed_pw = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
            now = datetime.now().isoformat()
            cursor.execute("""
                UPDATE users SET password = ?, updatedby = ?, updatedat = ? WHERE email = ?
            """, (hashed_pw, email, now, email))
            conn.commit()
            return True, "Password updated."
        else:
            return False, "Email not found."
        conn.close()
