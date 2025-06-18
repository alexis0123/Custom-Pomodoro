from datetime import date
import json
import os

class Data:
    def __init__(self):

        self.path = "journal"
        self.file_path = os.path.join(self.path, "log.json")
        self.date_today = date.today()

        os.makedirs(self.path, exist_ok=True)

        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                json.dump({}, f)

        self.logs = self.load()

    def load(self) -> dict:
        with open(self.file_path, "r") as f:
            return json.load(f)
        
    def save(self):
        with open(self.file_path, "w") as f:
            json.dump(self.logs, f , indent=2)

    def add_task(self, task) -> str:
        if self.date_today not in self.logs:
            self.logs[self.date_today] = {}

        task_name = task

        if task_name not in self.logs[self.date_today]:
            self.logs[self.date_today][task_name] = {"pomos": []}

        else:
            n = 1
            task_name = f"{task}({n})"
            while task_name in self.logs[self.date_today]:
                n += 1
            self.logs[self.date_today][task_name] = {"pomos": []}

        return task_name

    def add_pomo(self, task_name, start, end, reflection):
        if task_name not in self.logs[self.date_today]:
            raise ValueError(f"{task_name} doesnt exist.. you must add_task() first")

        self.logs[self.date_today][task_name]["pomos"].append({"started": start, "ended": end, "reflection": reflection})

    def add_reflection(self, task_name, reflection):
        if task_name not in self.logs[self.date_today]:
            raise ValueError(f"{task_name} doesnt exist.. you must add_task() first")
        
        self.logs[self.date_today][task_name]["reflection"] = reflection

    def get_tasks(self) -> list:
        tasks = []
        for task in self.logs[self.date_today]:
            tasks.append({"task": task, "pomos": len(self.logs[self.date_today][task]["pomos"])})

        return tasks
