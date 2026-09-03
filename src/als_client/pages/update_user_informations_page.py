from .abstract_form_user_informations_page import AbstractFormUserInformationsPage

class UpdateUserInformationsPage(AbstractFormUserInformationsPage):
	def __init__(self, master, geometry: str = "400x500"):
		super().__init__(master, button_text="Atualizar", title="Atualizar usuário", geometry=geometry)