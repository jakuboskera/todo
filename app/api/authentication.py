from functools import wraps

from flask import current_app
from flask import abort
from flask import request


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "X-API-KEY" in request.headers:
            token = request.headers["X-API-KEY"]
        if not token:
            return {
                "message": "Authentication Token is missing!",
                "data": None,
                "error": "Unauthorized",
            }, 401
        if token != current_app.config.get("API_KEY"):
            abort(403)
        return f(*args, **kwargs)

    return decorated
