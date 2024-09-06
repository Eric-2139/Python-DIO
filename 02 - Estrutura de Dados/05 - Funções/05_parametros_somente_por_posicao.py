# Argumentos podem ser passados para uma função Python tanto por posição, quanto explicitamente pelo nome. Para melhor legibilidade e desempenho, faz sentido restringir a maneira pelo qual argumentos possam ser passados, assim um dev precisa apenas olhar para a definição da função para determinar se os itens são passados *por posição, por posição e nome, ou por nome*

# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#  positional only|positional or keyword|keyword only

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro('Palio', 1999, 'ABC-1234', marca='Fiat', motor='1.0', combustivel='Gasolina')