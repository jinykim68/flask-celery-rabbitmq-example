#!/bin/bash

set -a
source .env
set +a

source ./.venv/bin/activate
celery worker -A app.server:celery --concurrency=1000 -P gevent --loglevel=info