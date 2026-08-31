from pages import Login, Home, SelfInformations
from pages.page import Page
from als_requests import Request
import atexit

class App():
	def __init__(self) -> None:
		atexit.register(Request.logout)
		self.current_window = None

	def __update_current_window(self, new_window: Page):
		if self.current_window:
			self.current_window.destroy()

		self.current_window = new_window
		self.current_window.mainloop()

	def _go_to_home(self) -> None:
		home_page = Home({
			"Ver minhas informações": lambda: print("Ver minhas informações"),
			"Acessar tabela de usuários": lambda: print("Acessar tabela de usuários"),
			"Cadastrar novo usuário": lambda: print("Cadastrar novo usuário"),
			"Sair": lambda: print("Sair")
		})

		self.__update_current_window(home_page)
	
	def start(self) -> None:
		login_page = Login(successful_login_callback=self._go_to_home)
		self.__update_current_window(login_page)