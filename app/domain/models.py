from dataclasses import dataclass, field
from uuid import UUID

@dataclass(frozen=True)
class Book:
    id: UUID
    name: str

@dataclass(frozen=True)
class Author:
    id: UUID
    name: str
    books: dict[UUID, Book] = field(default_factory=dict)
