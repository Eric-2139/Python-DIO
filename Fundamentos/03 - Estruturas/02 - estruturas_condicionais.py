MAIOR_IDADE = 18
IDADE_ESPECIAL = 16

idade = int(input('Informe a sua idade: '))

if idade >= MAIOR_IDADE:
    print('Pode tirar a cnh')

if idade <= MAIOR_IDADE:
    print('Não pode tirar a cnh')

#################################################################  

if idade >= MAIOR_IDADE:
    print('Pode tirar a cnh')
else:
    print('Não pode tirar a cnh')

#################################################################

if idade >= MAIOR_IDADE:
    print('Pode tirar a cnh')
elif idade == IDADE_ESPECIAL:
    print('Pode somente fazer aulas teóricas')
else:
    print('Não pode tirar a cnh')
