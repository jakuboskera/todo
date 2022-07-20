from flask import request
from flask_restx import fields
from flask_restx import Namespace
from flask_restx import Resource

from app import db
from app.models import Tasks
from app.api.authentication import token_required

api = Namespace("tasks", description="Tasks related operations")

task = api.model(
    "Task",
    {
        "id": fields.Integer(readonly=True, description="The task identifier"),
        "text": fields.String(required=True, description="The task details"),
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
        task = Tasks(api.payload["text"])
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
            Tasks.query.filter_by(id=id).update(dict(text=api.payload["text"]))
            db.session.commit()
            return Task().get(id)
        api.abort(404)
