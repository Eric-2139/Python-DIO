def soma_tupla(tupla):
    return sum(tupla)

if __name__ == "__main__": # verifica se o script foi executado diretamente
    entrada = input('Digite uma sequência de numeros com um espaçamento entre eles, exemplo: 2 6 5 4...: ')
    elementos = tuple(map(int, entrada.split()))
    
    resultado = soma_tupla(elementos)
    print(f"A soma dos elementos da tupla é: {resultado}")