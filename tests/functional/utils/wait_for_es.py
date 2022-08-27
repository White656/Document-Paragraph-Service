import time

from elasticsearch import Elasticsearch

from functional.settings import test_settings

es = Elasticsearch([f'{test_settings.es_host}:{test_settings.es_port}'], verify_certs=True)

while not es.ping():
    print('ES not connected, retry in 5 seconds...')
    time.sleep(5)
else:
    print('ES connected.')
