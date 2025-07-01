from data import borrowings as data
from cache import borrower as cache
from data.borrowings import get_borrowings_by_month


def test():
    db_test = data.test()
    redis_test = cache.test()
    return {"sqlite": db_test, "redis": redis_test}

def borrow_book(borrower: str, title: str):
    book = data.get_book_by_title(title)
    if not book or book["available"] == 0:
        return {"success": False, "error": "대출할 수 없는 도서입니다."}

    try:
        data.insert_borrowing(borrower, book["book_id"])
        data.set_book_unavailable(book["book_id"])
        return {"success": True}
    except Exception as e:
        return {"success": False, "error": str(e)}

def fetch_borrowings_by_month(borrow_month: str):
    return get_borrowings_by_month(borrow_month)