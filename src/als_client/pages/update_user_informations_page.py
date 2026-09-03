from .abstract_form_user_informations_page import AbstractFormUserInformationsPage
from als_requests import Request

class UpdateUserInformationsPage(AbstractFormUserInformationsPage):
	def __init__(self, master, geometry: str = "400x500"):
		super().__init__(master, button_text="Atualizar", title="Atualizar usuário", default_inputs_value=Request.get_self_infos(), geometry=geometry)