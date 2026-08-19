import os, secrets
from dotenv import load_dotenv

from .database_managers import DatabaseManager

load_dotenv()

class TableConnectionsManager(DatabaseManager):
	def __init__(self, host: str, port: int, database: str, user: str, password: str):
		super().__init__(host, port, database, user, password)
		self.connections_table = os.getenv("TABLE_CONNECTIONS")

	def create_new_connection(self, user_id: int):
		token = secrets.token_hex(127)
		self._execute_insert(
			table=self.connections_table,
			fields=[
				"user_id",
				"token"
			],
			values=[
				user_id,
				token
			]
		)

		self._execute_commit()
		
		return token