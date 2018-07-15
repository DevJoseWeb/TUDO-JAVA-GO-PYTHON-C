# Programar em Python #31 - Herança

class Pai:
	ultimoNome = 'Silva';

	def comidaPreferida(self):
		print('A minha comida preferida é arroz de marisco!');

class Filho(Pai):
	primeiroNome = 'Nelson';
	idade = 21;

	def informacao(self):
		print('Nome:', self.primeiroNome, self.ultimoNome);
		print('Idade:', self.idade);

pessoa = Filho();
pessoa.informacao();
pessoa.comidaPreferida();