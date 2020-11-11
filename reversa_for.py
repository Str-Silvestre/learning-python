def run():
    reversa_letra =[]
    nombre = 'Kelvin'


    for letra in nombre:
        reversa_letra.insert(0, nombre)
    
    reversa_nombre = ''.join(reversa_letra)
    print(reversa_nombre)


if __name__ == '__main__':
    run()