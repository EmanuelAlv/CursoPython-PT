from random import shuffle

lista = ['','0','']
listaMezclada = ''
respuesta = 0

def revolver_lista(lista):
    shuffle(lista)
    return lista

def eleccionDeJugador ():
    eleccion = ''
    while eleccion not in ['0','1','2']:
        eleccion = input ("En que vaso esta la polota? 0, 1 o 2 \n")
    return int(eleccion)

def verificadorEleccion (lista, eleccion):
    if lista[eleccion] == '0':
        print("Adivinaste, has ganado")
    else:
        print("La bola no esta aqui")
        print(lista)

# Flujo del programa
listaMezclada = revolver_lista(lista)
respuesta = eleccionDeJugador()
verificadorEleccion(listaMezclada, respuesta)



