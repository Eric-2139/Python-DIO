# CSV: um formato amplamente utilizado para armazenar dados tabulares

import csv
from pathlib import Path

COLUNA_ID = 0
COLUNA_NOME = 1

ROOT_PATH = Path(__file__).parent

try:
    with open(ROOT_PATH / "usarios.csv", "w", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(['id', 'nome'])
        escritor.writerow(['1', 'Maria'])
        escritor.writerow(['2', 'João'])
except IOError as exc:
    print(f'Erro ao criar o arquivo: \n {exc}')

try:
    with open(ROOT_PATH / "usarios.csv", "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        for idx, row in enumerate (leitor):
            if idx == 0:
                continue
            print(f'ID: {row[COLUNA_ID]}')
            print(f"Nome: {row[COLUNA_NOME]}")
except IOError as exc:
    print(f'Erro ao criar o arquivo: \n {exc}')
except IndexError as exc:
    print({exc})
    
try:
    with open(ROOT_PATH / "usarios.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(f'ID: {row['id']}')
            print(f"Nome: {row['nome']}")
except IOError as exc:
    print(f'Erro ao criar o arquivo: \n {exc}')