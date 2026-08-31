import customtkinter as ctk

class Page(ctk.CTkFrame):
	def __init__(self, master: ctk.CTk, geometry: str = "400x300", title: str = "Page") -> None:
		super().__init__(master)

		self.title = title
		self.geometry = geometry

	def _create_widgets(self) -> None:
		pass