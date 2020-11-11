
def promedio(temps):
    suma_temp = 0

    for temp in temps:
        suma_temp += float(temp)
    return suma_temp / len(temps)


if __name__ == '__main__':
    temps = [25, 30, 35, 40, 45]

    avg = promedio(temps)

    print('La temperatura promedio es: {}'.format(avg))