# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#  positional only|positional or keyword|keyword only

def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro(modelo='Palio', ano=1999, placa='LKM-8956', marca='Fiat', motor='1.0', combustivel='Gasolina')