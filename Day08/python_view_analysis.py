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
                select department_name as department, count(*) as Employees, round(avg(salary),2) as Average_salary
                from emp_dept_view group by department_name order by department_name;
"""
)

rows = cursor.fetchall()

print("\nEmployee Department Report")
print("--------------------------")

for row in rows:
    department, employees, average_salary = row

    print(
        f"Department: {department} | "
        f"Employees: {employees} | "
        f"Average_Salary: {average_salary} "
    )

cursor.execute(""" select count(*) as total_employees, count(salary) as employees_with_salary, 
                   round(avg(salary),2) as average_salary1 from emp_dept_view; """)
row1 = cursor.fetchone()

total_employees, employees_with_salary, average_salary1 = row1

print("\nOverall Employee Statistics")
print("---------------------------")

print(f"Total Employees: {total_employees}")
print(f"Employees With Salary: {employees_with_salary}")
print(f"Average Salary: {average_salary1}")

cursor.close()
connection.close()