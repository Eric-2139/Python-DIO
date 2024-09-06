def elementos_comuns(set1, set2):
    return list(set1.intersection(set2))

lista1 = set(input('Digite uma sequência de numeros separados por espaço como no exemplo: 5 6 9 8: ').split())
lista2 = set(input('Digite outra sequência de numeros: ').split())

if all(item.isdigit() for item in lista1) and all(item.isdigit() for item in lista2):
    set1 = set(map(int, lista1))
    set2 = set(map(int, lista2))
    comuns = elementos_comuns(set1, set2)
    print(f"Elementos comuns às duas listas: {comuns}")
else:
    print("Entrada inválida.")