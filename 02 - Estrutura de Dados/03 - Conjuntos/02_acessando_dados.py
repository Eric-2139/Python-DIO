# Conjuntos em Python não suportam indexação e fatiamento, para acessar os seu valores é necessário converte-lo numa lista

numeros = {1, 2, 3, 1, 2}
numeros = list(numeros)

print(numeros[0])