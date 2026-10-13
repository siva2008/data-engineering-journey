
import config

required_settings = {
    "DB_HOST": config.DB_HOST,
    "DB_NAME": config.DB_NAME,
    "DB_USER": config.DB_USER,
    "DB_PASSWORD": config.DB_PASSWORD,
}

missing_settings = [
    name
    for name, value in required_settings.items()
    if not value
]

if missing_settings:
    print("Missing settings:", ", ".join(missing_settings))
else:
    print("All required database settings are configured.")
