from abc import abstractmethod
from typing import ClassVar, TypeVar

import attr

from books_repo_fast_api.domain.models.base_model import FiltersBase, SortDirection
from books_repo_fast_api.domain.repositories.repository_base import AbstractRepository

K = TypeVar("K", bound=dict)
T = TypeVar("T")


@attr.define
class RepositoryBase[T](AbstractRepository):
    data: ClassVar[list[T]] = []

    @abstractmethod
    def _orm_to_domain_model(self, entity_orm: K) -> T:
        pass

    def get(
        self,
        filters: FiltersBase | None = None,
        order: SortDirection = SortDirection.NONE,
        order_by: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
    ) -> list[T]:
        data = self.data

        if filters:
            predicate = filters.get_predicate()
            if predicate:
                data = [b for b in data if predicate(b)]

        if order_by:
            reverse = order == SortDirection.DESC
            data = sorted(data, key=lambda b: b.get(order_by), reverse=reverse)

        if offset:
            data = data[offset:]
        if limit:
            data = data[:limit]

        return [self._orm_to_domain_model(b) for b in data]

    def count(
        self,
        filters: FiltersBase | None = None,
    ) -> int:
        data = self.data
        if filters:
            predicate = filters.get_predicate()
            if predicate:
                data = [b for b in data if predicate(b)]
        return len(data)
