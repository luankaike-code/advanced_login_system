from .table_users_manager import TableUsersManager
from .table_connections_manager import TableConnectionsManager

class TableManagers():
	_instance: TableManagers = None

	def __init__(self, host: str, port: int, database: str, user: str, password: str):
		if getattr(self, "_initialized", False):
			return
		self._initialized = True

		self.users = TableUsersManager(
			host=host,
			port=port,
			database=database,
			user=user,
			password=password
		)

		self.connections = TableConnectionsManager(
			host=host,
			port=port,
			database=database,
			user=user,
			password=password
		)

	def __new__(cls, *args):
		if cls._instance == None:
			cls._instance = super().__new__(cls)
		return cls._instance