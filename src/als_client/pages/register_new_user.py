from .form_user_informations import FormUserInformations

class RegisterNewUser(FormUserInformations):
	def __init__(self, master, geometry: str = "400x500"):
		super().__init__(master, button_text="Cadastrar", title="Cadastrar usuário", display_password_input=True, geometry=geometry)