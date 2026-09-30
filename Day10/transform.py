from logger import get_logger

logger = get_logger()

def transform_data(employees):
    valid_employees = []
    rejected_employees = []

    for employee in employees:

        try:
            employee_id = int(employee["id"])
            name = employee["name"].strip()
            department = employee["department"].strip()
            salary = float(employee["salary"])

            if not employee["name"]:
                raise ValueError("Name is missing")

            if not employee["department"]:
                raise ValueError("Department is missing")

            if not employee["salary"]:
                raise ValueError("Salary is missing")

            if salary < 0:
                raise ValueError("Salary cannot be negative")

            transformed_data = {
                "id" : employee_id,
                "name": name,
                "department": department,
                "salary": salary
                }

            valid_employees.append(transformed_data)

        except(TypeError, ValueError) as error:
            rejected_employees.append({
                "employee": employee,
                "reason": str(error) } )

            logger.warning(f"Employee {employee.get('id')} Reason {error}")
    return valid_employees, rejected_employees