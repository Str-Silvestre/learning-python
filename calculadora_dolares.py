def foregin_exchange_calculator(ammount):
    dolar_to_do_rate = 58.85

    return dolar_to_do_rate * ammount


def run():
    """
    docstring
    """
    print('C A L C U L A D O RA  D E D I V I S A S')
    print('Convierte dolares a pesos Dominicanos.')
    print('')


    ammount = float(input('Ingresa la cantidad en pesos Dominicanos:  '))

    result = foregin_exchange_calculator(ammount)

    print('${} dolares son ${} pesos dominicanos'.format(ammount, result))

if __name__ == '__main__':
    run()