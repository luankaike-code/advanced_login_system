import tkinter as tk
from .components import Input
from .page import Page

class Home(Page):
	def __init__(self, screenName = None, baseName = None, className = "Tk", useTk = True, sync = False, use = None, geometry: str = "400x300", title: str = "Home"):
		super().__init__(screenName, baseName, className, useTk, sync, use, geometry, title)

		self._create_widgets()

	def check_login_informations(self):
		pass
	
	def _create_widgets(self):
		title = tk.Label(self, text="Sistema Avançado de Login")
		title.pack(padx=10, pady=10)

		self.input_identity = Input(self, "Identificador", "Nome / Email / Telefone")
		self.input_identity.pack_all_widgets(padx=10, pady=5)

		self.input_password = Input(self, "Senha", "******")
		self.input_password.pack_all_widgets(padx=10, pady=5)

		self.error_msg = tk.Label(self)
		self.error_msg.pack(padx=10, pady=10)

		button = tk.Button(self, text="Entrar" ,command=self.check_login_informations)
		button.pack(padx=10, pady=10)

		