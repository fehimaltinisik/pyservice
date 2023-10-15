import importlib.resources
import json
from typing import Dict


BASE_PATH: str = 'tests.resources'


def load_json_resource(resource_path: str, file_name: str) -> Dict:
    full_path: str = f"{BASE_PATH}.{resource_path}"
    file_path: str = importlib.resources.path(full_path, file_name).__str__()
    with open(file_path, "r") as file:
        return json.load(file)


def save_json_payload(submission: Dict, resource_path: str, file_name: str) -> None:
    full_path: str = f"{BASE_PATH}.{resource_path}"
    file_path: str = importlib.resources.path(full_path, file_name).__str__()
    with open(file_path, "w") as file:
        json.dump(submission, file)
