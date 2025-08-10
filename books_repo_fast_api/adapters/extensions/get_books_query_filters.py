from books_repo_fast_api.domain.services.books.queries.get_books import GetBooksQueryFilters


def get_predicate(self: GetBooksQueryFilters):  # noqa: ARG001
    return None


GetBooksQueryFilters.get_predicate = get_predicate
