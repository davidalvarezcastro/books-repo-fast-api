from abc import abstractmethod

from books_repo_fast_api.adapters.repositories.repository_base import RepositoryBase
from books_repo_fast_api.domain.models.book import Book


class AbstractBooksRepository(RepositoryBase[Book]):
    @abstractmethod
    def get_by_title(self, title: str) -> Book:
        """Retrieve book by title."""
        raise NotImplementedError
