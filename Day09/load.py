import psycopg2
from logger import get_logger


logger = get_logger()


def load_data(employees):

    connection = None
    cursor = None

    try:

        connection = psycopg2.connect(
            host="localhost",
            database="dataengineering",
            user="postgres",
            password="PWD"
        )

        cursor = connection.cursor()

        for employee in employees:

            cursor.execute(
                """
                SELECT department_id
                FROM department
                WHERE department_name = %s
                """,
                (employee["department"],)
            )

            result = cursor.fetchone()

            if result is None:

                logger.warning(
                    f"Department not found: {employee['department']}"
                )

                continue

            department_id = result[0]

            cursor.execute(
                """
                INSERT INTO employee (
                    id,
                    name,
                    salary,
                    department_id
                )
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (id) DO NOTHING
                """,
                (
                    employee["id"],
                    employee["name"],
                    employee["salary"],
                    department_id
                )
            )

        connection.commit()

        logger.info("Database transaction committed successfully")

    except psycopg2.Error as error:

        if connection:
            connection.rollback()

        logger.error(
            f"Database error: {error}"
        )

        raise

    finally:

        if cursor:
            cursor.close()

        if connection:
            connection.close()

        logger.info("Database connection closed")