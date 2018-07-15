# Programar em Python #29 - Classes e Objetos

class Inimigo:
	vida = 5;

	def ataque(self):
		print('Eu fui atacado e perdi uma vida!');
		self.vida -= 1;

	def verificarVida(self):
		if self.vida <= 0:
			print('Eu estou morto porque não tenho mais vidas!');
		else:
			print('Eu ainda estou em combate e tenho', self.vida, 'vidas!');

inimigo1 = Inimigo();
inimigo2 = Inimigo();

inimigo1.ataque();
inimigo1.ataque();
inimigo1.ataque();
inimigo1.verificarVida();
inimigo2.verificarVida();