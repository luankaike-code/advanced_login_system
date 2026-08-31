import customtkinter as ctk
from .components import H1, Paragraph, Button, Table
from .page import Page
from als_requests import Request
from typing import Callable

class SelfInformations(Page):
	def __init__(self, master: ctk.CTk, back_button_callback=Callable, geometry: str = "400x500", title: str = "Informações") -> None:
		super().__init__(master, geometry, title)
		
		self.infos = Request.get_self_infos()
		self.back_button_callback = back_button_callback

		self._create_widgets()
	
	def _create_widgets(self) -> None:
		H1(self, text=f"Olá, {self.infos.name}").pack(padx=10, pady=10)
		Paragraph(self, text="Suas informações abaixo").pack(padx=10, pady=10)
		table = Table(self)

		table_content = [
			[Paragraph(table, text="name"), Paragraph(table, text=self.infos.name)],
			[Paragraph(table, text="email"), Paragraph(table, text=self.infos.email)],
			[Paragraph(table, text="password"), Paragraph(table, text=self.infos.password)],
			[Paragraph(table, text="tel"), Paragraph(table, text=self.infos.tel)],
			[Paragraph(table, text="tem super acesso?"), Paragraph(table, text="sim" if self.infos.has_sudo_access else "não")]
		]

		table.set_content(table_content)
		table.pack()

		Button(self, text="Voltar", command=self.back_button_callback).pack()