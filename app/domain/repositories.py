from app.domain.models import Author, Book
from uuid import UUID

authors: dict[UUID, Author] = {}

async def authors_repository() -> dict[UUID, Author]:
    return authors

books: dict[UUID, Book] = {}

async def books_repository() -> dict[UUID, Book]:
    return books
