from typing import TypeVar

import attr

T = TypeVar("T")


@attr.define
class PaginationDTO:
    page: int
    total_items: int
    page_items: int
    items: list[T]
