from typing import List
from app.domain.models import Book
from app.services.books import BookService
from fastapi import APIRouter, status

router = APIRouter(
    prefix="/v1/books",
    tags=["books"],
)

service = BookService()

@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_book(book: Book) -> Book:
    return service.add(book)

@router.get("/{name}", status_code=status.HTTP_200_OK)
async def get_book(name: str) -> Book:
    return service.get(name)

@router.delete("/{name}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(name: str) -> None:
    service.remove(name)

@router.get("/", status_code=status.HTTP_200_OK)
async def get_books() -> List[Book]:
    return service.list()
