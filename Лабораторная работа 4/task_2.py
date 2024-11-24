import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:

    with open(INPUT_FILENAME, "r", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        data = [row for row in reader]


    with open(OUTPUT_FILENAME, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    task()


    with open(OUTPUT_FILENAME, "r", encoding="utf-8") as output_file:
        for line in output_file:
            print(line, end="")