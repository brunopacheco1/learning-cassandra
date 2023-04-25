from app.domain.dtos import BookRequest, BookResponse
from app.services.books import BookService
from fastapi import Depends, APIRouter, status
from typing import Annotated

router = APIRouter(
    prefix="/v1/books",
    tags=["books"],
)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_book(book: BookRequest, service: Annotated[BookService, Depends(BookService)]) -> BookResponse:
    return await service.add(book)

@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_book(id: str, service: Annotated[BookService, Depends(BookService)]) -> BookResponse:
    return await service.get(id)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(id: str, service: Annotated[BookService, Depends(BookService)]) -> None:
    await service.remove(id)
    pass

@router.get("/", status_code=status.HTTP_200_OK)
async def get_books(service: Annotated[BookService, Depends(BookService)]) -> list[BookResponse]:
    return await service.list()
