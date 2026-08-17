import tkinter as tk
from .components import Input
from .page import Page

class Home(Page):
	def __init__(self, screenName = None, baseName = None, className = "Tk", useTk = True, sync = False, use = None, geometry: str = "400x300", title: str = "Home"):
		super().__init__(screenName, baseName, className, useTk, sync, use, geometry, title)

		self._create_widgets()
	
	def _create_widgets(self):
		texto = tk.Label(self, text="Hi")
		texto.pack(padx=20, pady=20)

		inp = Input(self, "test")
		inp.pack_all_widget(padx=20, pady=5)