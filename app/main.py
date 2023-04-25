from app.domain.exceptions import BookNotFoundException, AuthorNotFoundException
from fastapi import FastAPI
from app.routers.books import router as books_router
from app.routers.authors import router as authors_router
from app.routers.exceptions import not_found_exception_handler, generic_exception_handler

app = FastAPI()

app.add_exception_handler(BookNotFoundException, not_found_exception_handler)
app.add_exception_handler(AuthorNotFoundException, not_found_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

app.include_router(books_router)
app.include_router(authors_router)
