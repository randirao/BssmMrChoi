from fastapi import APIRouter, HTTPException, Form
from service import books
router = APIRouter()

@router.post("/books")
def register_book(
        title: str = Form(...),
        author: str = Form(...)):
    result = books.add_book(title, author)
    if not result["success"]:
        raise HTTPException(status_code=500, detail=result["error"])
    return {"message": "도서 등록 성공!"}

@router.get("/books")
def list_books():
    return books.get_available_books()

@router.delete("/books/{book_id}")
def delete_book(book_id: int):
    result = books.remove_book(book_id)
    if not result["success"]:
        raise HTTPException(status_code=404, detail=result["error"])
    return {"message": "도서 삭제 성공!"}