from cache.borrower import get_borrowed_books

def fetch_borrowed_books_by_borrower(borrower: str) -> dict:
    books = get_borrowed_books(borrower)
    return {
        "borrower": borrower,
        "books": books
    }
