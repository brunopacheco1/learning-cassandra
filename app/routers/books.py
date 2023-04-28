from app.dtos import BookRequest, BookResponse, book_dto
from app.models import Book
from app.exceptions import BookNotFound
from fastapi import APIRouter, status
from uuid import UUID
from cassandra.cqlengine.query import DoesNotExist

router = APIRouter(
    prefix="/v1/books",
    tags=["books"],
)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_book(book_to_add: BookRequest) -> BookResponse:
    book = Book.create(name=book_to_add.name)
    book.save()
    return book_dto(book)

@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_book(id: str) -> BookResponse:
    try:
        book: Book = Book.get(id=UUID(hex=id))
        return book_dto(book)
    except DoesNotExist:
        raise BookNotFound(id)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(id: str) -> None:
    try:
        book: Book = Book.get(id=UUID(hex=id))
        book.delete()
        pass
    except DoesNotExist:
        raise BookNotFound(id)

@router.get("/", status_code=status.HTTP_200_OK)
async def get_books() -> list[BookResponse]:
    return list(map(book_dto, Book.all()))
