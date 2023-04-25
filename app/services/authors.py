from typing import Dict, List
from app.domain.models import Author
from app.domain.exceptions import AuthorNotFoundException

class AuthorService:
    authors: Dict[str, Author]
    def __init__(self) -> None:
        self.authors = dict()

    def add(self, author: Author) -> Author:
        self.authors[author.name] = author
        return author

    def get(self, name: str) -> Author:
        if name not in self.authors:
            raise AuthorNotFoundException(name=name)
        return self.authors[name]
    
    def remove(self, name: str) -> None:
        if name not in self.authors:
            raise AuthorNotFoundException(name=name)
        del self.authors[name]

    def list(self) -> List[Author]:
        return list(self.authors.values())
