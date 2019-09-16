import random
import time

from app.ext.socketio import socket_io
from app.server import celery


@celery.task(bind=True)
def long_task(self, room):
    """
    Defines a background task that runs a long function with progress
    reports (Retrieved from https://blog.miguelgrinberg.com/post/using-celery-with-flask).
    """

    verb = ['Starting up', 'Booting', 'Repairing', 'Loading', 'Checking']
    adjective = ['master', 'radiant', 'silent', 'harmonic', 'fast']
    noun = ['solar array', 'particle reshaper', 'cosmic ray', 'orbiter', 'bit']
    message = ''
    total = random.randint(10, 50)
    for i in range(total):
        if not message or random.random() < 0.25:
            message = '{0} {1} {2}...'.format(random.choice(verb),
                                              random.choice(adjective),
                                              random.choice(noun))
        meta = {"current": i, "total": total, "status": message, "room": room}
        self.update_state(state='PROGRESS', meta=meta)
        socket_io.emit("message", meta, room=room, namespace='/test')
        time.sleep(1)

    result = {
        "current": 100,
        "total": 100,
        "status": "Task completed!",
        "result": 42,
        "room": room
    }
    socket_io.emit("message", result, room=room, namespace='/test')
    return result
