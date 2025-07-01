from data import borrowings

def process_return(borrower: str, title: str):
    success, message = borrowings.return_book(borrower, title)
    return {
        "success": success,
        "message": message
    }