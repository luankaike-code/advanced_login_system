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

	def __destroy_current_page(self) -> None:
		if self.current_page and self.current_page.winfo_exists():
			self.current_page.destroy()

	def __update_current_page(self, new_page: Page) -> None:
		self.__destroy_current_page()

		self.current_page = new_page

		self.title(self.current_page.title)
		self.geometry(self.current_page.geometry)

		self.current_page.pack(fill="both", expand=True)

	def __to_go_self_informations(self) -> None:
		self_informations_page = SelfInformations(self, back_button_callback=self._to_go_home)
		
		self.__update_current_page(self_informations_page)

	def _to_go_home(self) -> None:
		home_page = Home(self, {
			"Ver minhas informações": self.__to_go_self_informations,
			"Acessar tabela de usuários": lambda: print("Acessar tabela de usuários"),
			"Cadastrar novo usuário": lambda: print("Cadastrar novo usuário"),
			"Sair": self.destroy
		})

		self.__update_current_page(home_page)

	def _to_go_login(self, try_logout: bool = True) -> None:
		if try_logout:
			Request.logout()

		login_page = Login(self, successful_login_callback=self._to_go_home)
		self.__update_current_page(login_page)
	
	def mainloop(self) -> None:
		self._to_go_login(False)

		super().mainloop()