import logging

from app import (create_app, create_celery)

app = create_app('app.config.Config')

if __name__ != '__main__':
    # Use gunicorn to run the app. We need to have a logger to display logs.
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    # app.logger.handlers.extend(gunicorn_logger.handlers)
    app.logger.setLevel(gunicorn_logger.level)

    # https://realpython.com/python-web-applications-with-flask-part-iii/#logging
    # handler = logging.StreamHandler()
    # # log_format = "%(asctime)s\t%(levelname)s\t%(user_id)s\t%(ip)s\t%(method)s\t%(url)s\t%(message)s"
    # log_format = "%(asctime)s\t%(levelname)s\t%(message)s"
    # formatter = logging.Formatter(log_format)
    # handler.setFormatter(formatter)
    # app.logger.addHandler(handler)

    # https://medium.com/@sanchitsokhey/centralised-logging-for-django-gunicorn-and-celery-using-elk-stack-76b13c54414c

celery = create_celery(app=app)

if __name__ == '__main__':
    # Use the embedded server to run (e.g., FLASK_APP=server.py flask run).
    from app.ext import socket_io
    socket_io.run(app=app, debug=True)
