from app.domain.repositories import authors_repository
from app.services.books import BookService
from app.domain.models import Author, Book
from app.domain.dtos import AuthorRequest, AuthorResponse, author_dto
from app.domain.exceptions import AuthorNotFoundException, BookNotFoundException
from uuid import uuid4, UUID
from fastapi import Depends

class AuthorService:
    
    book_service: BookService
    authors: dict[UUID, Author]

    def __init__(self, authors = Depends(authors_repository), book_service = Depends(BookService)) -> None:
        self.authors = authors
        self.book_service = book_service
        pass

    async def add(self, author_to_add: AuthorRequest) -> AuthorResponse:
        author = Author(id=uuid4(), name=author_to_add.name)
        self.authors[author.id] = author
        return author_dto(author)

    async def get(self, id: str) -> AuthorResponse:
        author = await self.get_entity(id)
        return author_dto(author)

    async def get_entity(self, id: str) -> Author:
        key = UUID(hex=id)
        if key not in self.authors:
            raise AuthorNotFoundException(id)
        return self.authors[key]
    
    async def remove(self, id: str) -> None:
        key = UUID(hex=id)
        if key not in self.authors:
            raise AuthorNotFoundException(id)
        del self.authors[key]
        pass

    async def list(self) -> list[AuthorResponse]:
        return list(map(author_dto, self.authors.values()))

    async def add_book(self, id: str, bookId: str) -> AuthorResponse:
        author = await self.get_entity(id)
        book = await self.book_service.get_entity(bookId)
        author.books[book.id] = book
        return author_dto(author)
