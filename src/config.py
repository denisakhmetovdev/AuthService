import os

from dotenv import load_dotenv


load_dotenv()

DB_USER = os.environ.get("POSTGRES_USER")
DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_DB = os.environ.get("POSTGRES_DB")
DB_PORT = os.environ.get("POSTGRES_PORT")
