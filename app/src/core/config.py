import os
from logging import config as logging_config

from pydantic import BaseSettings, Field

from core.logger import LOGGING


class RedisConfig(BaseSettings):
    host: str = Field("127.0.0.1", env="REDIS_HOST")
    port: int = Field(6379, env="REDIS_PORT")
    minsize: int = Field(10, env="MIN_SIZE")
    maxsize: int = Field(20, env="MAX_SIZE")


class CeleryConfig(BaseSettings):
    broker_url: str = Field("redis://localhost:6379", env="BROKER_URL", description="url адрес брокера")
    result_url: str = Field("redis://localhost:6379", env="CELERY_RESULT_BACKEND",
                            description="url адрес брокера результатов")


class AppConfig(BaseSettings):
    name: str = Field("Document-Paragraph-Service", env="APP_NAME", description="имя приложения")
    cache_time: int = Field(5 * 60, env="CACHE_TIME", description="Время жизни кеша в секундах")
    celery_config: CeleryConfig = CeleryConfig()
    redis_config: RedisConfig = RedisConfig()


logging_config.dictConfig(LOGGING)

app_config = AppConfig()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
