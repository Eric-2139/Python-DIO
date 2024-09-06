def salvar_carro(marca, modelo, ano, placa):
    print(f'Carro inserido com sucesso: {marca}/{modelo}/{ano}/{placa}')

salvar_carro('Aston Martin', 'Vulcan', 2005, 'AEIOU')
salvar_carro(marca='Ferrari', modelo='F8', ano=1998, placa='Ayrton')
salvar_carro(**{'marca':'Uno', 'modelo': 'Turbo com escada', 'ano': 1999, 'placa': 'XYZ-6696'})