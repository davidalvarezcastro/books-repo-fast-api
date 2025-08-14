import uuid

import attrs

from books_repo_fast_api.domain.models.base_model import BaseModel


@attrs.define
class Book(BaseModel):
    title: str
    author: str
    category: str

    def __attrs_post_init__(self):
        self.id = str(uuid.uuid4())
