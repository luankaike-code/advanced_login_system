from mysql.connector.types import RowItemType, RowType
from typing import Dict

class RowUser:
	def __init__(self, user_data: Dict[str, RowItemType]):
		self.dict = user_data
		self.id = user_data.get("user_id")
		self.name = user_data.get("name")
		self.email = user_data.get("email")
		self.password = user_data.get("password")
		self.tel = user_data.get("tel")
		self.has_sudo_access = user_data.get("has_sudo_access")