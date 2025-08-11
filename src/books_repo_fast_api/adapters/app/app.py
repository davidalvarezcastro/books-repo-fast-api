from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from books_repo_fast_api.adapters.app.controllers.books.books_controller import BooksController
from books_repo_fast_api.adapters.app.middlewares.exceptions_middleware import ExceptionsMiddleware


def create_app() -> FastAPI:
    app = FastAPI(root_path="/api/v1", title="Books Repo API", version="0.0.1")

    BooksController().register_on_app(app=app, url_prefix="/books", tags=["Books"])

    ExceptionsMiddleware().register_on_app(app=app)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app
