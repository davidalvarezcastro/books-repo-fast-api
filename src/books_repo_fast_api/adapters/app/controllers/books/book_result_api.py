import uuid

from books_repo_fast_api.adapters.app.controllers.common.conversion_api_domain import ConversionAPIDomain


class BookResultAPI(ConversionAPIDomain):
    id: uuid.UUID
    title: str
    author: str
    description: str
    rating: int
    published_date: int
