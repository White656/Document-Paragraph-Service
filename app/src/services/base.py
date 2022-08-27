from abc import ABC, abstractmethod

from aioredis import Redis
from pydantic import BaseModel


class ItemService(ABC):
    def __init__(self, redis: Redis):
        self.redis = redis

    @staticmethod
    @abstractmethod
    def model(*args, **kwargs) -> BaseModel:
        ...

    async def get_by_id(self, pk: str):

        data = await self._from_cache(pk)  # пытаемся получить данные из кеша
        if not data:  # если они не найдены, то получаем их из elasticsearch

            return None

        await self._put_to_cache(data)  # записываем данные в кеш
        return data

    async def _from_cache(self, pk: str):
        data = await self.redis.get(pk)  # получаем данные из redis

        if not data:  # если данных не оказалось, то возвращаем None
            return None

        data = self.model.parse_raw(data)  # переводим данные в удобный формат

        return data  # возвращаем данные

    async def _put_to_cache(self, item):
        # вставляем данные в redis
        await self.redis.set(item.id, item.json())
