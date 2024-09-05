# get -> uma forma de acessar valores de um dicionário

contatos = {
    'barakus2139@gmail.com': {'nome': 'Barakus', 'telefone': 'xxxx-xxxx'},
    'samael2139@gmail.com': {'nome': 'Samael', 'telefone': 'xxxx-xxxx'},
    'valefor2139@gmail.com': {'nome': 'Valefor', 'telefone': 'xxxx-xxxx'},
    'apollo@gmail.com': {'nome': 'Apollo', 'telefone': 'xxxx-xxxx'},
}

# contatos['chave'] # KeyError

print(contatos.get('chave'))
print(contatos.get('chave'), {})
print(contatos.get('barakus2139@gmail.com', {}))