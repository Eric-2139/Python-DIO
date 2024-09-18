# Para se abrir arquivos no Python usamos a função open(), para fecha-los usamos o close()

# Modos de se abir um arquivo: leitura('r'), gravação('w') e anexar('a')

# Maneiras de ler um arquivo: 'read()' -> lê todo o arquivo de uma vez, 'readline()' -> lê uma linha por vez, 'readlines()' -> retorna uma lista onde cada elemento é uma linha de arquivo

arquivo = open(r'C:\Users\Erike\Documents\Digital Innovation One\Python\Python-DIO\06 - Manipulação de Arquivos\lorem.txt', 'r')

print(arquivo.read())
print(arquivo.readline())
print(arquivo.readlines())

# while len(linha := arquivo.readline()):
#     print(linha)

# for a in arquivo.readlines():
#     print(a)

arquivo.close()