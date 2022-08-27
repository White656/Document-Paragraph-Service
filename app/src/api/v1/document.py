from fastapi import APIRouter, UploadFile, File

from api.v1.schemas import TaskRunInfo
from services.worker import create_task

router = APIRouter()


@router.post("/upload", summary="Рут для выгрузки файлов и последующей обработки")
async def create_upload_files(
        file: UploadFile = File(description="A file read as UploadFile", default=None)) -> TaskRunInfo:
    task = create_task.delay(filedata=file.filename)
    return TaskRunInfo(id=task.id)
