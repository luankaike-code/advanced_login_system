import customtkinter as ctk
from .page import Page
from .components import H1, Input, PasswordInput, Button

class FormUserInformations(Page):
	def __init__(
			self, 
			master: ctk.CTk,
			button_text: str,
			title: str,
			display_password_input: bool = False,
			geometry: str = "400x500"
		):
		super().__init__(master, geometry, title)

		self.button_text = button_text
		self.display_password_input = display_password_input

		self.input_name = Input(self, "Nome", "José Almeida")
		self.input_email = Input(self, "Email", "JoséAlmeida@gmail.com")
		self.input_password = PasswordInput(self, "Senha", "******")
		self.input_confirm_password = PasswordInput(self, "Confirme a Senha", "******")
		self.input_tel = Input(self, "Telefone", "(00) 0 0000-0000")

		self._create_widgets()

	def __send_button_callback(self) -> None:
		print(
			self.input_name.get_value(),
			self.input_email.get_value(),
			self.input_password.get_value(),
			self.input_tel.get_value(),
		)

	def _create_widgets(self) -> None:
		H1(self, self.title).pack(padx=10, pady=10)

		self.input_name.pack(padx=10, pady=5)
		self.input_email.pack(padx=10, pady=5)

		if self.display_password_input:
			self.input_password.pack(padx=10, pady=5)
			self.input_confirm_password.pack(padx=10, pady=5)
		
		self.input_tel.pack(padx=10, pady=5)

		Button(self, self.button_text, command=self.__send_button_callback).pack(padx=10, pady=5)
