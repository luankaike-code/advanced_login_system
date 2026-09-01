import customtkinter as ctk
from .input import Input

class PasswordInput(Input):
	def __init__(self, window: ctk.CTk, label: str, placeholder: str = ""):
		super().__init__(window, label, placeholder)

		self.blind_char = "*"

		entry: ctk.CTkEntry = self._widgets["entry"]
		entry.configure(show=self.blind_char)
	
	def setValueVisibilityToUser(self, value: bool):
		entry: ctk.CTkEntry = self._widgets["entry"]
		entry.configure(
			show="" if value else self.blind_char
		)
	
	def toggleValueVisibilityToUser(self):
		entry: ctk.CTkEntry = self._widgets["entry"]
		self.setValueVisibilityToUser(entry.cget("show") == self.blind_char)