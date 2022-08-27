import backoff
from aioredis import Redis

from core.config import backoff_config
from models.document import Document
from services.base import State
from typing import Any


class RedisStateService(State):
    """
    :param redis
    Класс реализует взаимодействие с хранилищем Redis. Чтение и запись.
    """

    def __init__(self, redis: Redis) -> None:
        self._redis = redis

    @backoff.on_exception(**backoff_config)
    def get_key(self, key: str) -> str | Any | None:
        data = await self._redis.get(key)
        return data.decode() if data else None

    @backoff.on_exception(**backoff_config)
    def set_state(self, key: str, value: Document | str) -> None:
        await self._redis.set(key, value.json() if isinstance(value, Document) else value)
