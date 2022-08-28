import shutil
from functools import lru_cache

import docx2txt
from fastapi import UploadFile

from services.mixin import ReaderMixin, SaverMixin


class DocXService(ReaderMixin, SaverMixin):

    def save(self, file: UploadFile, file_location: str) -> None:
        with open(file_location, 'wb+') as file_object:
            shutil.copyfileobj(file.file, file_object)

    def read(self, file_location: str) -> str:
        return docx2txt.process(file_location)


@lru_cache()
def get_docx_service() -> DocXService:
    return DocXService()
