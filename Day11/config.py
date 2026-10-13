import os
from dotenv import load_dotenv

load_dotenv()

APP_ENV = os.getenv("APP_ENV", "development").lower()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

allowed_environments = {"development", "testing", "production"}

if APP_ENV not in allowed_environments:
    raise ValueError(f"Invalid APP_ENV: {APP_ENV}")