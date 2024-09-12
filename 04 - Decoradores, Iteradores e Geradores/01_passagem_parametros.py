def mensagem(nome):
    print('Executadno mensagem')
    return f'Oi {nome}'

def mensagem_longa(nome):
    print('Executando mensagemm longa')
    return f'Olá, tudo bem com você {nome}?'

def executar(funcao, nome):
    print('Executando executar')
    return funcao(nome)

print(executar(mensagem, 'Eric'))
print(executar(mensagem_longa, 'Eric'))