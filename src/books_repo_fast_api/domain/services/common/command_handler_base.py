from abc import ABC, abstractmethod
from typing import TypeVar

import attr

from books_repo_fast_api.domain.models.base_model import SortDirection

T = TypeVar("T")


@attr.define
class CommandBase:
    pass


@attr.define
class PaginationQueryBase(CommandBase):
    order: SortDirection = SortDirection.NONE
    order_by: str | None = None
    page: int = attr.field(default=1, validator=[attr.validators.ge(1)])
    items: int = attr.field(default=100, validator=[attr.validators.ge(1), attr.validators.le(100)])

    @property
    def offset(self):
        return (self.page - 1) * self.items


@attr.define
class CommandHandlerBase(ABC):
    @abstractmethod
    def handle(self, command: CommandBase) -> T:
        pass
