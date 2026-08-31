from pages import Login, Home, SelfInformations
from pages.page import Page
import customtkinter as ctk
from als_requests import Request
import atexit

class App(ctk.CTk):
	def __init__(self) -> None:
		super().__init__()
		atexit.register(Request.logout)
		self.current_page = None

	def __destroy_current_page(self):
		if self.current_page and self.current_page.winfo_exists():
			self.current_page.destroy()

	def __update_current_page(self, new_page: Page):
		self.__destroy_current_page()

		self.current_page = new_page

		self.title(self.current_page.title)
		self.geometry(self.current_page.geometry)

		self.current_page.pack(fill="both", expand=True)

	def _go_to_home(self) -> None:
		home_page = Home(self, {
			"Ver minhas informações": lambda: print("Ver minhas informações"),
			"Acessar tabela de usuários": lambda: print("Acessar tabela de usuários"),
			"Cadastrar novo usuário": lambda: print("Cadastrar novo usuário"),
			"Sair": self.destroy
		})

		self.__update_current_page(home_page)
	
	def mainloop(self) -> None:
		login_page = Login(self, successful_login_callback=self._go_to_home)
		self.__update_current_page(login_page)

		super().mainloop()