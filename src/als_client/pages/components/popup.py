import customtkinter as CTk

class Popup(CTk.CTkToplevel):
	def __init__(self, *args, title = str, label = str, geometry: str ="200x100", freeze: bool = True, fg_color = None, **kwargs) -> None:
		super().__init__(*args, fg_color=fg_color, **kwargs)

		self.title(title)
		self.geometry(geometry)

		CTk.CTkLabel(self, text=title).pack(pady=10)

		CTk.CTkLabel(self, text=label).pack(pady=5)

		if freeze:
			self.grab_set()