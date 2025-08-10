import attr

from books_repo_fast_api.adapters.repositories.data_context import DataContext
from books_repo_fast_api.domain.models.base_model import FiltersBase
from books_repo_fast_api.domain.services.books.books_dtos import BookDTO
from books_repo_fast_api.domain.services.common.command_handler_base import CommandHandlerBase, PaginationQueryBase
from books_repo_fast_api.domain.services.common.pagination_dto import PaginationDTO


@attr.define
class GetBooksQueryFilters(FiltersBase):
    author: str | None = attr.field(default=None)
    rating: int | None = attr.field(default=None)


@attr.define
class GetBooksQuery(PaginationQueryBase):
    filters: GetBooksQueryFilters | None = attr.field(default=None)


@attr.define
class GetBooksQueryHandler(CommandHandlerBase):
    data_context: DataContext

    def handle(self, command: GetBooksQuery) -> PaginationDTO:
        books = self.data_context.books_repo.get(
            filters=command.filters,
            order=command.order,
            order_by=command.order_by,
            offset=command.offset,
            limit=command.items,
        )
        total_items = self.data_context.books_repo.count(filters=command.filters)

        books_dto = [BookDTO.from_model(book) for book in books]
        return PaginationDTO(page=command.page, page_items=len(books_dto), total_items=total_items, items=books_dto)
