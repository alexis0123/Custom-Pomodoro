import json
import os
class Data:
    def __init__(self):

        self.path = "journal"
        self.file_path = os.path.join(self.path, "log.json")

        os.makedirs(self.path, exist_ok=True)

        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                json.dump("{}", f)