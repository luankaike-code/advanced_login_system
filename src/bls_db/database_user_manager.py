from mysql.connector import Error
from .database_commands_manager import DatabaseCommandsManager

# CREATE TABLE users (
# 	user_id INT PRIMARY KEY AUTO_INCREMENT,
# 	name VARCHAR(255) NOT NULL,
# 	email VARCHAR(255) UNIQUE NOT NULL,
# 	password VARCHAR(255) NOT NULL,
# 	tel VARCHAR(11) UNIQUE,
# 	can_view_user_table BOOL DEFAULT FALSE,
# 	can_create_new_user BOOL DEFAULT FALSE
# )

class DatabaseUserManager(DatabaseCommandsManager):
	def __init__(self, host: str, port: int, database: str, user: str, password: str):
		super().__init__(host, port, database, user, password)

	def insert_new_user(self, name: str, email: str, password: str, tel: str, can_view_user_table: bool=False, can_create_new_user: bool=False):
		try:
			self.insert_new_user_within_error_handler(name, email, password, tel, can_view_user_table, can_create_new_user)
		except Error as e:
			print(f"Error while insert new user: {e}")

	def insert_new_user_within_error_handler(self, name: str, email: str, password: str, tel: str, can_view_user_table: bool=False, can_create_new_user: bool=False):
		self._execute_insert(
			table="users",
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