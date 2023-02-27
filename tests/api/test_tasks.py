import unittest
import os

from app import create_app
from app import db
from settings import config_dict


class TestApiTasks(unittest.TestCase):
    TASK = {"text": "Some useful task to do", "is_done": False}
    API_KEY = os.environ.get("API_KEY")

    def setUp(self):
        self.app = create_app(config=config_dict["test"])
        self.appctx = self.app.app_context()
        self.appctx.push()
        self.client = self.app.test_client()
        self.client.environ_base["HTTP_X_API_KEY"] = self.API_KEY
        db.create_all()

    def tearDown(self):
        db.drop_all()
        self.appctx.pop()
        self.app = None
        self.client = None

    def test_get_tasks(self):
        response = self.client.get("/api/v1/tasks/")
        assert response.json == []
        assert response.status_code == 200

    def test_post_task(self):
        response = self.client.post("/api/v1/tasks/", json=self.TASK)
        assert response.json["id"] == 1
        assert response.json["is_done"] == self.TASK["is_done"]
        assert response.json["text"] == self.TASK["text"]
        assert response.status_code == 201

    def test_get_created_tasks(self):
        response = self.client.post("/api/v1/tasks/", json=self.TASK)
        assert response.status_code == 201

        response = self.client.get("/api/v1/tasks/")
        assert response.json[0]["id"] == 1
        assert len(response.json) == 1
        assert response.json[0]["text"] == self.TASK["text"]
        assert response.json[0]["is_done"] == False
        assert response.status_code == 200

    def test_update_task(self):
        response = self.client.post("/api/v1/tasks/", json=self.TASK)
        assert response.status_code == 201

        task = {"text": "Updated text of this task", "is_done": True}
        response = self.client.put("/api/v1/tasks/1", json=task)
        assert response.json["id"] == 1
        assert len(response.json) == 3
        assert response.json["text"] == task["text"]
        assert response.json["is_done"] == task["is_done"]
        assert response.status_code == 200

    def test_delete_task(self):
        response = self.client.post("/api/v1/tasks/", json=self.TASK)
        assert response.status_code == 201

        response = self.client.get("/api/v1/tasks/")
        assert response.json[0]["id"] == 1
        assert len(response.json) == 1
        assert response.json[0]["text"] == self.TASK["text"]
        assert response.json[0]["is_done"] == False
        assert response.status_code == 200

        response = self.client.delete("/api/v1/tasks/1")
        assert response.json == "OK"
        assert response.status_code == 200

        response = self.client.get("/api/v1/tasks/1")
        assert response.status_code == 404
