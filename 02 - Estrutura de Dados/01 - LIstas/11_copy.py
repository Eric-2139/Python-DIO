# copy -> gera uma cópia

lista = ['Espada Longa', 'Katana', 'Foice', 'Fuzil']

l2 = lista.copy()

print(lista)
print(l2)
print(id(l2), id(lista))

l2[0] = 2

print(lista)
print(l2)