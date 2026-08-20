import customtkinter as ctk
from .components import Input, Popup, H1, Paragraph, Button
from .page import Page
from .als_requests import Request

class Login(Page):
	def __init__(self, geometry: str = "400x300", title: str = "Login") -> None:
		super().__init__(geometry, title)

		self._create_widgets()

	def check_login_informations(self) -> None:
		pass
	
	def _create_widgets(self) -> None:
		title = H1(self, text="Sistema Avançado de Login")
		title.pack(padx=10, pady=10)

		self.input_identity = Input(self, "Identificador", "Nome / Email / Telefone")
		self.input_identity.pack_all_widgets(padx=10, pady=5)

		self.input_password = Input(self, "Senha", "******")
		self.input_password.pack_all_widgets(padx=10, pady=5)

		self.error_msg = Paragraph(self, text="error")
		self.error_msg.pack(padx=10, pady=10)

		button = Button(self, text="Entrar" ,command=self.check_login_informations)
		button.pack(padx=10, pady=10)


		