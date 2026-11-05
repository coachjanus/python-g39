'''Todo Project: Top level module for todo application'''

from .cli import app  # pyright: ignore[reportMissingImports]


def main() -> None:
    app()
