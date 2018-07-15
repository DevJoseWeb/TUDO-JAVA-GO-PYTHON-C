# Programar em Python #21 - Variáveis Globais e Locais

acesso = 'Global';

def mudarAcesso():
	acesso = 'Local';
	print('Acesso no interior da função:', acesso);

mudarAcesso();
print('Acesso no exterior da função:', acesso);