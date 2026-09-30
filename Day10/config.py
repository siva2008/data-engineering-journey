import os

DB_HOST = "localhost"
DB_NAME = "dataengineering"
DB_USER = "postgres"
DB_PASSWORD = os.getenv("DB_PASSWORD")

SOURCE_FILE = "employee_source.csv"
REJECTED_FILE = "rejected_data.csv"