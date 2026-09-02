from .form_user_informations import FormUserInformations

class UpdateUserInformations(FormUserInformations):
	def __init__(self, master, geometry: str = "400x500"):
		super().__init__(master, button_text="Atualizar", title="Atualizar usuário", display_password_input=True, geometry=geometry)