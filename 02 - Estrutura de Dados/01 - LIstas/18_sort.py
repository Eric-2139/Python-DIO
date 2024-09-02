# sort -> ordena a lista

linguagens = ['python', 'js', 'c', 'java', 'c#']
linguagens.sort() # ordena por ordem alfabética
print(linguagens)

linguagens = ['python', 'js', 'c', 'java', 'c#']
linguagens.sort(reverse=True) # ordena por ordem alfabética reversa
print(linguagens)

linguagens = ['python', 'js', 'c', 'java', 'c#']
linguagens.sort(key=lambda x: len(x)) # ordena por ordem crescente de tamanho | len = tamanho
print(linguagens)

linguagens = ['python', 'js', 'c', 'java', 'c#']
linguagens.sort(key=lambda x: len(x), reverse=True) # ordena por ordem decrescente tamanho
print(linguagens)