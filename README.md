# flask-celery-rabbitmq-example

A simple **Flask** application using **RabbitMQ**, **Redis**, **Celery**, **Flask-SocketIO** and **Flask-Session**.

## Getting Started

### Prerequisites

*Docker Engine* needs to be installed on your machine ([Docker Documentation](https://docs.docker.com/)).

### Environment variables

| Variable                 | Description                                                               |
| ------------------------ | ------------------------------------------------------------------------- |
| `RABBITMQ_ERLANG_COOKIE` | Set a consistent cookie (useful for clustering) for **RabbitMQ**          |
| `RABBITMQ_DEFAULT_USER`  | Set a default username for **RabbitMQ**                                   |
| `RABBITMQ_DEFAULT_PASS`  | Set a default username's password for **RabbitMQ**                        |
| `RABBITMQ_NODE_PORT`     | Set a port number of RabbitMQ node (e.g., *5672*)                         |
| `CELERY_BROKER_URL`      | Set a location of the broker instance (i.e., **RabbitMQ URL**)            |
| `CELERY_RESULT_BACKEND`  | Set a location of result store (i.e., **Redis URL**)                      |
| `SESSION_TYPE`           | Set a type of server-side session store (i.e., **"redis"**)               |
| `SESSION_REDIS_URL`      | Set a location of server-side session store (i.e., **Redis URL**)         |

### Installing

To build application docker image,

```bash
./run_build.sh
```

**flask-celery-rabbitmq-example-app** image will be generated.

```bash
$ docker images
REPOSITORY                         TAG     IMAGE ID      CREATED         SIZE
flask-celery-rabbitmq-example-app  latest  508adf7d3b65  26 minutes ago  331MB
```

### Get it running

```bash
$ docker-compose up -d
Creating network "flask-celery-rabbitmq-example_default" with the default driver
Creating flask-celery-rabbitmq-example_rabbitmq_1 ... done
Creating flask-celery-rabbitmq-example_redis_1    ... done
Creating flask-celery-rabbitmq-example_app-celery-worker_1 ... done
Creating flask-celery-rabbitmq-example_app_1               ... done
```

## References

* [RabbitMQ official docker image](https://hub.docker.com/_/rabbitmq)
* [Redis official docker image](https://hub.docker.com/_/redis)
* [Github Celery](https://github.com/celery/celery)
* [Github Flask-SocketIO](https://github.com/miguelgrinberg/Flask-SocketIO)
* [Github Flask-Session](https://github.com/fengsp/flask-session)
