import os
from dotenv import load_dotenv

load_dotenv("instance/secrets.env")

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
SECRET_KEY = os.getenv("SECRET_KEY")

DB = "database.db"
