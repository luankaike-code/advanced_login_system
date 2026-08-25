from .abstract_home import AbstractHome

class Home(AbstractHome):
	def __init__(self,  geometry: str = "400x300", title: str = "Login") -> None:
		super().__init__({
			"Ver minhas informações": lambda: print("Ver minhas informações"),
			"Acessar tabela de usuários": lambda: print("Acessar tabela de usuários"),
			"Cadastrar novo usuário": lambda: print("Cadastrar novo usuário"),
			"Sair": lambda: print("Sair")
		}, geometry, title)
