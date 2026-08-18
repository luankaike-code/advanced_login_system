import customtkinter as ctk

class Page(ctk.CTk):
	def __init__(self, geometry: str = "400x300", title: str = "Page") -> None:
		super().__init__()

		self.title(title)
		self.geometry(geometry)

	def _create_widgets(self) -> None:
		pass