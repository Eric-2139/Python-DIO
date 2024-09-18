# Podemos usar 'write()' ou 'writelines()' para escrever em um arquivo

arquivo = open(r'C:\Users\Erike\Documents\Digital Innovation One\Python\Python-DIO\06 - Manipulação de Arquivos\teste.txt', 'w')
arquivo.write('Escrevendo dados em um novo arquivo.')
arquivo.writelines(['\nI\n', 'am\n', 'the\n', 'bone\n', 'of\n', 'my\n', 'sword'])
arquivo.close()