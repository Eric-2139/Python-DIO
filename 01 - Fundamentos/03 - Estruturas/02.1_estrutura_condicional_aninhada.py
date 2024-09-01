conta_nomral = True
conta_universitaria = False

saldo = 2000
saque = 500
cheque_especial = 450

if conta_nomral:
    if saldo >= saque:
        print('Saque realizado')
    elif saldo <= (saldo + cheque_especial):
        print('Saque realizado com o uso do saque especial')
    else:
        print('Saldo insuficiente')
elif conta_universitaria:
    if saldo >= saque:
        print('Saque realizado com sucesso')
    else:
        print('Saldo insuficiente')
else:
    print('Tipo de conta não reconhecida')