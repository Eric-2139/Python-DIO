# issuperset -> se todos os elementos de um conjunto não estão contidos em outro. O contrario do issubset

conjunto_A = {1, 2, 3, 5}
conjunto_B = {1, 2, 3, 4, 5, 7}

print(conjunto_A.issuperset(conjunto_B))
print(conjunto_B.issuperset(conjunto_A))