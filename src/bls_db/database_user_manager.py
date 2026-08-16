from mysql.connector import Error
from mysql.connector.types import RowItemType, RowType
from typing import Literal, List, Dict, Any
from dotenv import load_dotenv
import os

from .database_commands_manager import DatabaseCommandsManager
from .errors import DuplicateLoginInformationError

load_dotenv()

class DatabaseUserManager(DatabaseCommandsManager):
	def __init__(self, host: str, port: int, database: str, user: str, password: str) -> None:
		super().__init__(host, port, database, user, password)
		self.user_table_name = os.getenv("TABLE_USERS_NAME")

	def insert_new_user(self, name: str, email: str, password: str, tel: str, can_view_user_table: bool=False, can_create_new_user: bool=False) -> None:
		try:
			self.insert_new_user_without_error_handler(name, email, password, tel, can_view_user_table, can_create_new_user)
		except Error as e:
			print(f"Error while insert new user: {e}")

	def check_login_information_without_error_handler(self, identifity: str, identifier_type: Literal["name", "email", "tel"], password: str) -> tuple[bool, List[RowType | Dict[str, RowItemType]] | Any]:
		res = self._execute_select(
			table=self.user_table_name,
			fields="*",
			where_query=f"{identifier_type} = %s AND password = %s",
			values=[
				identifity,
				password
			]
		)

		res_len = len(res)
		
		if res_len > 1:
			raise DuplicateLoginInformationError(self.user_table_name, res_len, res)

		return (res_len == 1, res)

	def insert_new_user_without_error_handler(self, name: str, email: str, password: str, tel: str, can_view_user_table: bool=False, can_create_new_user: bool=False) -> None:
		self._execute_insert(
			table=self.user_table_name,
			fields=[
				"name",
				"email",
				"password",
				"tel",
				"can_view_user_table",
				"can_create_new_user"
			],
			values=[
				name,
				email,
				password,
				tel,
				can_view_user_table,
				can_create_new_user
			],
		)

		self._execute_commit()