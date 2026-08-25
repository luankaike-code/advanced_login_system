import tkinter as tk
from pages import Login, Home

class App():
	def __init__(self):
		pass

	def _successful_login(self):
		Home().mainloop()
	
	def start(self):
		Login(successful_login_callback=self._successful_login).mainloop()