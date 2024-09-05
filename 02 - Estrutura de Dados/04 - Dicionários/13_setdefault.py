# setdefault -> se o atributo não estiver no dicionário, ele o cria, caso o atributo ja exista, ele retorna o atributo ja existente

contatos = {'nome': 'Barakus', 'telefone': 'xxxx-xxxx'}

print(contatos.setdefault('nome', 'Eric'))
print(contatos)

print(contatos.setdefault('idade', 21))
print(contatos)
