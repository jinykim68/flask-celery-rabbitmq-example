from flask import (current_app, request)
from flask.views import MethodView
from flask_rest_api import Blueprint

blp = Blueprint(
    "tasks", __name__, url_prefix="/tasks", description="Tasks blueprint")


@blp.route("/", strict_slashes=False)
class TestAPI(MethodView):
    @blp.response(code=200)
    def get(self):
        from app.tasks import long_task
        current_app.logger.debug("{} {}".format(
            request.method, request.url_rule))

        room = request.args.get('room')
        task = long_task.apply_async(retry=True, kwargs={"room": room})
        current_app.logger.info(
            "Task (id: {}, state: {}, queue: {}) is registered.".format(
                task.task_id, task.state, task.queue))
        return {
            "taskId": task.id
        }


@blp.route("/<task_id>", strict_slashes=False)
class TestTaskAPI(MethodView):
    @blp.response(code=200)
    def get(self, task_id):
        from app.tasks import long_task
        current_app.logger.debug("{} {}".format(
            request.method, request.url_rule))
        task = long_task.AsyncResult(task_id)
        current_app.logger.info(
            "Task (id: {}, state: {}, queue: {}) is retrieved from backend {}."
            .format(task.task_id, task.state, task.queue, task.backend))
        return {
            "state": task.state
        }
