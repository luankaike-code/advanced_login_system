import customtkinter as CTk
from .paragraph import Paragraph
from .hs import H1

class Popup(CTk.CTkToplevel):
	def __init__(self, *args, title = str, label = str, geometry: str ="200x100", freeze: bool = True, fg_color = None, **kwargs) -> None:
		super().__init__(*args, fg_color=fg_color, **kwargs)

		self.title(title)
		self.geometry(geometry)

		H1(self, text=title).pack(pady=10)

		Paragraph(self, text=label).pack(pady=5)

		if freeze:
			self.grab_set()