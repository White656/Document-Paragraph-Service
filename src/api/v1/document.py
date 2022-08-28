import shutil
import docx2txt
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse

from api.v1.schemas import TaskRunInfo
from worker import create_task

router = APIRouter()


@router.post("/upload", summary="Рут для выгрузки файлов и последующей обработки")
async def create_upload_files(
        file: UploadFile = File(description="A file read as UploadFile", default=None)) -> TaskRunInfo:
    file_location = f"files/{file.filename}"
    print(file.content_type)
    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
    my_text = docx2txt.process(file_location)
    task = create_task.delay(text=my_text)
    return TaskRunInfo(id=task.id, file_path=file_location, text=my_text)


@router.get("/download/<file_path>", summary="Рут для выгрузки файлов")
async def download_file(file_path: str) -> FileResponse:
    return FileResponse(path=file_path, filename=file_path,
                        media_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
