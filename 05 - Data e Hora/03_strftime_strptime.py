from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = '2024-09-15 10:20'
mascara_ptbr = '%d/%m/%Y %H:%M %a'

print(data_hora_atual.strftime(mascara_ptbr))

mascara_en = '%Y-%m-%d %H:%M'
data_convertida = datetime.strptime(data_hora_str, mascara_en)

print(data_convertida)
print(type(data_convertida))