import orjson

from pydantic import BaseModel

from app.src.models.base import orjson_dumps


class UUIDMixing(BaseModel):
    id: str

    class Config:
        # Заменяем стандартную работу с json на более быструю
        json_loads = orjson.loads
        json_dumps = orjson_dumps
