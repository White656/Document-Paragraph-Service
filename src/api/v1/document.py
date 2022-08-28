from fastapi import APIRouter, UploadFile, File, Depends
from fastapi.responses import FileResponse

from api.v1.schemas import TaskRunInfo
from services.documents import get_docx_service, DocXService
from worker import create_task

router = APIRouter()


@router.post("/upload", summary="Рут для выгрузки файлов и последующей обработки")
async def create_upload_files(
        file: UploadFile = File(description="A file read as UploadFile", default=None),
        docx_service: DocXService = Depends(get_docx_service)) -> TaskRunInfo:
    file_location = f"files/{file.filename}"
    docx_service.save(file=file, file_location=file_location)
    my_text = docx_service.read(file_location)
    task = create_task.delay(text=my_text)
    return TaskRunInfo(id=task.id, file_path=file_location, text=my_text)


@router.get("/download/<file_path>", summary="Рут для выгрузки файлов")
async def download_file(file_path: str) -> FileResponse:
    return FileResponse(path=file_path, filename=file_path,
                        media_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
