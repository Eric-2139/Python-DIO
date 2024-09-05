# popitem -> vai removendo os itens um a um, caso o dicionário esteja vazio, retorna um KeyError

contatos = {
    'barakus2139@gmail.com': {'nome': 'Barakus', 'telefone': 'xxxx-xxxx'},
    'samael2139@gmail.com': {'nome': 'Samael', 'telefone': 'xxxx-xxxx'},
    'valefor2139@gmail.com': {'nome': 'Valefor', 'telefone': 'xxxx-xxxx'},
    'apollo@gmail.com': {'nome': 'Apollo', 'telefone': 'xxxx-xxxx'},
}

print(contatos.popitem())
print(contatos)