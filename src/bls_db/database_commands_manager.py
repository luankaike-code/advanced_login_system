from mysql.connector import Error
from .database_connection_manager import DatabaseConnectionManager

class DatabaseCommandsManager(DatabaseConnectionManager):
	def __init__(self, host: str, port: int, database: str, user: str, password: str):
		super().__init__(host, port, database, user, password)

	def _execute_insert(self, table: str, fields: list[str], values: list[any]):
		table_fields_str = ", ".join(fields)
		insert_query_within_values = f"INSERT INTO {table} ({table_fields_str})"

		template_values = ", ".join(["%s"] * len(fields))
		insert_query_with_template_values = f"{insert_query_within_values} VALUES ({template_values})"

		self._cursor.execute(insert_query_with_template_values, values)

	def _execute_commit(self):	
			try:
				self._connection.commit()
			except Error as commit_err:
				print(f"Error while executing commit: {commit_err}")

				try:
					self._connection.rollback()
					print(f"Completed rollback")
				except Error as rollback_err:
								print(f"Error while executing rollback: {rollback_err}")