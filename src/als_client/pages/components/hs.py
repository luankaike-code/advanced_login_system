import customtkinter as CTk
from .fonts import font_h1, font_h2

class H1(CTk.CTkLabel):
	def __init__(self, master, text = "H1", **kwargs):
		super().__init__(master, text=text, font=font_h1(), **kwargs)

class H2(CTk.CTkLabel):
	def __init__(self, master, text = "H2", **kwargs):
		super().__init__(master, text=text, font=font_h1(), **kwargs)
