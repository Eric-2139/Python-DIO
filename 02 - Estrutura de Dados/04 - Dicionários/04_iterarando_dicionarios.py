contatos = {
    'barakus2139@gmail.com': {'nome': 'Barakus', 'telefone': 'xxxx-xxxx'},
    'samael2139@gmail.com': {'nome': 'Samael', 'telefone': 'xxxx-xxxx'},
    'valefor2139@gmail.com': {'nome': 'Valefor', 'telefone': 'xxxx-xxxx'},
    'apollo@gmail.com': {'nome': 'Apollo', 'telefone': 'xxxx-xxxx'},
}

for chave in contatos:
    print(chave, contatos[chave])

print('')

for chave, valor in contatos.items():
    print(chave, valor) 