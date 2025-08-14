import uuid

import attr

from books_repo_fast_api.domain.services.books.base_dto import BaseDTO


@attr.define
class BookDTO(BaseDTO):
    id: uuid.UUID | None
    title: str
    author: str
    category: str
