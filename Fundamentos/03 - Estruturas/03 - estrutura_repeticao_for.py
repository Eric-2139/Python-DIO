texto = input('Informe um texto: ')
VOGAIS = 'AEIOU'

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()
    print('Executa no final do laço')


# range(start->inclusivo, end->exclusivo(n-1), step)
for numero in range(0, 51, 5):
    print(numero, end=" ")