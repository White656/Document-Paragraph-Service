from abc import ABC, abstractmethod
from typing import Any


class SaverMixin(ABC):

    @abstractmethod
    def save(self, file: Any, file_location: str) -> None:
        raise NotImplementedError


class ReaderMixin(ABC):

    @abstractmethod
    def read(self, file_location: str) -> Any:
        raise NotImplementedError


class DeleteMixin(ABC):

    @abstractmethod
    def delete(self, file: any, file_location: str) -> Any:
        raise NotImplementedError
