import tkinter as tk
from pages import Login, Home
from als_requests import Request
import atexit

class App():
	def __init__(self):
		atexit.register(Request.logout)

	def _successful_login(self):
		Home().mainloop()
	
	def start(self):
		Login(successful_login_callback=self._successful_login).mainloop()