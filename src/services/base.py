from typing import Any, Protocol
from abc import abstractmethod


class State(Protocol):

    @abstractmethod
    def set_state(self, key: str, value: str | Any) -> None:
        ...

    @abstractmethod
    def get_key(self, key: str, default: str = None) -> str | Any | None:
        ...
