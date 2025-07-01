from fastapi import APIRouter
from service import borrowings as service
from fastapi import Form, HTTPException

router = APIRouter(prefix="/borrows")

@router.get("")
def test():
    return service.test()

@router.post("")
def borrow_book(borrower: str = Form(...), title: str = Form(...)):
    result = service.borrow_book(borrower, title)
    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["error"])
    return {"message": "도서 대출 성공!"}