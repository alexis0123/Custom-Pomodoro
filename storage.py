from datetime import date
import json
import os

class Data:
    def __init__(self):

        self.path = "journal"
        self.file_path = os.path.join(self.path, "log.json")
        self.date_today = date.today().strftime("%d/%m/%Y")

        os.makedirs(self.path, exist_ok=True)

        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                json.dump({}, f)

        self.logs = self.load()

    def load(self):
        with open(self.file_path, "r") as f:
            return json.load(f)
        
    def save(self):
        with open(self.file_path, "w") as f:
            json.dump(self.logs, f , indent=2)

    def add_task(self, task):
        if self.date_today not in self.logs:
            self.logs[self.date_today] = {}

        self.logs[self.date_today][task] = {}