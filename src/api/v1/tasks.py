from celery.result import AsyncResult
from fastapi import APIRouter

from api.v1.schemas import CeleryTaskInfo

router = APIRouter()


@router.get("/{task_id}")
async def get_status(task_id) -> CeleryTaskInfo:
    task_result = AsyncResult(task_id)
    return CeleryTaskInfo(status=task_result.status, result=task_result.result, id=task_id)
