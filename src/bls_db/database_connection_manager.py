import mysql.connector
from mysql.connector import Error
from mysql.connector.pooling import PooledMySQLConnection
from mysql.connector.abstracts import MySQLConnectionAbstract

class DatabaseConnectionManager:
	def __init__(self, host: str, port: int, database: str, user: str, password: str) -> None:
		self.__host = host
		self.__port = port
		self.__database = database
		self.__user = user
		self.__password = password

		self.__update_connection()

	def __update_connection(self) -> None:
		self.__connection = self.__create_connection()

		if self.__connection:
			self.__cursor = self.__connection.cursor()

	def __create_connection(self) -> (PooledMySQLConnection | MySQLConnectionAbstract | None):
		connection = None

		try:
			connection = mysql.connector.connect(
				host=self.__host,
				port=self.__port,
				database=self.__database,
				user=self.__user,
				password=self.__password,
			)
		except Error as e:
			print(f"Error while connecting to MySQL: {e}")

		return connection

	def __del__(self) -> None:
		if 'connection' in locals() and self.__connection.is_connected():
			self.__cursor.close()
			self.__connection.close()
			print("MySQL connection is closed.")