import tkinter as tk
from .component import Component

class Input(Component):
	def __init__(self, window: tk.Tk, label: str) -> None:
		super().__init__()

		self._widgets.update({
			"label": tk.Label(window, text=label),
			"entry": tk.Entry(window)
		})

	def get_value(self) -> str:
		entry: tk.Entry = self._widgets["entry"]
		return entry.get()