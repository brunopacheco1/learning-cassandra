from app.domain.dtos import AuthorRequest, AuthorResponse
from app.services.authors import AuthorService
from fastapi import Depends, APIRouter, status
from typing import Annotated

router = APIRouter(
    prefix="/v1/authors",
    tags=["authors"],
)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_author(author: AuthorRequest, service: Annotated[AuthorService, Depends(AuthorService)]) -> AuthorResponse:
    return await service.add(author)

@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_author(id: str, service: Annotated[AuthorService, Depends(AuthorService)]) -> AuthorResponse:
    return await service.get(id)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_author(id: str, service: Annotated[AuthorService, Depends(AuthorService)]) -> None:
    await service.remove(id)
    pass

@router.get("/", status_code=status.HTTP_200_OK)
async def get_authors(service: Annotated[AuthorService, Depends(AuthorService)]) -> list[AuthorResponse]:
    return await service.list()

@router.patch("/{id}/books/{bookId}", status_code=status.HTTP_200_OK)
async def add_book_to_author(id: str, bookId: str, service: Annotated[AuthorService, Depends(AuthorService)]) -> AuthorResponse:
    return await service.add_book(id, bookId)
