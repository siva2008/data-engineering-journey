import csv

def load_data(transform):
    with open("processed_employees.csv", "w", newline ="") as file:
        fieldname = ["id", "name", "department", "salary"]
        writer = csv.DictWriter(file, fieldnames = fieldname)

        writer.writeheader()
        writer.writerows(transform)

print("Processed data written to processed_employees.csv")