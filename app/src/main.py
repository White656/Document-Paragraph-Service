import aioredis
import uvicorn
from elasticsearch import AsyncElasticsearch
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from core.config import APP_CONFIG
from db import elastic, redis

app = FastAPI(
    title=APP_CONFIG.name,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
)


@app.on_event('startup')
async def startup():
    # redis.redis = aioredis.from_url(f'redis://{APP_CONFIG.redis_config.host}:{APP_CONFIG.redis_config.port}',
    #                                 encoding="utf8",
    #                                 decode_responses=True)
    #
    # elastic.es = AsyncElasticsearch(
    #     hosts=[f'{APP_CONFIG.elasticsearch_config.host}:{APP_CONFIG.elasticsearch_config.port}'])
    # FastAPICache.init(RedisBackend(redis.redis), prefix="fastapi-cache")
    ...


@app.on_event('shutdown')
async def shutdown():
    await redis.redis.close()
    await elastic.es.close()


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
