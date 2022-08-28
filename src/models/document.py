from typing import Any

from models.base import AbstractModel


class CeleryTaskInfo(AbstractModel):
    id: str
    status: Any
    result: Any