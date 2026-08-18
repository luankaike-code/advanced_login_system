import customtkinter as ctk
from .component import Component

class Input(Component):
	def __init__(self, window: ctk.CTk, label: str, placeholder: str="") -> None:
		super().__init__()

		self.entry_value = ctk.StringVar()

		self._widgets.update({
			"label": ctk.CTkLabel(window, text=label),
			"entry": ctk.CTkEntry(window, placeholder_text=placeholder, textvariable=self.entry_value)
		})