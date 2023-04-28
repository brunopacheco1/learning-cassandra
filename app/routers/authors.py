from app.dtos import AuthorRequest, AuthorResponse, BookResponse, author_dto, book_dto
from app.models import Author, Book
from app.exceptions import AuthorNotFound, BookNotFound
from fastapi import APIRouter, status
from uuid import UUID
from cassandra.cqlengine.query import DoesNotExist

router = APIRouter(
    prefix="/v1/authors",
    tags=["authors"],
)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_author(author_to_add: AuthorRequest) -> AuthorResponse:
    author = Author.create(name=author_to_add.name)
    author.save()
    return author_dto(author)

@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_author(id: str) -> AuthorResponse:
    try:
        author: Author = Author.get(id=UUID(hex=id))
        return author_dto(author)
    except DoesNotExist:
        raise AuthorNotFound(id)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_author(id: str) -> None:
    try:
        author: Author = Author.get(id=UUID(hex=id))
        books: list[Book] = Book.filter(author_id=author.id).all()
        for book in books: book.delete()
        author.delete()
        pass
    except DoesNotExist:
        raise AuthorNotFound(id)

@router.get("/", status_code=status.HTTP_200_OK)
async def get_authors() -> list[AuthorResponse]:
    return list(map(author_dto, Author.all()))

@router.get("/{id}/books", status_code=status.HTTP_200_OK)
async def add_book_to_author(id: str) -> list[BookResponse]:
    try:
        author: Author = Author.get(id=UUID(hex=id))
        books = Book.filter(author_id=author.id).all()
        return list(map(book_dto, books))
    except DoesNotExist:
        raise AuthorNotFound(id)

@router.patch("/{id}/books/{book_id}", status_code=status.HTTP_201_CREATED)
async def add_book_to_author(id: str, book_id: str) -> BookResponse:
    author: Author
    try:
        author = Author.get(id=UUID(hex=id))
    except DoesNotExist:
        raise AuthorNotFound(id)
    
    book: Book
    try:
        book = Book.get(id=UUID(hex=book_id))
    except DoesNotExist:
        raise BookNotFound(id)
    
    book.author_id = author.id

    book.update()

    return book_dto(book)
