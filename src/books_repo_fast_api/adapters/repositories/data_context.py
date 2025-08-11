import attrs

from books_repo_fast_api.adapters.repositories.books_repository import BooksRepository
from books_repo_fast_api.domain.repositories.books_repository import AbstractBooksRepository


@attrs.define
class DataContext:
    books_repo: AbstractBooksRepository = attrs.field(init=False)

    def __attrs_post_init__(self):
        self.books_repo = BooksRepository()
