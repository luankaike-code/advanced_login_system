from mysql.connector.types import RowItemType, RowType
from typing import Dict

class RowUser:
	def __init__(self, user_data: Dict[str, RowItemType]):
		self.dict = user_data
		self.id = user_data["user_id"]
		self.name = user_data["name"]
		self.email = user_data["email"]
		self.paaword = user_data["password"]
		self.tel = user_data["tel"]
		self.has_sudo_access = user_data["has_sudo_access"]