# Programar em Python #30 - init

class Pessoa:
	def __init__(self, primeiroNome, ultimoNome, idade):
		self.primeiroNome = primeiroNome;
		self.ultimoNome = ultimoNome;
		self.idade = idade;

	def informacao(self):
		print('Nome:', self.primeiroNome, self.ultimoNome);
		print('Idade:', self.idade);

	def verificarEntrada(self):
		if self.idade >= 18:
			print('Esta pessoa pode entrar no local porque tem mais de 18 anos!');
		else:
			print('Esta pessoa não pode entrar no local porque tem menos de 18 anos!');

pessoa1 = Pessoa('Nelson', 'Silva', 21);
pessoa2 = Pessoa('Marta', 'Antunes', 17);

pessoa1.informacao();
pessoa1.verificarEntrada();

pessoa2.informacao();
pessoa2.verificarEntrada();