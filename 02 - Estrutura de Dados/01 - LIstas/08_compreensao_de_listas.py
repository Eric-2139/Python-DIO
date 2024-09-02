numeros = [1, 30 ,25, 79, 65, 2, 4]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

######################################################################

numeros = [1, 30 ,25, 79, 65, 2, 4]
pares = [numero for numero in numeros if numero % 2 == 0]

print(pares)

######################################################################

numeros = [1, 30 ,25, 79, 65, 2, 4]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

print(quadrado)

######################################################################

numeros = [1, 30 ,25, 79, 65, 2, 4]
quadrado = [numero ** 2 for numero in numeros]

print(quadrado)