import json
import os

path = "journal"
file_path = os.path.join(path, "log.json")

try:
    os.makedirs(path)
except FileExistsError:
    pass

if not os.path.exists(file_path):
    with open(file_path, "w") as f:
        pass