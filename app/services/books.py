from app.domain.models import Book
from app.domain.exceptions import BookNotFoundException

class BookService:
    books: dict[str, Book]
    def __init__(self) -> None:
        self.books = {}

    async def add(self, book: Book) -> Book:
        self.books[book.name] = book
        return book

    async def get(self, name: str) -> Book:
        if name not in self.books:
            raise BookNotFoundException(name)
        return self.books[name]
    
    async def remove(self, name: str) -> None:
        if name not in self.books:
            raise BookNotFoundException(name)
        del self.books[name]

    async def list(self) -> list[Book]:
        return list(self.books.values())
