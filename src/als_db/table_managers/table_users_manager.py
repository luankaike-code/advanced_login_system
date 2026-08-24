from mysql.connector import Error
from mysql.connector.types import RowItemType, RowType
from typing import Literal, List, Dict, Any

from .table_manager import TableManager
from ..errors import DuplicateLoginInformationError
from .types import RowUser

class TableUsersManager(TableManager):
	def __init__(self, host: str, port: int, database: str, user: str, password: str) -> None:
		super().__init__("TABLE_USERS", host, port, database, user, password)

	def get_user_using_id(self, user_id: int) -> RowUser | None:
		data = self._execute_select(
			table=self.table_name,
			fields=[
				"*",
			],
			where_query="user_id = %s",
			values=[
				user_id
			]
		)

		if len(data) < 1:
			return None
		return RowUser(data[0])

	def insert_new_user(self, name: str, email: str, password: str, tel: str, has_sudo_access: bool = False) -> None:
		try:
			self.insert_new_user_without_error_handler(name, email, password, tel, has_sudo_access)
		except Error as e:
			print(f"Error while insert new user: {e}")

	def check_login_information_without_error_handler(self, identifity: str, identifier_type: Literal["name", "email", "tel"], password: str) -> tuple[bool, RowUser | List[RowType | Dict[str, RowItemType]] | Any]:
		res = self._execute_select(
			table=self.table_name,
			fields="*",
			where_query=f"{identifier_type} = %s AND password = %s",
			values=[
				identifity,
				password
			]
		)

		res_len = len(res)
		
		if res_len > 1:
			raise DuplicateLoginInformationError(self.table_name, res_len, res)

		res_status = res_len == 1

		return (res_status, RowUser(res[0]) if res_status else res)

	def insert_new_user_without_error_handler(self, name: str, email: str, password: str, tel: str, has_sudo_access: bool = False) -> None:
		self._execute_insert(
			table=self.table_name,
			fields=[
				"name",
				"email",
				"password",
				"tel",
				"has_sudo_access",
			],
			values=[
				name,
				email,
				password,
				tel,
				has_sudo_access,
			],
		)

		self._execute_commit()