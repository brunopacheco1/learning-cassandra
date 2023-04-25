from app.domain.models import Author
from app.domain.exceptions import AuthorNotFoundException

class AuthorService:
    authors: dict[str, Author]
    def __init__(self) -> None:
        self.authors = {}

    async def add(self, author: Author) -> Author:
        self.authors[author.name] = author
        return author

    async def get(self, name: str) -> Author:
        if name not in self.authors:
            raise AuthorNotFoundException(name)
        return self.authors[name]
    
    async def remove(self, name: str) -> None:
        if name not in self.authors:
            raise AuthorNotFoundException(name)
        del self.authors[name]

    async def list(self) -> list[Author]:
        return list(self.authors.values())
