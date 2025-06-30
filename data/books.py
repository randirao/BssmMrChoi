import sqlite3

conn = sqlite3.connect("mydb.db", check_same_thread=False)
cursor = conn.cursor()

def insert_book(title: str, author: str):
    try:
        cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
        conn.commit()
        return {"success": True}
    except Exception as e:
        return {"success": False, "error": str(e)}

def fetch_all_books():
    cursor.execute("SELECT id, title, author FROM books")
    rows = cursor.fetchall()
    return [{"id": row[0], "title": row[1], "author": row[2]} for row in rows]