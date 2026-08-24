from .components import H1, Paragraph
from .page import Page
from als_requests import Request

class Home(Page):
	def __init__(self, geometry: str = "400x300", title: str = "Login") -> None:
		super().__init__(geometry, title)

		self._create_widgets()
	
	def _create_widgets(self) -> None:
		self_data = Request.get_self_infos()

		H1(self, text=f"Olá, {self_data.name}").pack(padx=10, pady=10)
		Paragraph(self, text="Seja bem-vindo(a)").pack(padx=10, pady=10)
