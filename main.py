import csv
import json

students = []

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        students.append(row)

with open("students.json", "w") as file:
    json.dump(students, file, indent = 4)

print("CSV converted to JSON sucessfully!")