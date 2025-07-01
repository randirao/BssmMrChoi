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