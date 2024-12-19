import secrets
import sqlite3
from typing import Optional

DATABASE = "library.db"

class Auth:
    @staticmethod
    def generate_token(user: str) -> str:
        token = secrets.token_hex(16)
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO tokens (token, user) VALUES (?, ?)''', (token, user))
        conn.commit()
        conn.close()
        return token

    @staticmethod
    def verify_token(token: str) -> bool:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM tokens WHERE token = ?''', (token,))
        result = cursor.fetchone()
        conn.close()
        return result is not None
