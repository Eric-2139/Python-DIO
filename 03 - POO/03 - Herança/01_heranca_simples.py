# Herança: capacidade de uma classe-filha derivar ou herdar as características e comportamentos da classe-pai

# Herança simples: quando uma classe-filha herda apenas uma classe-pai

class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print('Ligando motor')
        
class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado
        

    def esta_carregado(self):
        print(f'{'Sim' if self.carregado else 'Não'} estou carregado')

    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}'

moto = Motocicleta('preta', 'wqs-2368', 2)
moto.ligar_motor()

carro = Carro('prata', 'xjs-0241', 4)
carro.ligar_motor()

caminhao = Caminhao('vermelho', 'gdj-9874', 8, True)
caminhao.ligar_motor()
caminhao.esta_carregado()

print(moto)
print(carro)
print(caminhao)
