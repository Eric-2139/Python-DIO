# Interface: define um contrato, onde são declarados os métodos e suas respectivas assinaturas. Em Python, utilizamos classe abstratas para criar contratos. Elas não podem ser instanciadas

# ABC: é o módulo que fornece a base para definir classes abstratas pois, por padrão, o Python não fornece classes abstratas. O ABC funciona decorando métodos da classe base como abstratos e, em seguida, registrando classes concretas como implementações da base abstrata. Um método se abstrato quando decorado com *@abstractmethod*

from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractmethod
    def marca(self):
        pass

    
class ControleTV(ControleRemoto):
    def ligar(self):
        print('Ligando a TV')

    def desligar(self):
        print('Desligando a TV')

    @property
    def marca(self):
        return 'LG'
    
       
class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print('Ligando ar-condicionado')

    def desligar(self):
        print('Desligando ar-condicionado')
    
    @property
    def marca(self):
        return 'samsumg'
    

controle = ControleTV()
controle.ligar()
controle.desligar()

controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)