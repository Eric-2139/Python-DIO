# Métodos de classe: estão ligados a classe e tem acesso ao seu estado, pois recebem um parâmetro que apontam para a classe

# Métodos estáticos: não recebe um primeiro argumento explícito, mas é um método vinculado à classe. Ele não pode acessar ou modificar o estado da classe, mas está presente porque faz sentido que o método esteja presente na classe

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_a_partir_data_nascimeto(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return Pessoa(nome, idade)
    
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18

# p = Pessoa('Eric', 19)
# print(p.nome, p.idade)

p = Pessoa.criar_a_partir_data_nascimeto(2005, 6, 14, 'Eric')
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(2))