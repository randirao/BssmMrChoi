from data import books as book_repo

def add_book(title: str, author: str):
    return book_repo.insert_book(title, author)

def get_available_books():
    return book_repo.fetch_all_books()

def remove_book(book_id: int):
    return book_repo.delete_book(book_id)