import tkinter as tk

class Page(tk.Tk):
	def __init__(self, screenName = None, baseName = None, className = "Tk", useTk = True, sync = False, use = None, geometry: str = "400x300", title: str = "Page"):
		super().__init__(screenName, baseName, className, useTk, sync, use)

		self.title(title)
		self.geometry("400x300")

	def _create_widgets(self):
		pass