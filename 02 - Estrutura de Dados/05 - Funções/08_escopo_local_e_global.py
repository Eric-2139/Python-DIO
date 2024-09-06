# Python trabalha com escopo local e global, dentro do bloco da função o escopo é local, portanto alterações ali feitas em objetos imutáveis serão perdidas quando o método terminar de ser executado. Para usar objetos globais, utilizamos a palavra chave global, que informa ao interpretador que a variável a ser usada é do escopo global. ESSA NÃO É UMA BOA PRÁTICA E DEVE SER EVITADA

salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

print(salario_bonus(500))