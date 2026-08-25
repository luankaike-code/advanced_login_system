import secrets

from .table_manager import TableManager

class TableConnectionsManager(TableManager):
	def __init__(self, host: str, port: int, database: str, user: str, password: str):
		super().__init__("TABLE_CONNECTIONS", host, port, database, user, password)

	def create_new_connection(self, user_id: int) -> str:
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

	def get_user_id(self, token: str) -> int | None:
			data = self._execute_select(
				table=self.table_name,
				fields=[
					"user_id",
				],
				where_query="token = %s",
				values=[
					token
				]
			)

			if len(data) < 1:
				return None
			return data[0]["user_id"]

	def destroy_connection_using_token(self, token: int) -> int:
		count_row_affects = self._execute_delete(
			table=self.table_name,
			where_query="token = %s",
			values=[
				token,
			]
		)

		self._execute_commit()

		return count_row_affects