from dataclasses import dataclass
from app.models import Author, Book
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
    author_id: UUID | None

@dataclass(frozen=True)
class AuthorRequest:
    name: str

@dataclass(frozen=True)
class AuthorResponse:
    id: UUID
    name: str

def author_dto(author: Author) -> AuthorResponse:
    return AuthorResponse(
        id=author.id,
        name=author.name,
    )

def book_dto(book: Book) -> BookResponse:
    return BookResponse(
        id=book.id,
        name=book.name,
        author_id=book.author_id
    )
