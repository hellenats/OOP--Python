from typing import List
from project.task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, new_task: Task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str):
        try:
            t = next((t for t in self.tasks if t.name == task_name))
            t.completed = True
            return f"Completed task {t.name}"

        except StopIteration:
            return f"Could not find task with the name {task_name}"

    def clean_section(self):
        completed_tasks = []
        try:
            completed_tasks = [next((t for t in self.tasks if t.completed))]
            for task in completed_tasks:
                self.tasks.remove(task)
        except StopIteration:
            pass
        return f"Cleared {len(completed_tasks)} tasks."

    def view_section(self):
        result = [f"Section {self.name}:"]
        for t in self.tasks:
            result.append(t.details())
        return '\n'.join(result)