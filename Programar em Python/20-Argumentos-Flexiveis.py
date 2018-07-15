# Programar em Python #20 - Argumentos Flexíveis

def imprimirArgumentos(*argumentos):
	for argumento in argumentos:
		print('Argumento:', argumento);

imprimirArgumentos(1, 1.5, 'Eu sou uma string!', True, ['ABC', 'DEF', 'GHI']);