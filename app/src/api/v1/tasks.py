from celery.result import AsyncResult
from fastapi import APIRouter

from api.v1.schemas import CeleryTaskInfo

router = APIRouter()


@router.get("/{task_id}")
async def get_status(task_id) -> CeleryTaskInfo:
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result
    }
    print(type(task_result.status))
    return CeleryTaskInfo(status=task_result.status, result=task_result.result, id=task_id)
