# TODO решите задачу
import json


FILENAME = "input.json"
def task() -> float:
    with open(FILENAME) as f:
        json_data = json.load(f)
    total_values = sum([item["score"]*item["weight"] for item in json_data])
    return round(total_values,3)

print(task())
