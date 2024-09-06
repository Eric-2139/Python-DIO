def exibir_mensagem():
    print('Hello World')

def exibir_mensagem_2(nome):
    print(f'Bem-vindo {nome}')

def exibir_mensagem_3(nome = 'Anônimo'):
    print(f'Bem-vindo {nome}')

exibir_mensagem()
exibir_mensagem_2('Eric')
exibir_mensagem_3()
exibir_mensagem_3(nome = 'Eu')