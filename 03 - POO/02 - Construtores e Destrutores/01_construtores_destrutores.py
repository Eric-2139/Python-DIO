# Método construtor: é executado quando uma nova instância de classe é criada. Nele inicializamos o estado do nosso projeto. Para declará-lo criamos um método com o nome __init__

# Método destrutor: é executado quando uma instância é destrída. Não são tão necessários em Python pois a linguagem tem um coletor de lixo que lida com o gerenciamento de memória. Para declará-lo criamos um método com o nome __del__

class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print('Inicializando a classe')
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print('Destruindo a instância')


    def latir(self):
        print('auau')

def criar_cachorro():
    c = Cachorro('Kratos', 'Cor da Guerra', False)
    print(c.nome)

c = Cachorro('Spike', 'malhado')
c.latir()
del c

criar_cachorro()

