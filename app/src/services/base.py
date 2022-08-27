from typing import Any

from typing import Protocol
from abc import abstractmethod, ABC


class State(Protocol):

    @abstractmethod
    def set_state(self, key: str, value: str | Any) -> None:
        ...

    @abstractmethod
    def get_key(self, key: str, default: str = None) -> str | Any | None:
        ...


class FileManager(ABC):

    @abstractmethod
    def save(self, file: object, path: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def read(self, filename: str, path: str) -> Any:
        raise NotImplementedError

    @abstractmethod
    def delete(self, filename: str, path: str) -> bool:
        raise NotImplementedError
