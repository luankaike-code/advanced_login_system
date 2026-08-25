import requests, os
from dotenv import load_dotenv
from .errors import TryRequestWhithoutLoggedError
from als_db.table_managers.types import RowUser

load_dotenv()

DOMAIN = os.getenv("DOMAIN")
URL_LOGIN = f"{DOMAIN}{os.getenv("ROUTE_LOGIN")}"
URL_LOGOUT = f"{DOMAIN}{os.getenv("ROUTE_LOGOUT")}"
URL_GET_SELF = f"{DOMAIN}{os.getenv("ROUTE_GET_SELF")}"

class Request:
	_token: str = ""
	_is_logged: bool = False

	@staticmethod
	def __check_login_status():
		if not Request._is_logged:
			raise TryRequestWhithoutLoggedError()

	@staticmethod
	def try_login(identity: str, password: str) -> tuple[bool, int]:
		json_data = {'identity': identity, 'password': password}

		fetch_response = requests.post(URL_LOGIN, json=json_data)

		json = fetch_response.json()

		print(f"Request::try_login fetch -> code: {fetch_response.status_code}, response: {json["response"]}")

		Request._is_logged = fetch_response.status_code == 200
		if Request._is_logged:
			Request._token = json["token"]
		
		return Request._is_logged, fetch_response.status_code

	@staticmethod
	def logout() -> None:
		if not Request._is_logged:
			print(f"Request::logout print: you not logged")
			return
		elif Request._token.strip() == "":
			print(f"Request::logout print: you not have token")
			Request._is_logged = False
			return

		json_data = {"token": Request._token}
		
		fetch_response = requests.post(URL_LOGOUT, json=json_data)

		json = fetch_response.json()

		print(f"Request::logout fetch -> code: {fetch_response.status_code}, response: {json["response"]}")
		URL_LOGOUT
		

	@staticmethod
	def get_self_infos() -> RowUser | None:
		Request.__check_login_status()
		json_data = {'token': Request._token}

		fetch_response = requests.post(URL_GET_SELF, json=json_data)

		self_data = fetch_response.json()

		print(f"Request::get_self_infos fetch -> code: {fetch_response.status_code}, response: {self_data}")

		if fetch_response.status_code != 200:
			return None
		return RowUser(self_data)