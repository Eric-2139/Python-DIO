''' 
Geradores: tipos especiais de iteradores, ao contrário das listas ou outros iteráveis, não armazenam todos os seus valores na memória. São definidos usando funções regulares, mas ao invés de retornar valores usando 'return', utilizam 'yield'

Características: 
Quando um item gerado é consumido, ele não pode mais ser acessado
O estado interno de um gerador é mantido entre chamadas
A sua execução é pausada no 'yield' e retomada da próxima vez que for chamado
'''

def meu_gerador(numeros: list[int]):
    for numero in numeros:
        yield numero * 2

for i in meu_gerador(numeros=[1, 2, 3]):
    print(i)