from fastapi import FastAPI

from web import borrowings as borrow_web
from web import books
from web import borrowings

app = FastAPI()
app.include_router(borrow_web.router)
app.include_router(books.router)
app.include_router(borrowings.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host='0.0.0.0', reload=True)
