import aioredis
import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from core.config import app_config
from db import redis

app = FastAPI(
    title=app_config.name,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
)


@app.on_event('startup')
async def startup():
    redis.redis = aioredis.from_url(f'redis://{app_config.redis_config.host}:{app_config.redis_config.port}',
                                    encoding="utf8",
                                    decode_responses=True)


@app.on_event('shutdown')
async def shutdown():
    await redis.redis.close()


# Теги указываем для удобства навигации по документации
# app.include_router(films.router, prefix='/api/v1/films', tags=['films'])
# app.include_router(genres.router, prefix='/api/v1/genres', tags=['genres'])
# app.include_router(persons.router, prefix='/api/v1/persons', tags=['persons'])

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8000,
        reload=True,
        debug=True,
    )
