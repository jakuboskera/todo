from flask import request
from flask_restx import fields
from flask_restx import Namespace
from flask_restx import Resource

from app import db
from app.api.authentication import token_required
from app.models import Tasks

api = Namespace("tasks", description="Tasks related operations")

task = api.model(
    "Task",
    {
        "id": fields.Integer(readonly=True, description="The task identifier"),
        "text": fields.String(required=True, description="The task details"),
        "is_done": fields.Boolean(
            default=False, description="Deciding if the task is done"
        ),
    },
)


@api.route("/")
class TaskList(Resource):
    """Shows a list of all tasks, and lets you POST to add new tasks"""

    @api.doc("list_tasks")
    @api.marshal_list_with(task)
    @api.doc(security=None)
    def get(self):
        """List all tasks"""
        return Tasks.query.order_by(Tasks.id).all()

    @api.doc("create_task")
    @api.expect(task)
    @api.marshal_with(task, code=201)
    @token_required
    def post(self):
        """Create a new task"""
        task = Tasks(api.payload["text"], api.payload["is_done"])
        db.session.add(task)
        db.session.commit()
        return task, 201, {"Location": "".join([request.url, str(task.id)])}


@api.route("/<int:id>")
@api.response(404, "Task not found")
@api.param("id", "The task identifier")
class Task(Resource):
    """Show a single task item and lets you delete them"""

    @api.doc("get_task")
    @api.marshal_with(task)
    @api.doc(security=None)
    def get(self, id):
        """Fetch a given resource"""
        task = Tasks.query.filter_by(id=id).first()

        if task is not None:
            return task
        api.abort(404)

    @api.doc("delete_task")
    @api.response(200, "Task deleted")
    @token_required
    def delete(self, id):
        """Delete a task given its identifier"""
        task = Tasks.query.filter_by(id=id).first()

        if task is not None:
            Tasks.query.filter_by(id=id).delete()
            db.session.commit()
            return "OK"
        api.abort(404)

    @api.expect(task)
    @api.marshal_with(task)
    @token_required
    def put(self, id):
        """Update a task given its identifier"""
        task = Tasks.query.filter_by(id=id).first()

        if task is not None:
            data = {}
            if w := api.payload.get("text", None) is not None:
                data["text"] = w
            if w := api.payload.get("is_done", None) is not None:
                data["is_done"] = w
            Tasks.query.filter_by(id=id).update(data)
            db.session.commit()
            return Task().get(id)
        api.abort(404)
