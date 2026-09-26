import psycopg2

connection = psycopg2.connect(
    host = "localhost",
    database = "dataengineering",
    user = "postgres",
    password = "pwd",
    port = "5432"
)

cursor = connection.cursor()
cursor.execute("""
    SELECT
        department,
        COUNT(*) AS employee_count,
        ROUND(AVG(salary), 2) AS avg_salary
    FROM employee
    GROUP BY department
    HAVING avg(salary) > 75000
    ORDER BY department;
""")

rows = cursor.fetchall()

print("\nDepartment Analysis")
print("-------------------")

for result in rows:
    department, employee_count, avg_salary = result

    print(
        f"Department: {department} | "
        f"Employees: {employee_count} | "
        f"Average Salary: {avg_salary}"
    )
cursor.close()
connection.close()