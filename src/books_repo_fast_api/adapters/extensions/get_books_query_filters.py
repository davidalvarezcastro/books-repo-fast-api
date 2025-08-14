from books_repo_fast_api.domain.services.books.queries.get_books import GetBooksQueryFilters


def get_predicate(self: GetBooksQueryFilters):
    def predicate(book: dict):
        if self.author and self.author.lower() != book["author"].lower():
            return False
        if self.category and self.category.lower() != book["category"].lower():
            return False
        return True

    return predicate


GetBooksQueryFilters.get_predicate = get_predicate
