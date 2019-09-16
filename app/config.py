import os

import redis


class Config:
    OPENAPI_VERSION = os.environ.get('OPENAPI_VERSION', '3.0.2')
    SECRET_KEY = os.environ.get('SECRET_KEY', 'test_secret_key')
    CACHE_REDIS_URL = os.environ.get('CACHE_REDIS_URL')

    SESSION_TYPE = os.environ.get('SESSION_TYPE', 'redis')
    SESSION_REDIS = redis.from_url(os.environ.get('SESSION_REDIS_URL'))

    """
    Celery Config
    - CELERY_BROKER_URL uses `pyamqp`.
    - CELERY_IMPORTS registers tasks.
    - BROKER_HEARTBEAT of Celery App must be set to 0
        so that Rabbitmq will not disconnect the connection.
        (This issue is still opened in:
            - https://github.com/celery/celery/issues/5037
            - https://github.com/celery/celery/issues/5157
            - https://github.com/celery/celery/issues/4921)
    """
    CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')
    CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND')
    CELERY_IMPORTS = ('app.tasks')
    CELERY_BROKER_HEARTBEAT = 0
