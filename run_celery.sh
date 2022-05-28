#!/bin/bash

set -a
source .env
set +a

source ./.venv/bin/activate
celery -A app.server:celery worker --concurrency=1000 -P gevent --loglevel=info