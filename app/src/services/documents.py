from typing import Any

from services.base import FileManager


class DocumentService:
    ...


class DocXManager(FileManager):

    def save(self, file: object, path: str) -> str:
        raise NotImplementedError

    def read(self, filename: str, path: str) -> Any:
        raise NotImplementedError

    def delete(self, filename: str, path: str) -> bool:
        raise NotImplementedError
