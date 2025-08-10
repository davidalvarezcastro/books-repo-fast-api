from abc import ABC, abstractmethod


class AbstractBooksRepository(ABC):
    @abstractmethod
    def get_all_books(self):
        """Retrieve all books from the repository."""
        raise NotImplementedError
