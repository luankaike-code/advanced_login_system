from mysql.connector import Error
from mysql.connector.types import RowItemType, RowType
from typing import List, Dict, Any
from .database_connection_manager import DatabaseConnectionManager

class DatabaseCommandsManager(DatabaseConnectionManager):
	def __init__(self, host: str, port: int, database: str, user: str, password: str) -> None:
		super().__init__(host, port, database, user, password)

	def _execute_insert(self, table: str, fields: list[str], values: list[any]) -> None:
		table_fields_str = ", ".join(fields)
		insert_query_without_values = f"INSERT INTO {table} ({table_fields_str})"

		template_values = ", ".join(["%s"] * len(fields))
		insert_query_with_template_values = f"{insert_query_without_values} VALUES ({template_values})"

		self._cursor.execute(insert_query_with_template_values, values)

	def _execute_select(self, table: str, fields: list[str], where_query="", values: list[any]=[]) -> List[RowType | Dict[str, RowItemType]] | Any:
		table_fields_str = ", ".join(fields)
		select_query = f"SELECT {table_fields_str} FROM {table}"

		where_query_striped = where_query.strip()
		where_query_correct = where_query_striped if where_query_striped.startswith("WHERE") or where_query_striped == "" else f"WHERE {where_query}"

		select_query_complete = f"{select_query} {where_query_correct}"

		self._cursor.execute(select_query_complete, values)
		return self._cursor.fetchall()

	def _execute_commit(self) -> None:	
			try:
				self._connection.commit()
			except Error as commit_err:
				print(f"Error while executing commit: {commit_err}")

				try:
					self._connection.rollback()
					print(f"Completed rollback")
				except Error as rollback_err:
								print(f"Error while executing rollback: {rollback_err}")