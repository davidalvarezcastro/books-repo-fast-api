import attrs

from books_repo_fast_api.adapters.repositories.data_context import DataContext
from books_repo_fast_api.domain.services.books.queries.get_books import GetBooksQuery, GetBooksQueryHandler
from books_repo_fast_api.domain.services.common.pagination_dto import PaginationDTO


@attrs.define
class BooksService:
    data_context: DataContext

    def get_books(self, get_books_query: GetBooksQuery) -> PaginationDTO:
        return GetBooksQueryHandler(data_context=self.data_context).handle(command=get_books_query)
