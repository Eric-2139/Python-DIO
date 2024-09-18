# Context manager: o gerenciamento de contexto permite trabalhar com arquivos de forma segura, garantindo que eles sejam fechados corretamente, mesmo em caso de exceções. Você o usa com a declaração 'with'

from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    with open(ROOT_PATH / 'l2orem.txt', 'r') as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f'Erro ao abrir o arquivo: \n{exc}')

# try:
#     with open(ROOT_PATH / 'arquivo-utf-8.txt', 'w', encoding='utf-8') as arquivo:
#         arquivo.write('Aprendendo a manipular arquivos usando Python')
# except IOError as exc:
#     print(f'Erro ao abrir o arquivo: \n{exc}')

try:
    with open(ROOT_PATH / 'arquivo-utf-8.txt', 'r', encoding='utf-8') as arquivo:
        arquivo.read()
except IOError as exc:
    print(f'Erro ao abrir o arquivo: \n{exc}')
except UnicodeDecodeError as exc:
    print(exc)