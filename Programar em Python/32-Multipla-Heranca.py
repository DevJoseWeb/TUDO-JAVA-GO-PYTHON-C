# Programar em Python #32 - Múltipla Herança

class Pai:
	altura = 'Entre 180 e 190 centímetros';
	corDosOlhos = 'Castanhos';

class Mae:
	def corPreferida(self):
		print('A minha cor preferida é branco!');

class Filho(Pai, Mae):
	def informacao(self):
		print('Nome: Nelson Silva');
		print('Idade: 21');
		print('Altura:', self.altura);
		print('Cor dos olhos:', self.corDosOlhos);

pessoa = Filho();
pessoa.informacao();
pessoa.corPreferida();