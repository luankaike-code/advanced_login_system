class InvalidMasterError(Exception):
	def __init__(self, mensage) -> None:
		super().__init__(f"Invalid master error: {mensage}")