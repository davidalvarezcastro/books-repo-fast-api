from typing import Annotated

import attrs
from fastapi import APIRouter, Depends, status

from books_repo_fast_api.adapters.app.controllers.books.book_result_api import BookResultAPI
from books_repo_fast_api.adapters.app.controllers.common.base_controller import BaseController
from books_repo_fast_api.adapters.app.controllers.common.conversion_api_domain import ConversionAPIDomain
from books_repo_fast_api.adapters.app.controllers.common.pagination_api import PaginationFiltersAPI, PaginationResultAPI
from books_repo_fast_api.adapters.app.dependencies import get_books_service
from books_repo_fast_api.domain.services.books.books_service import BooksService
from books_repo_fast_api.domain.services.books.queries.get_books import GetBooksQuery


class GetBooksFiltersAPI(ConversionAPIDomain):
    author: str | None = None
    rating: int | None = None


@attrs.define
class BooksController(BaseController):
    def _add_url_rules(self, controller: APIRouter) -> None:
        @controller.post(
            "/",
            status_code=status.HTTP_200_OK,
        )
        def get_users(
            body: PaginationFiltersAPI[GetBooksFiltersAPI],
            books_service: Annotated[BooksService, Depends(get_books_service)],
        ) -> PaginationResultAPI[BookResultAPI]:
            get_books_query = body.to_domain(GetBooksQuery)
            users = books_service.get_books(get_books_query=get_books_query)
            return PaginationResultAPI.from_domain(users)
