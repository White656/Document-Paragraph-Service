import time
from celery import Celery

from core.config import app_config

celery: Celery = Celery(__name__, broker=app_config.celery_config.broker_url,
                        backend=app_config.celery_config.backend_url)


@celery.task(name="create_task")
def create_task(filedata):
    print(filedata)
    time.sleep(10)
    return filedata
