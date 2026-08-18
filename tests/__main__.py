import os, als_db
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("HOST")
port = int(os.getenv("PORT"))
database = os.getenv("DATABASE")
user = os.getenv("DATABASE_USER")
password = os.getenv("PASSWORD")

db = als_db.TableUserManager(
	host=host,
	port=port,
	database=database,
	user=user,
	password=password
)

db.insert_new_user(
	name="Luka",
	email="@outllokkk",
	password="senha",
	tel="12345677"
)