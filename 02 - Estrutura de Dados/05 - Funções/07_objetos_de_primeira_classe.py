# Em Python, tudo é objeto, dessa forma, funções também são objetos, o que as torna objetos de primeira classe. Com isso, podemos atribuir funções a variáveis, passa-las como parâmetros para funções, usá-las como valores em estruturas de dados(listas, tuplas, dicionários, etc) e usar como valor de retorno para uma função(closures). 

def somar(a, b):
    return 'adição',f'{a} + {b} = {a + b}' 

def subtrair(a, b):
    return f'subtração', f'{a} - {b} = {a - b}' 

def multiplicar(a, b):
    return f'multiplicação', f'{a} x {b} = {a * b}'

def dividir(a, b):
    return f'divisão', f'{a} / {b} = {a // b}'

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f'Resultado da operação de -> {resultado}')

exibir_resultado(10, 10, somar)
exibir_resultado(10, 10, subtrair)
exibir_resultado(10, 10, multiplicar)
exibir_resultado(10, 10, dividir)