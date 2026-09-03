from .abstract_form_user_informations_page import AbstractFormUserInformationsPage

class RegisterNewUserPage(AbstractFormUserInformationsPage):
	def __init__(self, master, geometry: str = "400x500"):
		super().__init__(master, button_text="Cadastrar", title="Cadastrar usuário", geometry=geometry)