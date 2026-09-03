import customtkinter as ctk
from .component import Component

class Input(Component):
	def __init__(self, window: ctk.CTk, label: str, placeholder: str="") -> None:
		super().__init__(window)

		self._widgets.update({
			"label": ctk.CTkLabel(window, text=label),
			"entry": ctk.CTkEntry(window, placeholder_text=placeholder)
		})

		self.default_entry_border_color = self._widgets["entry"].cget("border_color")

	def set_normal(self) -> None:
		self._widgets["entry"].configure(border_color=self.default_entry_border_color)
		self.master.focus_set()

	def set_error(self) -> None:
		self._widgets["entry"].configure(border_color="#FF5733")
		self._widgets["entry"].focus_set()

	def get_value(self) -> str:
		return self._widgets["entry"].get()