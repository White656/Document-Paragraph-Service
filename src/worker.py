from celery import Celery

from core.config import app_config
from services.ml import predictProbas

celery: Celery = Celery(__name__, broker=app_config.celery_config.broker_url,
                        backend=app_config.celery_config.backend_url)


@celery.task(name="predict_probas")
def create_task(text):
    result = predictProbas(text)
    return result
