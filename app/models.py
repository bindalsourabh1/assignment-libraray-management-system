import sqlite3
from typing import List, Dict, Union

DATABASE = "library.db"

class Book:
    @staticmethod
    def create_book(data: Dict[str, Union[str, int]]) -> int:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO books (title, author, published_date, is_available) 
                          VALUES (?, ?, ?, ?)''', 
                       (data["title"], data["author"], data["published_date"], 1))
        conn.commit()
        book_id = cursor.lastrowid
        conn.close()
        return book_id

    @staticmethod
    def get_books(offset=0, limit=10, search=None) -> List[Dict]:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        query = "SELECT * FROM books WHERE 1=1"
        params = []

        if search:
            query += " AND (title LIKE ? OR author LIKE ?)"
            params.extend([f"%{search}%", f"%{search}%"])

        query += " LIMIT ? OFFSET ?"
        params.extend([limit, offset])
        
        cursor.execute(query, params)
        books = cursor.fetchall()
        conn.close()
        return [{"id": b[0], "title": b[1], "author": b[2], "published_date": b[3], "is_available": b[4]} for b in books]

    @staticmethod
    def update_book(book_id: int, data: Dict[str, Union[str, int]]) -> bool:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''UPDATE books 
                          SET title=?, author=?, published_date=?, is_available=? 
                          WHERE id=?''',
                       (data["title"], data["author"], data["published_date"], data["is_available"], book_id))
        conn.commit()
        updated = cursor.rowcount > 0
        conn.close()
        return updated

    @staticmethod
    def delete_book(book_id: int) -> bool:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM books WHERE id= ?", (book_id,))
        conn.commit()
        deleted = cursor.rowcount > 0
        conn.close()
        return deleted
