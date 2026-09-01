import customtkinter as CTk
from .errors import InvalidMasterError

class Table(CTk.CTkFrame):
	def __init__(self, master, width = 200, height = 200):
		super().__init__(master, width, height)

	def set_content(self, content_data: list[list[CTk.CTkBaseClass]] | None = None) -> None:
		self.__content_data = content_data
		self.__update_data()

	def __update_data(self) -> None:
		if self.__content_data is None:
			return
		
		column_count = len(self.__content_data[0])
		columns_index = list(i for i in range(column_count))
		self.grid_columnconfigure(columns_index, weight=1)

		for row, row_data in enumerate(self.__content_data):
			for column, component in enumerate(row_data):
				if component.master != self:
					raise InvalidMasterError("All table´s children must have it how master")
				component.grid(row=row, column=column, padx=20, pady=20)