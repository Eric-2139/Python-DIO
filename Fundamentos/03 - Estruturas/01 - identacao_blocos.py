def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print('valor sacado')
    else:
        print('saldo insuficente')

def depositar(valor):
    saldo = 500
    saldo += valor
    print(saldo)

sacar(1000)
depositar(500)