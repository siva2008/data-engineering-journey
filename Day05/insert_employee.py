import psycopg2

connection = psycopg2.connect(
    host = "localhost",
    database = "dataengineering",
    user = "postgres",
    password = "YOUR_POSTGRES_PASSWORD",
    port = 5432
)

print("Database connection successful!")

cursor = connection.cursor()

sql = """  INSERT INTO employee (id, name, department, salary)
    VALUES (%s, %s, %s, %s);
    """
employee_data = (1008, "Lisa", "Marketing", 76000)
cursor.execute(sql,employee_data)

connection.commit()

print("Employee inserted successfully!")

cursor.close()
connection.close();
print("Database connection closed")