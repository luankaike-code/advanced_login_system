import secrets

from .table_manager import TableManager

class TableConnectionsManager(TableManager):
	def __init__(self, host: str, port: int, database: str, user: str, password: str):
		super().__init__("TABLE_CONNECTIONS", host, port, database, user, password)

	def create_new_connection(self, user_id: int):
		token = secrets.token_hex(127)
		self._execute_insert(
			table=self.table_name,
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