import uuid

import attr

from books_repo_fast_api.domain.services.books.base_dto import BaseDTO


@attr.define
class BookDTO(BaseDTO):
    title: str
    author: str
    description: str
    rating: int
    published_date: int
