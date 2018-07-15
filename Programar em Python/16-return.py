# Programar em Python #16 - return

def adicao():
	resultado = 0;

	for numero in range(1, 11):
		resultado += numero;

	return resultado;

print('Resultado da adição:', adicao());