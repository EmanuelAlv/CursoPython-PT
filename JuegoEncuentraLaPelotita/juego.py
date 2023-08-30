from random import shuffle  # Importa la función shuffle del módulo random

lista = ['','0','']  # Crea una lista con tres elementos: dos vacíos y uno con '0'
listaMezclada = ''    # Inicializa una variable para almacenar la lista mezclada
respuesta = 0         # Inicializa una variable para almacenar la respuesta del jugador

def revolver_lista(lista):
    shuffle(lista)     # Mezcla aleatoriamente los elementos de la lista
    return lista       # Devuelve la lista mezclada

def eleccionDeJugador():
    eleccion = ''
    while eleccion not in ['0','1','2']:
        eleccion = input("En qué vaso está la pelota? 0, 1 o 2 \n")  # Pide al jugador que elija un vaso
    return int(eleccion)  # Devuelve la elección del jugador convertida a entero

def verificadorEleccion(lista, eleccion):
    if lista[eleccion] == '0':  # Si el elemento en la posición elegida es '0'
        print("Adivinaste, has ganado")
    else:
        print("La bola no está aquí")
        print(lista)  # Muestra la lista para demostrar dónde estaba la bola

# Flujo del programa
listaMezclada = revolver_lista(lista)  # Mezcla la lista utilizando la función definida
respuesta = eleccionDeJugador()       # Pide al jugador que elija un vaso
verificadorEleccion(listaMezclada, respuesta)  # Verifica si la elección del jugador es correcta



