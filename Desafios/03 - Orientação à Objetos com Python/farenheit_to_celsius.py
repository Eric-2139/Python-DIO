class ConversorTemperatura:
    def __init__(self, celsius):
        self.celsius = celsius

    def celsius_para_fahrenheit(self):
        self.fahrenheit = (self.celsius * 9/5) + 32
        return self.fahrenheit

celsius = float(input('Digite o valor a ser convertido: '))

conversor = ConversorTemperatura(celsius)

fahrenheit = conversor.celsius_para_fahrenheit()
print(f'{celsius}⁰C é igual à {fahrenheit}⁰F')