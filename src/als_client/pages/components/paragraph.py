import customtkinter as CTk
from .fonts import font_normal

class Paragraph(CTk.CTkLabel):
	def __init__(self, master, text = "paragraph", **kwargs):
		super().__init__(master, text=text, font=font_normal(), **kwargs)