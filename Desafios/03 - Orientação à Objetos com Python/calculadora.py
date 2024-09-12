class Calculadora:
  def __init__(self, n1, n2):
    self.n1 = n1
    self.n2 = n2
  
  def soma(self):
    return self.n1 + self.n2

num1 = int(input('Digite o valor do primeiro número: '))
num2 = int(input('Digite o valor do segundo número: '))

calc = Calculadora(num1, num2)

resultado = calc.soma()
print(f'A soma de {num1} e {num2} é {resultado}')
