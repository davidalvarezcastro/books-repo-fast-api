import attrs

from books_repo_fast_api.domain.models.base_model import BaseModel


@attrs.define
class Book(BaseModel):
    title: str
    author: str
    description: str
    rating: int
    published_date: int
