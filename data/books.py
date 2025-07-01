from data import con, cur

def insert_book(title: str, author: str):
    try:
        cur.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
        con.commit()
        return {"success": True}
    except Exception as e:
        return {"success": False, "error": str(e)}

def fetch_all_books():
    cur.execute("SELECT book_id, title, author FROM books")
    rows = cur.fetchall()
    return [{"id": row[0], "title": row[1], "author": row[2]} for row in rows]

def delete_book(book_id: int):
    try:
        cur.execute("DELETE FROM books WHERE book_id = ?", (book_id,))
        con.commit()
        if cur.rowcount == 0:
            return {"success": False, "error": "해당 도서가 존재하지 않습니다."}
        return {"success": True}
    except Exception as e:
        return {"success": False, "error": str(e)}