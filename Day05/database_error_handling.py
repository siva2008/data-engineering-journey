import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="dataengineering",
    user="postgres",
    password="YOUR_POSTGRES_PASSWORD",
    port="5432"
)

print("Database connection successful")
cursor = connection.cursor()

try:
    sql = """
    insert into employee (id, name, department, salary)
    values (%s, %s, %s, %s)
    """
    employee_data = (1008, "Mike", "IT", 70000)

    cursor.execute(sql,employee_data)

    connection.commit()
    print("Employee inserted successfully!")

except psycopg2.Error as error:
    connection.rollback()
    print("Database error:", error)

finally:
    cursor.close()
    connection.close()
    print("Database connection closed")