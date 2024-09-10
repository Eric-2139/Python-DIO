# Todos os objetos nascem com a mesma quantidade de atributos de classe e instância. Atributos de instância são diferentes para cada objeto, já os atributos de classe são compartilhados entre os objetos

class Estudante:
    escola = 'Dio'

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f'{self.nome} - {self.matricula} - {self.escola}'

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

eric = Estudante('Eric', 1)
barakus = Estudante('Barakus', 2)
mostrar_valores(eric, barakus)

Estudante.escola = 'Python'
eric.matricula = 5
charles = Estudante('Charles', 3)
mostrar_valores(eric, barakus, charles)
