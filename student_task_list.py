import datetime


class Task:
    """
    Represents a single task object (Encapsulation)
    """

    def __init__(self, task_id: int, title: str, description: str):
        self.task_id = task_id
        self.title = title
        self.description = description

        self._iscompleted = False
        self.created_at = datetime.datetime.now()

    def mark_completed(self):
        """
        Changes the internal state of the object
        """
        self._iscompleted = True

    def __str__(self):
        """
        Returns the string representation of the object
        """
        status = "Done" if self._iscompleted else "Pending"
        return (
            f"[{self.task_id}] {self.title} {status}\nDescription: {self.description}"
        )


class TaskManager:
    """
    Manages the collection of tasks and exposes public behaviors
    """

    def __init__(self):

        # Private-like attribute tracking task
        self._task = {}

    def add_task(self, title: str, description: str):
        """
        Creates a new task and stores it
        """

        task_id = len(self._task) + 1
        new_task = Task(task_id, title, description)
        self._task[task_id] = new_task
        print(f"Added task: {title}")
        return new_task

    def complete_task(self, task_id: int):
        """
        Find a task by ID and mark is complete
        """

        if task_id in self._task:
            self._task[task_id].mark_completed()
            print(f"Task # {task_id} is completed")
            return True
        else:
            print(f"Error! Task # {task_id} not found")
            return False

    def list_tasks(self, include_completed=True):
        """
        It displays tasks depending on their status
        """

        print("\n---Current Task List---")
        if not self._task:
            print("No task available!")
            return

        for task in self._task.values():
            if not include_completed and task._iscompleted:
                continue
            print(task)
            print("----------")


if __name__ == "__main__":
    # Initiate the application controller.
    app = TaskManager()

    # Add items, creates independing instances of task
    app.add_task("Buy Groceries", "Milk, eggs, and freshly ground beans")
    app.add_task("Finish OOP code", "Write python snippet demonstating encapsulation")

    # View pending status
    app.list_tasks()

    # Interact with individual object via the manager
    app.complete_task(1)

    # View updated status
    app.list_tasks()
