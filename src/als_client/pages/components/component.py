import customtkinter as ctk
from typing import Dict

class Component():
	def __init__(self) -> None:
		self._widgets: Dict[str, ctk.CTkBaseClass] = {}

	def pack(self, padx: int, pady: int) -> None:
		for widget in self._widgets.values():
			widget.pack(padx=padx, pady=pady)