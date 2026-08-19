import als_db, os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("HOST")
PORT = int(os.getenv("PORT"))
DATABASE = os.getenv("DATABASE")
USER = os.getenv("DATABASE_USER")
PASSWORD = os.getenv("PASSWORD")

class TableManagers():
	_instance: TableManagers = None

	def __init__(self):
		print("oi")
		if getattr(self, "_initialized", False):
			return
		print("tudo")
		self._initialized = True

		self.users = als_db.TableUsersManager(
			host=HOST,
			port=PORT,
			database=DATABASE,
			user=USER,
			password=PASSWORD
		)

		self.connections = als_db.TableConnectionsManager(
			host=HOST,
			port=PORT,
			database=DATABASE,
			user=USER,
			password=PASSWORD
		)

	def __new__(cls):
		if cls._instance == None:
			cls._instance = super().__new__(cls)
		return cls._instance