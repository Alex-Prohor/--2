import json

def task() -> float:

    with open("input.json", "r") as file:
        data = json.load(file)


    result = sum(item["score"] * item["weight"] for item in data if "score" in item and "weight" in item)


    return round(result, 3)

print(task())