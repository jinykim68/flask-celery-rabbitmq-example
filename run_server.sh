#!/bin/bash

set -a
source .env
set +a

source ./.venv/bin/activate
# gunicorn app.server:connexion_app -t 180 -w 4 -b 0.0.0.0:5000 --log-level=debug
# gunicorn -k gevent -w 1 --threads 12 -t 180 -b 0.0.0.0:5000 --log-level=debug app.server:connexion_app
# uwsgi --http 127.0.0.1:5000 --gevent 100 --socket :3031 --module app.server:connexion_app
# gunicorn app.server:app --bind 0.0.0.0:5000 --timeout 180 --worker-class gevent --worker-connections 1000 --log-level=debug
gunicorn app.server:app --bind 0.0.0.0:5000 --timeout 180 --worker-class geventwebsocket.gunicorn.workers.GeventWebSocketWorker --worker-connections 1000 --log-level=debug
