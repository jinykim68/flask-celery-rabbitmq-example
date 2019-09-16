import logging

from celery import Celery
from dynaconf.contrib import FlaskDynaconf
from flask import Flask
from flask_rest_api import Api

from app.ext import (cache, session, socket_io)


def create_celery(app):
    """
    Initializes a celery application using Flask App
        (retrieved from `http://flask.pocoo.org/docs/1.0/patterns/celery/`).
    """
    celery = Celery(app.import_name,
                    broker=app.config.CELERY_BROKER_URL,
                    backend=app.config.CELERY_RESULT_BACKEND)
    # celery.conf.update(app.config)
    celery.conf.CELERY_IMPORTS = app.config.CELERY_IMPORTS
    celery.conf.BROKER_HEARTBEAT = app.config.CELERY_BROKER_HEARTBEAT

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


def register_blueprints(app, *blps):
    api = Api(app=app)
    for blp in blps:
        api.register_blueprint(blp)

    return api


def create_app(config_module):
    app = Flask(__name__)
    app.config.from_object(config_module)

    # make app.config support dot notation.
    FlaskDynaconf(app=app)

    # init Cache
    cache.init_app(app, {
        "CACHE_TYPE": "redis",
        "CACHE_REDIS_URL": app.config.CACHE_REDIS_URL
    })

    # init SocketIO
    if not app.config.CELERY_BROKER_URL:
        logging.warn(
            """app.config.CELERY_BROKER_URL is not set. """
            """SocketIO may not work with Celery workers now.""")

    socket_io.init_app(app=app, message_queue=app.config.CELERY_BROKER_URL)

    # init Session
    session.init_app(app=app)

    # register blueprints
    from app.api import task_blp
    register_blueprints(app, task_blp)

    return app
