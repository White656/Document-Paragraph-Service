from pydantic import BaseModel

from models.base import AbstractModel


class ResultProcessing(BaseModel):
    name: str
    percent: int
    is_true: bool


class Document(AbstractModel):
    file_url: str
    percent: int
    result: list[ResultProcessing]
