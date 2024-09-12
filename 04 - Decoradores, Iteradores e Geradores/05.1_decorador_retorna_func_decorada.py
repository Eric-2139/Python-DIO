def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print('Faz algo antes de executar')
        resultado = funcao(*args, **kwargs)
        print('Faz algo depois de executar')
        return resultado

    return envelope

@meu_decorador
def ola_mundo(nome, idade):
    print(f'Olá mundo {nome} {idade}')
    return nome.upper()

resultado = ola_mundo('Eric', 19)
print(resultado)