# del -> mais uma forma de remover valores

contatos = {
    'barakus2139@gmail.com': {'nome': 'Barakus', 'telefone': 'xxxx-xxxx'},
    'samael2139@gmail.com': {'nome': 'Samael', 'telefone': 'xxxx-xxxx'},
    'valefor2139@gmail.com': {'nome': 'Valefor', 'telefone': 'xxxx-xxxx'},
    'apollo@gmail.com': {'nome': 'Apollo', 'telefone': 'xxxx-xxxx'},
}

del contatos['apollo@gmail.com']
del contatos['barakus2139@gmail.com']['telefone']

print(contatos)