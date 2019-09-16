from flask_caching import Cache
from app.ext.session import session  # noqa
from app.ext.socketio import socket_io  # noqa

cache = Cache()
