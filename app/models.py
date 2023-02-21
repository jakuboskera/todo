from app import db


class Tasks(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(), nullable=False)
    is_done = db.Column(db.Boolean, unique=False, default=False)

    def __init__(self, text, is_done):
        self.text = text
        self.is_done = is_done
