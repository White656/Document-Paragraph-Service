import backoff
from aioredis import Redis

from core.config import RedisConfig, backoff_config
from services.base import State
from typing import final, Any, Optional


@final
class RedisState(State):
    """
    :param config базовая конфигурация redis
    :param connection опционально, подключение к redis


    Класс реализует взаимодействие с хранилищем Redis. Чтение и запись.
    """

    def __init__(self, config: RedisConfig, connection: Optional[Redis] = None) -> None:
        self._config = config
        self._connection = connection

    @property
    def _redis_connection(self) -> Redis:
        if not self._connection or not self._connection.ping():
            self._connection = self._create_connection()
        return await self._connection

    @backoff.on_exception(**backoff_config)
    def _create_connection(self) -> Redis:
        return Redis(**self._config.dict())

    @backoff.on_exception(**backoff_config)
    def get_key(self, key: str) -> str | Any | None:
        data = await self._redis_connection.get(key)
        return data.decode() if data else None

    @backoff.on_exception(**backoff_config)
    def set_state(self, key: str, value: str | Any) -> None:
        await self._redis_connection.set(key, value.encode())
