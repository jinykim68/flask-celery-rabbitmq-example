FROM python:3.7-alpine

ENV INSTALL_PATH=/home/test_app

WORKDIR ${INSTALL_PATH}

COPY app app
COPY ["requirements.txt", "docker/app/docker-entrypoint.sh", "./"]

RUN apk add --no-cache curl gcc musl-dev linux-headers bash; \
    pip install --upgrade pip; \
    pip install --no-cache-dir cython

RUN pip install -r requirements.txt

RUN chmod +x docker-entrypoint.sh
ENTRYPOINT [ "./docker-entrypoint.sh" ]
