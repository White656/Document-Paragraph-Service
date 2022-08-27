import os
from logging import config as logging_config

from pydantic import BaseSettings, Field

from core.logger import LOGGING


class AppConfig(BaseSettings):
    ...


# Применяем настройки логирования
logging_config.dictConfig(LOGGING)

APP_CONFIG = AppConfig()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
