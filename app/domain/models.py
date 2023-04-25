from dataclasses import dataclass
from typing import Dict

@dataclass(frozen=True)
class Book:
    name: str

@dataclass(frozen=True)
class Author:
    name: str
    books: Dict[str, Book]
