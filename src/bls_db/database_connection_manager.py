import os, mysql.connector
from mysql.connector import Error
from mysql.connector.pooling import PooledMySQLConnection
from mysql.connector.abstracts import MySQLConnectionAbstract
from dotenv import load_dotenv

load_dotenv()

MAX_CONNECTION_ATTEMPS = int(os.getenv("MAX_CONNECTION_ATTEMPS"))

class DatabaseConnectionManager:
	def __init__(self, host: str, port: int, database: str, user: str, password: str) -> None:
		self.__host = host
		self.__port = port
		self.__database = database
		self.__user = user
		self.__password = password

		self._update_connection()

	def _update_connection(self) -> None:
		self._connection = self._create_connection()

		if self._connection:
			self._cursor = self._connection.cursor()

	def _create_connection(self) -> (PooledMySQLConnection | MySQLConnectionAbstract | None):
		connection = None
		connection_attemps = 0

		while connection_attemps < MAX_CONNECTION_ATTEMPS and connection == None:
			try:
				connection = mysql.connector.connect(
					host=self.__host,
					port=self.__port,
					database=self.__database,
					user=self.__user,
					password=self.__password,
				)
			except Error as e:
				connection_attemps += 1
				print(f"Error #{connection_attemps} throw while connecting to MySQL: {e}; attempting again...")

		return connection

	def __del__(self) -> None:
		if 'connection' in locals() and self._connection.is_connected():
			self._cursor.close()
			self._connection.close()
			print("MySQL connection is closed.")