import requests

class Request:
	_token: str = ""
	_is_logged: bool = False

	@staticmethod
	def try_login(identity: str, password: str) -> tuple[bool, int]:
		json_data = {'identity': identity, 'password': password}

		fetch_response = requests.post('http://127.0.0.1:5000/users/login', json=json_data)

		json = fetch_response.json()

		fetch_response.status_code

		print(f"Request::try_login fetch -> code: {fetch_response.status_code}, response: {json["response"]}")

		Request._is_logged = fetch_response.status_code == 200
		if Request._is_logged:
			Request._token = json["token"]
		
		return Request._is_logged, fetch_response.status_code
