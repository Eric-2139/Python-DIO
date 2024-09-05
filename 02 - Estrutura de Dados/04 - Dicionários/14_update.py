# update -> atualiza o dicionário, se for para uma chave existente, ele ira substituir os valores atuais pelo o especificado, caso a chave não exista, ele irá criar a chave


contatos = {
    'barakus2139@gmail.com': {'nome': 'Barakus', 'telefone': 'xxxx-xxxx'},
    'samael2139@gmail.com': {'nome': 'Samael', 'telefone': 'xxxx-xxxx'},
    'valefor2139@gmail.com': {'nome': 'Valefor', 'telefone': 'xxxx-xxxx'},
    'apollo@gmail.com': {'nome': 'Apollo', 'telefone': 'xxxx-xxxx'},
}

contatos.update({'barakus2139@gmail.com': {'nome': 'Ishiki Shimazu Sasaki'}})
print(contatos)

contatos.update({'smokerjoker@gmail.com': {'nome': 'Smoker Joker'}})
print(contatos)