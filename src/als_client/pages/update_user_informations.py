from .abstract_form_user_informations import AbstractFormUserInformations

class UpdateUserInformations(AbstractFormUserInformations):
	def __init__(self, master, geometry: str = "400x500"):
		super().__init__(master, button_text="Atualizar", title="Atualizar usuário", display_password_input=True, geometry=geometry)