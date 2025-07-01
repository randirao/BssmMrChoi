

from fastapi import APIRouter
import service.borrower as service

router = APIRouter(prefix="/borrowers")

@router.get("/{borrower}/books")
def get_borrowed_books(borrower: str):
    return {"result": service.fetch_borrowed_books_by_borrower(borrower)}