# Iterador: é um objeto que contém um número contável de valores que podem ser iterados, o que significa que você pode percorrer todos os valores. O protocolo do iterador é uma maneira do Python fazer a iteração de  um objeto, que consiste em dois métodos especiais: '__iter__()' e '__next__()'

class MeuIterador:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2
        except IndexError:
            raise StopIteration

for i in MeuIterador(numeros=[23, 45 ,78 ,5561]):
    print(i)

