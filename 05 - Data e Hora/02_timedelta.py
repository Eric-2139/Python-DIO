from datetime import datetime, timedelta

tipo_carro = input('Digite o tamanho do seu carro(P, M ou G): ').upper()
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == 'P':
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f'Chegada: {data_atual}, Saída estimada: {data_estimada}')
elif tipo_carro == 'M':
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f'Chegada: {data_atual}, Saída estimada: {data_estimada}')
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f'Chegada: {data_atual}, Saída estimada: {data_estimada}')

# Exemplo de como pegar informações separadas
print(datetime.now().time())
print(datetime.now().date())