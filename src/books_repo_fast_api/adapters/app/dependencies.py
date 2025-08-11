from typing import Annotated

from fastapi.params import Depends

from books_repo_fast_api.adapters.repositories.data_context import DataContext
from books_repo_fast_api.domain.services.books.books_service import BooksService


def get_data_context() -> DataContext:
    return DataContext()


def get_books_service(
    data_context: Annotated[DataContext, Depends(get_data_context)],
) -> BooksService:
    return BooksService(data_context=data_context)
