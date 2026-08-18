import customtkinter as ctk
from .components import Input
from .page import Page

class Login(Page):
	def __init__(self, geometry: str = "400x300", title: str = "Login") -> None:
		super().__init__(geometry, title)

		self._create_widgets()

	def check_login_informations(self) -> None:
		pass
	
	def _create_widgets(self) -> None:
		title = ctk.CTkLabel(self, text="Sistema Avançado de Login")
		title.pack(padx=10, pady=10)

		self.input_identity = Input(self, "Identificador", "Nome / Email / Telefone")
		self.input_identity.pack_all_widgets(padx=10, pady=5)

		self.input_password = Input(self, "Senha", "******")
		self.input_password.pack_all_widgets(padx=10, pady=5)

		self.error_msg = ctk.CTkLabel(self)
		self.error_msg.pack(padx=10, pady=10)

		button = ctk.CTkButton(self, text="Entrar" ,command=self.check_login_informations)
		button.pack(padx=10, pady=10)


		