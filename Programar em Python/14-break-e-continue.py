# Programar em Python #14 - break e continue

numero = 0;
animais = ['Cão', 'Gato', 'Galinha', 'Coelho', 'Leão'];

for animal in animais:
	print('Animal:', animal);

	if animal == 'Coelho':
		break;

while numero < 10:
	numero += 1;

	if numero == 5:
		continue;

	print('Número da volta:', numero);