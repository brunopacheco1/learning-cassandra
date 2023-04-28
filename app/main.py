import uvicorn
from fastapi import FastAPI
from app.exceptions import BookNotFound, AuthorNotFound
from app.routers.books import router as books_router
from app.routers.authors import router as authors_router
from app.routers.exceptions import not_found_exception_handler, generic_exception_handler, bad_request_exception_handler
from app.database import get_session
from app.models import Book, Author
from cassandra.cqlengine.management import sync_table

app = FastAPI()

@app.on_event("startup")
def on_startup() -> None:
    get_session()
    sync_table(Author)
    sync_table(Book)
    pass

app.add_exception_handler(BookNotFound, not_found_exception_handler)
app.add_exception_handler(ValueError, bad_request_exception_handler)
app.add_exception_handler(AuthorNotFound, not_found_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

app.include_router(books_router)
app.include_router(authors_router)
