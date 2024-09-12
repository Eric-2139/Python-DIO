def calculadora(operacao):
    def soma(a, b):
        return a + b
    
    def subtracao(a, b):
        return a - b
    
    def multiplicacao(a, b):
        return a * b
    
    def divisao(a, b):
        return a / b
    
    match operacao:
        case '+':
            return soma
        
        case '-':
            return subtracao
        
        case '*':
            return multiplicacao
        
        case '/':
            return divisao
        
print(calculadora('+')(5, 5))
print(calculadora('-')(5, 5))
print(calculadora('*')(5, 5))
print(calculadora('/')(5, 5))

print('')

op = calculadora('+')
print(op(5, 5))

op = calculadora('-')
print(op(5, 5))

op = calculadora('*')
print(op(5, 5))

op = calculadora('/')
print(op(5, 5))