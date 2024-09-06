def verificador_ano_bissexto():
    ano = int(input('Digite um ano para verificar se ele é bisexto: '))
    
    if(ano % 4 == 0 and not ano % 100 == 0 or ano % 400 == 0):
      print('É um ano bisexto')
    else:
      print('Não é um ano bisexto')

verificador_ano_bissexto()