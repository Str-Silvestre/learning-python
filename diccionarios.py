def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }
    """ print(mi_diccionario['llave2'])
    print(mi_diccionario['llave3']) """

    poblacion_paises = {
        'Republica Dominicana': 10000000,
        'Argentina': 4715151,
        'colombia': 454512011,
    }

    """ for pais in poblacion_paises.keys():
        print(pais) """

    """ for pais in poblacion_paises.values():
        print(pais) """

    for pais, poblacion in poblacion_paises.items():
        print(pais + ' tiene '+ str(poblacion) + ' habitantes')


if __name__ == '__main__':
    run()