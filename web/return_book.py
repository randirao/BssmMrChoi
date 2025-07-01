from fastapi import APIRouter, Form, HTTPException
from service import return_book as return_service

router = APIRouter(prefix="/returns")

@router.post("")
def return_book(borrower: str = Form(...), title: str = Form(...)):
    result = return_service.process_return(borrower, title)
    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["message"])
    return {"message": result["message"]}