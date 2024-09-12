class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
   
    def mostrar(self):
      print(f'Nome: {self.nome}, Idade: {self.idade}')

nome = input('Digite um nome: ')
idade = int(input('Digite uma idade: '))

pessoa = Pessoa(nome, idade)

pessoa.mostrar()