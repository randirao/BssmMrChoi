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
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cur.execute("INSERT INTO borrowings (borrower, book_id, borrow_at) VALUES (?, ?, ?)", (borrower, book_id, now))
    con.commit()

def set_book_unavailable(book_id: int):
    cur.execute("UPDATE books SET available = 0 WHERE book_id = ?", (book_id,))
    con.commit()

def return_book(borrower: str, title: str):
    cur.execute("SELECT book_id FROM books WHERE title = ?", (title,))
    book = cur.fetchone()
    if not book:
        return False, "해당 도서를 찾을 수 없습니다."
    book_id = book[0]

    cur.execute("SELECT id FROM borrowings WHERE borrower = ? AND book_id = ? AND return_at IS NULL", (borrower, book_id))
    borrowing = cur.fetchone()
    if not borrowing:
        return False, "반납할 대출 기록이 없습니다."

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cur.execute("UPDATE borrowings SET return_at = ? WHERE id = ?", (now, borrowing[0]))
    cur.execute("UPDATE books SET available = 1 WHERE book_id = ?", (book_id,))
    con.commit()
    return True, "반납이 완료되었습니다."

def get_borrowings_by_month(borrow_month: str):
    cur.execute("""
        SELECT b.borrower, bk.title, bk.author
        FROM borrowings b
        JOIN books bk ON b.book_id = bk.book_id
        WHERE strftime('%Y-%m', b.borrow_at) = ?
    """, (borrow_month,))
    rows = cur.fetchall()
    return [{"borrower": r[0], "title": r[1], "author": r[2]} for r in rows]