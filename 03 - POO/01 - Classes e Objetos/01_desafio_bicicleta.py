class Bicicleta:
    def __init__(self,  cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print('ding ding')

    def parar(self):
        print('Parando bicicleta')
        print('Bicicleta parada')

    def correr(self):
        print('R de Rapidão')

    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}'
   
b1 = Bicicleta('preta', 'caloi', 2024, 700)
b1.buzinar()
b1.correr()
b1.parar()
print(f'{b1.cor}, {b1.modelo}, {b1.ano}, {b1.valor}')

b2 = Bicicleta('verde', 'monark', 2002, 200)
# Bicicleta.buzinar(b2) == b2.buzinar()
print(b2)
