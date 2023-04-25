from typing import Dict, List
from app.domain.models import Book
from app.domain.exceptions import BookNotFoundException

class BookService:
    books: Dict[str, Book]
    def __init__(self) -> None:
        self.books = dict()

    def add(self, book: Book) -> Book:
        raise Exception("rest")
        self.books[book.name] = book
        return book

    def get(self, name: str) -> Book:
        if name not in self.books:
            raise BookNotFoundException(name=name)
        return self.books[name]
    
    def remove(self, name: str) -> None:
        if name not in self.books:
            raise BookNotFoundException(name=name)
        del self.books[name]

    def list(self) -> List[Book]:
        return list(self.books.values())
