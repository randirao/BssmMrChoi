from fastapi import FastAPI

from web import borrowings as borrowing_web
from web import books as books_web
from web import return_book as return_book_web

app = FastAPI()
app.include_router(borrowing_web.router)
app.include_router(books_web.router)
app.include_router(return_book_web.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host='0.0.0.0', reload=True)
