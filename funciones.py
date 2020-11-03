""" def imprimir_mensaje(parameter_list):
    print('Mensaje especial: ')
    print('estoy aprendiendo a usar funciones!')


imprimir_mensaje()
imprimir_mensaje() """

def conversacion(opcion):
    print('Hola')
    print('Como estas?')
    print('Elegiste la opción ' + str(opcion) )
    print('Adios')

opcion = int(input('Ekuge una opcion (1, 2, 3:)'))
if opcion == 1:
    conversacion(opcion)
elif opcion == 2:
    conversacion(opcion)
elif opcion == 3:
    conversacion(opcion)
else:
    print('Ingrese una opcion valida')