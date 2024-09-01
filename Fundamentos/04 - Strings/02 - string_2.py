nome = 'Eric'
idade = 19
saldo = 45.56584

dados = {'nome': 'Eric', 'idade': '19'}

print('Nome: %s, Idade: %d' % (nome, idade)) # Old style

print('Nome: {}, Idade: {}'.format(nome, idade)) # Format
print('Nome: {1}, Idade: {0}'.format(idade, nome))
print('Nome: {nome}, Idade: {idade}'.format(idade = idade, nome = nome))
print('Nome: {nome}, Idade: {idade}'.format(**dados))

print(f'Nome: {nome}, idade: {idade}') # F String
print(f'Nome: {nome}, idade: {idade}, saldo: {saldo:10.2f}')