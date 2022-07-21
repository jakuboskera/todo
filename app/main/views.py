from flask import Blueprint
from flask import render_template

from app.api.tasks import TaskList

blueprint = Blueprint("main", __name__, template_folder="templates")


@blueprint.route("/")
def home():
    return render_template("index.html", tasks=TaskList().get())
