import os
from als_db import TableManagers
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("HOST")
port = int(os.getenv("PORT"))
database = os.getenv("DATABASE")
user = os.getenv("DATABASE_USER")
password = os.getenv("PASSWORD")

table_managers = TableManagers(host, port, database, user, password)