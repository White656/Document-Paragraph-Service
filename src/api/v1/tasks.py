from celery.result import AsyncResult
from fastapi import APIRouter, Depends

from api.v1.schemas import CeleryTaskInfo
from services.redis_state import RedisStateService, get_redis_service

router = APIRouter()


@router.get("/{task_id}", summary="Получение информации по запущенной задаче")
async def get_status(task_id: str, redis_service: RedisStateService = Depends(get_redis_service)) -> CeleryTaskInfo:
    result = redis_service.get_key(task_id)

    if not result:
        result = AsyncResult(task_id)
        redis_service.set_state(task_id, CeleryTaskInfo(status=result.status, result=result.result, id=task_id))

    return CeleryTaskInfo(status=result.status, result=result.result, id=task_id)
