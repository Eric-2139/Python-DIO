nome = 'eRiC'
print(nome.upper())
print(nome.lower())
print(nome.title())

texto = '  I am the bone of my sword      '
print(texto + '.')
print(texto.strip() + '.')
print(texto.rstrip() + '.')
print(texto.lstrip() + '.')

menu = 'Lobo Branco'
print(f'####{menu}####')
print(menu.center(19))
print(menu.center(19, '#'))
print('-'.join(menu))