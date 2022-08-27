import time

from redis import Redis, ConnectionError

from functional.settings import test_settings

r = Redis(host=test_settings.redis_host, port=test_settings.redis_port)

is_connected = False

while not is_connected:
    try:
        is_connected = r.ping()
        print('Redis connected.')
    except ConnectionError:
        print('Redis not connected, retry in 5 seconds...')
        time.sleep(5)
