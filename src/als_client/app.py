from pages import Login, Home, SelfInformations
from als_requests import Request
import atexit

class App():
	def __init__(self):
		atexit.register(Request.logout)

	def _successful_login(self):
		Home({
			"Ver minhas informações": lambda: print("Ver minhas informações"),
			"Acessar tabela de usuários": lambda: print("Acessar tabela de usuários"),
			"Cadastrar novo usuário": lambda: print("Cadastrar novo usuário"),
			"Sair": lambda: print("Sair")
		}).mainloop()
	
	def start(self):
		Login(successful_login_callback=self._successful_login).mainloop()