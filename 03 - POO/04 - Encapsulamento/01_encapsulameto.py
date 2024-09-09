# Encapsulamento: descreve a ideia de agrupar dados e os métodos que manipulam esses dados em uma unidade. Isso impões restrições ao acesso a variáveis e métodos. Em Python não temos palavras reservas para definição de público e privado, então para isso são usadas convenções no nome do recurso

# Variável pública: var
# VAriável privada: _var

class Conta:
    def __init__(self, nmr_agencia, saldo=0):
        self._saldo = saldo

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def mostrar_saldo(self):
        return self._saldo 

conta = Conta('0001', 100)
conta.depositar(100)