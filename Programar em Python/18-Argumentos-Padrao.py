# Programar em Python #18 - Argumentos Padrão

def estadoDaPorta(estado = True):
	if estado:
		print('A porta está aberta!');
	else:
		print('A porta está fechada!');

estadoDaPorta(False);