import time

from db.celery_db import celery


@celery.task(name="create_task")
def create_task(filedata):
    print(filedata)
    time.sleep(10)
    return filedata
