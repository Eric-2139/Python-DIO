def contar_caracteres(string):
    contador = {}

    for char in string:
        if char in contador:
            contador[char] += 1
        else:
            contador[char] = 1
    
    return contador

entrada = input('Digite uma palavra ou uma frase: ')
resultado = contar_caracteres(entrada)
print(resultado)