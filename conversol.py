menu = '''
Bienvenido al conversor de moneda 💰

1 - Pesos Dominicanos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opción:  '''

opcion = int(input(menu))

if opcion == 1:
    pesos = input('Cuanto pesos dominicano tienes?: ')
    pesos = float(pesos)
    valor_dolar= 59.36
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print( 'Tienes $ ' + dolares + ' dolares') 
elif opcion == 2:
    pesos = input('Cuanto pesos argentino tienes?: ')
    pesos = float(pesos)
    valor_dolar= 65
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print( 'Tienes $ ' + dolares + ' dolares')
elif opcion == 3:
    pesos = input('Cuanto pesos mexicano tienes?: ')
    pesos = float(pesos)
    valor_dolar= 24
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print( 'Tienes $ ' + dolares + ' dolares')
else:
    print('ingresa una opcion correcta por favor ')


