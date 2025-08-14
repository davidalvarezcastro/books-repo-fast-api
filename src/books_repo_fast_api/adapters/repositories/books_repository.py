import logging
from typing import ClassVar

import attrs

from books_repo_fast_api.domain.models.book import Book
from books_repo_fast_api.domain.repositories.books_repository import AbstractBooksRepository

BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "science"},
    {"title": "david", "author": "Author Three", "category": "science"},
    {"title": "Title Two", "author": "david", "category": "science"},
    {"title": "Title Four", "author": "Author Four", "category": "math"},
    {"title": "Title Five", "author": "Author Five", "category": "math"},
    {"title": "Title Six", "author": "Author Two", "category": "math"},
]


@attrs.define
class BooksRepository(AbstractBooksRepository):
    data: ClassVar[list[dict]] = BOOKS

    def _orm_to_domain_model(self, entity_orm: dict) -> Book:
        book = Book(**entity_orm)
        logging.error(book)
        return Book(**entity_orm)

    def get_by_title(self, title: str) -> Book:
        for book in self.data:
            if book["title"] == title:
                return Book(**book)
        return None
