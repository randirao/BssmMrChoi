from . import con, cur

def test():
    return "sqlite connect ok"

from datetime import datetime

def get_book_by_title(title: str):
    cur.execute("SELECT book_id, title, author, available FROM books WHERE title = ?", (title,))
    row = cur.fetchone()
    if row:
        return {
            "book_id": row[0],
            "title": row[1],
            "author": row[2],
            "available": row[3]
        }
    return None

def insert_borrowing(borrower: str, book_id: int):
    now = datetime.now().strftime("%Y-%m")
    cur.execute("INSERT INTO borrowings (borrower, book_id, borrow_month) VALUES (?, ?, ?)", (borrower, book_id, now))
    con.commit()

def set_book_unavailable(book_id: int):
    cur.execute("UPDATE books SET available = 0 WHERE book_id = ?", (book_id,))
    con.commit()