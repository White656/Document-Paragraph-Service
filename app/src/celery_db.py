from celery import Celery

from core.config import app_config

celery: Celery = Celery(__name__, broker=app_config.celery_config.broker_url,
                        backend=app_config.celery_config.backend_url)


# Функция понадобится при внедрении зависимостей
async def get_celery() -> Celery:
    return celery
