# Programar em Python #27 - Ficheiros (Ler e Escrever)

escreverFicheiro = open('27-Ficheiros-Ler-e-Escrever.txt', 'w');
escreverFicheiro.write('Eu estou a escrever na primeira linha deste ficheiro!\n');
escreverFicheiro.write('Agora estou a escrever na segunda linha!');
escreverFicheiro.close();

lerFicheiro = open('27-Ficheiros-Ler-e-Escrever.txt', 'r');
print(lerFicheiro.read());
lerFicheiro.close();