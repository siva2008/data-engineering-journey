import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="dataengineering",
    user="postgres",
    password="YOUR_POSTGRES_PASSWORD",
    port="5432"
)

print("Database connection successful!")

cursor = connection.cursor()

cursor.execute("select * from employee;")

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()

connection.close()
print("Database connection closed.")