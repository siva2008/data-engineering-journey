import psycopg2
import config

connection = None

try:
    connection = psycopg2.connect(
        host=config.DB_HOST,
        database=config.DB_NAME,
        user=config.DB_USER,
        password=config.DB_PASSWORD
    )

    print("PostgreSQL connection successful!")

    cursor = connection.cursor()
    cursor.execute("SELECT current_database(), current_user;")
    result = cursor.fetchone()

    print("Database:", result[0])
    print("User:", result[1])

    cursor.close()

except psycopg2.Error as error:
    print("Database connection failed.")
    print("Error:", error)

finally:
    if connection is not None:
        connection.close()
        print("Connection closed.")


