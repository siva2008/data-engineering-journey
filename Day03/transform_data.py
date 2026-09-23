def validate_salary(salary):
    if salary is None:
        return None

    return int(salary * 1.10)

def validate_name(employee):
    if not employee["name"]:
        return False

    return True

def transform_data(employees):
    it_employees = [
    employee
    for employee in employees
    if employee["department"] == "IT"
]

    validate_emp = [
        employee
        for employee in it_employees
        if validate_name(employee)
    ]

    updated_employees = [
        {
            "id": employee["id"],
            "name": employee["name"],
            "department": employee["department"],
            "salary": validate_salary(employee["salary"]),
        }
        
        for employee in validate_emp
    ]
    return updated_employees

