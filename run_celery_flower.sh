#!/bin/bash

celery flower -A app.server:celery --address=127.0.0.1 --port=5555
