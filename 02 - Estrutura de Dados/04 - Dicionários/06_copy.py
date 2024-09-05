# copy -> faz uma cópia do dicionário

contatos = {
    'barakus2139@gmail.com': {'nome': 'Barakus', 'telefone': 'xxxx-xxxx'},
    'samael2139@gmail.com': {'nome': 'Samael', 'telefone': 'xxxx-xxxx'},
    'valefor2139@gmail.com': {'nome': 'Valefor', 'telefone': 'xxxx-xxxx'},
    'apollo@gmail.com': {'nome': 'Apollo', 'telefone': 'xxxx-xxxx'},
}

copia = contatos.copy()
copia['valefor2139@gmail.com'] = {'nome': 'Djinn do Gelo Valefor'}

print(contatos['valefor2139@gmail.com']['nome'])
print(copia['valefor2139@gmail.com']['nome'])