from flask_socketio import (SocketIO, emit, join_room, leave_room, rooms)

socket_io = SocketIO(
    manage_session=False, cors_allowed_origins="*", logger=True,
    engineio_logger=True)


@socket_io.on_error_default
def default_error_handler(e):
    from flask import current_app
    current_app.logger.error(e)


@socket_io.on("connect", namespace='/test')
def socket_connect():
    from flask import (current_app, session)
    current_app.logger.info("Client (sid: {}) connected.".format(session.sid))
    emit("message", {"status": "Connected"}, broadcast=True)


@socket_io.on("disconnect", namespace='/test')
def socket_disconnect():
    from flask import (current_app, session)
    current_app.logger.info("Client (sid: {}) disconnected.".format(session.sid))
    emit("message", {"status": "Disconnected"}, broadcast=True)


@socket_io.on('join', namespace='/test')
def join(json):
    from flask import (current_app, session)
    room = json['room']
    join_room(room)
    current_app.logger.info(
        "Client (sid: {}) joined the room ({}).".format(session.sid, room))
    data = {"status": "Joined room ({})".format(room), "rooms": rooms()}
    emit("message", data)


@socket_io.on('leave', namespace='/test')
def leave(json):
    from flask import (current_app, session)
    current_app.logger.info("Client (sid: {}) connected".format(session.sid))
    room = json['room']
    leave_room(room)
    current_app.logger.info(
        "Client (sid: {}) left the room ({}).".format(session.sid, room))
    data = {"status": "Left room ({})".format(room), "rooms": rooms()}
    emit("message", data)
