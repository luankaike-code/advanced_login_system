import os
from dotenv import load_dotenv
from typing import Literal
from .database_managers import DatabaseManager

class TableManager(DatabaseManager):
	def __init__(self, table_name_env: Literal["TABLE_CONNECTIONS", "TABLE_USERS"], host: str, port: int, database: str, user: str, password: str):
		super().__init__(host, port, database, user, password)
		load_dotenv()
		self.table_name = os.getenv(table_name_env)