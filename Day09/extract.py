import csv

def extract_data(filename):
    employees = []

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            employees.append(row)

    return employees