#!/bin/bash

image_name=flask-celery-rabbitmq-example-app
tag=latest

docker build --no-cache -t ${image_name}:${tag:-latest} -f ./docker/app/Dockerfile .
