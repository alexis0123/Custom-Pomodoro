from datetime import datetime, date, timedelta
import json
import os

class Data:
    def __init__(self):

        self.path = "journal"
        self.file_path = os.path.join(self.path, "log.json")
        self.date_today = date.today().isoformat()

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

    def add_pomo(self, task_name, start, end):
        if task_name not in self.logs[self.date_today]:
            raise ValueError(f"{task_name} doesnt exist.. you must add_task() first")

        self.logs[self.date_today][task_name]["pomos"].append({"started": start, "ended": end})

    def add_reflection(self, task_name, reflection):
        if task_name not in self.logs[self.date_today]:
            raise ValueError(f"{task_name} doesnt exist.. you must add_task() first")
        
        self.logs[self.date_today][task_name]["reflection"] = reflection

    def get_tasks(self) -> list:
        tasks = []
        for task in self.logs[self.date_today]:
            tasks.append({"task": task, "pomos": len(self.logs[self.date_today][task]["pomos"])})

        return tasks
    
    def get_streak(self) -> dict:
        dates = []
        day_logs = self.logs.get(self.date_today, {})
        for task in day_logs:
            if self.logs[task]:
                dates.append(datetime.strptime(task, "%Y-%m-%d").date())

        if not dates:
            return {"longest_streak": 0, "streak": 0}
        
        longest_streak = 1
        streak = 1

        for cur, nxt in zip(dates, dates[1:]):
            if nxt - cur == timedelta(days=1):
                streak += 1

            else:
                streak = 1

            longest_streak = max(longest_streak, streak)

        if (date.today() - dates[-1]).days > 1:
            streak = 0

        return {"longest_streak": longest_streak, "streak": streak}