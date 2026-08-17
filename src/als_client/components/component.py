import tkinter as tk
from typing import Dict

class Component():
	def __init__(self) -> None:
		self._widgets: Dict[str, tk.Widget] = {}

	def pack_all_widget(self, padx: int, pady: int) -> None:
		for widget in self._widgets.values():
			widget.pack(padx=padx, pady=pady)