from app.models import Tasks


class TestModels:
    def test_new_task(self):
        """
        GIVEN a Task model
        WHEN a new Task is created
        THEN check the text, is_done
        """
        task = Tasks("Some useful task to do", False)
        assert task.text == "Some useful task to do"
        assert task.is_done == False

    def test_task_is_done(self):
        """
        GIVEN a Task model
        WHEN a new Task is done
        THEN check the text, is_done
        """
        task = Tasks("Some useful task to do", True)
        assert task.text == "Some useful task to do"
        assert task.is_done == True
