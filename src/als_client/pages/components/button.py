import customtkinter as CTk
from typing import Callable
from .fonts import font_normal

class Button(CTk.CTkButton):
	def __init__(self, master, text: str = "CTkButton", command: Callable | None = None, **kwargs) -> None:
		super().__init__(master, text=text, font=font_normal(), command=command, **kwargs)