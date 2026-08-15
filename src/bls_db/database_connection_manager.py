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

		self.__update_connection()

	def __update_connection(self) -> None:
		self.__connection = self.__create_connection()

		if self.__connection:
			self.__cursor = self.__connection.cursor()

	def __create_connection(self) -> (PooledMySQLConnection | MySQLConnectionAbstract | None):
		connection = None
		connection_attemps = 0
		errors = []

		def print_all_throw_errors():
			for i, error in enumerate(errors):
				print(f"Error #{i} throw while connecting to MySQL: {error}")

		while connection_attemps < MAX_CONNECTION_ATTEMPS:
			try:
				connection = mysql.connector.connect(
					host=self.__host,
					port=self.__port,
					database=self.__database,
					user=self.__user,
					password=self.__password,
				)
			except Error as e:
				errors.append(e)
				connection_attemps += 1
		else:
			print_all_throw_errors()

		return connection

	def __del__(self) -> None:
		if 'connection' in locals() and self.__connection.is_connected():
			self.__cursor.close()
			self.__connection.close()
			print("MySQL connection is closed.")