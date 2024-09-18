from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    arquivo = open(ROOT_PATH / 'novo-diretorio' / 'novo.txt', 'r')
except FileNotFoundError as exc:
    print(f'Arquivo não encontrado: \n{exc}')
except IsADirectoryError as exc:
    print(f'Não foi possível abrir o arquivo: \n{exc}')
except PermissionError as exc:
    print(F'Você não tem permissão para abrir esse arquivo/diretorio: \n{exc}')
except IOError as exc:
    print(f'Erro ao abrir o arquivo: \n{exc}')
except Exception as exc:
    print(f'Alguma exceção ocorreu: \n {exc}')

# try:
#     arquivo = open(ROOT_PATH / 'novo-diretorio')
# except PermissionError as exc:
#     print(F'Você não tem permissão para abrir esse arquivo/diretorio: \n{exc}')