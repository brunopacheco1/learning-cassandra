from app.domain.models import Author
from app.services.authors import AuthorService
from fastapi import APIRouter, status

router = APIRouter(
    prefix="/v1/authors",
    tags=["authors"],
)

service = AuthorService()

@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_author(author: Author) -> Author:
    return await service.add(author)

@router.get("/{name}", status_code=status.HTTP_200_OK)
async def get_author(name: str) -> Author:
    return await service.get(name)

@router.delete("/{name}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_author(name: str) -> None:
    await service.remove(name)

@router.get("/", status_code=status.HTTP_200_OK)
async def get_authors() -> list[Author]:
    return await service.list()
