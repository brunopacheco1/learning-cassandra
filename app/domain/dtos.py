from dataclasses import dataclass, field
from app.domain.models import Author, Book
from uuid import UUID

@dataclass(frozen=True)
class ExceptionResponse:
    message: str
    className: str
    capturedAt: str

@dataclass(frozen=True)
class BookRequest:
    name: str

@dataclass(frozen=True)
class BookResponse:
    id: UUID
    name: str

@dataclass(frozen=True)
class AuthorRequest:
    name: str

@dataclass(frozen=True)
class AuthorResponse:
    id: UUID
    name: str
    books: list[BookResponse] = field(default_factory=list)

def author_dto(author: Author) -> AuthorResponse:
    return AuthorResponse(
        id=author.id,
        name=author.name,
        books=list(map(book_dto, author.books.values())),
    )

def book_dto(book: Book) -> BookResponse:
    return BookResponse(
        id=book.id,
        name=book.name,
    )
