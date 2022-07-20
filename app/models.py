from app import db


class Tasks(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(), nullable=False)

    def __init__(self, text):
        self.text = text
