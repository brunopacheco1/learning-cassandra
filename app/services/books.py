from app.domain.models import Book
from app.domain.repositories import books_repository
from app.domain.dtos import BookRequest, BookResponse, book_dto
from app.domain.exceptions import BookNotFoundException
from uuid import uuid4, UUID
from fastapi import Depends

class BookService:

    books: dict[UUID, Book]

    def __init__(self, books = Depends(books_repository)) -> None:
        self.books = books
        pass

    async def add(self, book_to_add: BookRequest) -> BookResponse:
        book = Book(id=uuid4(), name=book_to_add.name)
        self.books[book.id] = book
        return book_dto(book)

    async def get(self, id: str) -> BookResponse:
        book = await self.get_entity(id)
        return book_dto(book)

    async def get_entity(self, id: str) -> Book:
        key = UUID(hex=id)
        if key not in self.books:
            raise BookNotFoundException(id)
        return self.books[key]

    async def remove(self, id: str) -> None:
        key = UUID(hex=id)
        if key not in self.books:
            raise BookNotFoundException(id)
        del self.books[key]
        pass

    async def list(self) -> list[BookResponse]:
        return list(map(book_dto, self.books.values()))
