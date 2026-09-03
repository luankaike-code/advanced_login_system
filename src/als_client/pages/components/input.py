import customtkinter as ctk
from .component import Component

class Input(Component):
	def __init__(self, window: ctk.CTk, label: str, placeholder: str="") -> None:
		super().__init__(window)

		self._widgets.update({
			"label": ctk.CTkLabel(window, text=label),
			"entry": ctk.CTkEntry(window, placeholder_text=placeholder)
		})

	def get_value(self) -> str:
		return self._widgets["entry"].get()