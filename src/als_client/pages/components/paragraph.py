import customtkinter as CTk
from .fonts import font_normal

class Paragraph(CTk.CTkLabel):
	def __init__(self, master, text: str = "paragraph", **kwargs) -> None:
		self.text = CTk.StringVar(value=text)

		super().__init__(master, textvariable=self.text, font=font_normal(), **kwargs)