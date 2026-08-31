import customtkinter as ctk
from typing import Dict, Callable
from .components import H1, Paragraph, Button
from .page import Page
from als_requests import Request

class Home(Page):
	def __init__(self, master: ctk.CTk, buttons: Dict[str, Callable], geometry: str = "400x300", title: str = "Login") -> None:
		super().__init__(master, geometry, title)

		self._create_widgets(buttons)
	
	def _create_widgets(self,  buttons: Dict[str, Callable]) -> None:
		self_data = Request.get_self_infos()

		H1(self, text=f"Olá, {self_data.name}").pack(padx=10, pady=10)
		Paragraph(self, text="Seja bem-vindo(a)").pack(padx=10, pady=10)

		for btn_text, btn_callback in buttons.items():
			Button(self, text=btn_text, command=btn_callback).pack(padx=10, pady=10)
