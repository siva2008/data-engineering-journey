import csv
import psycopg2

def extract_data():
    employees = []

    with open("Day05/employee_source.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            employees.append(row)

    return employees


def transform_data(employees):
    transformed_employees = []
    rejected_employees = []

    for employee in employees:
        try:
            salary = float(employee["salary"])
        except(TypeError,ValueError):
            print(
                "Invalid salary for employee:",
                employee["id"],
                employee["name"]
            )
            rejected_employees.append(employee)
            continue

        transformed_employee = {
            "id": int(employee["id"]),
            "name": employee["name"],
            "department": employee["department"],
            "salary": float(employee["salary"])
        }

        transformed_employees.append(transformed_employee)

    return transformed_employees, rejected_employees

def load_data(transformed_employees):

    connection = psycopg2.connect(
        host="localhost",
        database="dataengineering",
        user="postgres",
        password="YOUR_POSTGRES_PASSWORD",
        port="5432"
    )

    cursor = connection.cursor()
    sql = """
        insert into employee (id, name, department, salary)
        values (%s,%s,%s,%s) on conflict (id) DO NOTHING"""

    for employee in transformed_employees:
        data = (
            employee["id"],
            employee["name"],
            employee["department"],
            employee["salary"]
        )
        cursor.execute(sql, data)

    connection.commit()
    cursor.close()
    connection.close()
    print("Data loaded successfully into PostgreSQL!")

employees = extract_data()

transformed_employees, rejected_employees = transform_data(employees)
print("Valid records:", len(transformed_employees))
print("Rejected records:", len(rejected_employees))

load_data(transformed_employees)

