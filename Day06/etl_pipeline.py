import csv
import psycopg2

def extract_data():
    employees = []

    with open("employee_source.csv","r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            employees.append(row)
    return employees

def validate_employees(employee):
    if not employee["id"].strip():
        return False, "Missing id"

    if not employee["name"].strip():
        return False, "Missing Name"

    if not employee["department"].strip():
        return False, "Missing Department"
    if not employee["salary"].strip():
        return False, "Missing Salary"
    try:
        salary = float(employee["salary"])
    except(TypeError,ValueError):
        return False, "Invalid Salary"

    if salary < 0:
        return False, "Negative Salary"

    return True, "Valid"

def transform_data(employees):
    transformed_data = []

    for row in employees:
        transform_data = {
            "id": int(row["id"]),
            "name": row["name"].strip(),
            "department": row["department"].strip(),
            "salary": float(row["salary"])
        }
        transformed_data.append(transform_data)

    return transformed_data

def load_data(employees):
    connection = psycopg2.connect(
        host="localhost",
        database = "dataengineering",
        user = "postgres",
        password = "Yourpwd",
        port = "5432"
    )

    cursor = connection.cursor()
    
    for employee in employees:
        cursor.execute(
            """
            INSERT INTO employee (id, name, department, salary)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (id) DO NOTHING;
            """,
            (
                employee["id"],
                employee["name"],
                employee["department"],
                employee["salary"]
            )
        )

    connection.commit()
    cursor.close()
    connection.close()

    print("\nData loaded successfully")

employees = extract_data()

print("Validation results")

valid_employees = []
rejected_employees = []

for employee in employees:
    is_valid, reason = validate_employees(employee)

    if is_valid:
        valid_employees.append(employee)
    else:
        employee["rejected_reason"] = reason
        rejected_employees.append(employee)

def save_rejected_records(rejected_employees):

    with open("rejected_data.csv","w", newline="") as file:
        fieldnames = ["id", "name", "department", "salary", "rejected_reason"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for row in rejected_employees:
            writer.writerow(row)

print("Valid employees:", len(valid_employees))
print("Rejected employees:", len(rejected_employees))

print("\nValid employees")
for row in valid_employees:
    print(row)

print("\nRejected employees")
for row in rejected_employees:
    print(row)

trans_data = transform_data(valid_employees)
print("\nTransformed employees")
for row in trans_data:
    print(row)

save_rejected_records(rejected_employees)

load_data(trans_data)