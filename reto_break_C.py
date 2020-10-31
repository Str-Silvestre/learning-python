def run():
    """
    docstring
    """
    vida = 100
    while vida > 0:
        print('Estoy con vida: ' + str(vida))
        vida = vida - 5
        if vida <= 25:
            print('Casi estoy muerto: ' + str(vida))
            break
        

if __name__ == '__main__':
    run()