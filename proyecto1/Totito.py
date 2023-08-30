import os
import sys
tableroGuia = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
tablero = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def imprimir_tablero(tablero, tableroGuia):
    print('\n\n      == TO TI TO ==\n')
    print(" {} | {} | {} \t {} | {} | {}".format(tablero[0], tablero[1], tablero[2], tableroGuia[0], tableroGuia[1], tableroGuia[2]))
    print("---+---+--- \t---+---+---")
    print(" {} | {} | {} \t {} | {} | {}".format(tablero[3], tablero[4], tablero[5], tableroGuia[3], tableroGuia[4], tableroGuia[5]))
    print("---+---+--- \t---+---+---")
    print(" {} | {} | {} \t {} | {} | {}\n\n".format(tablero[6], tablero[7], tablero[8], tableroGuia[6], tableroGuia[7], tableroGuia[8]))

def inputUsuario():
    opciones = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    eleccion = ' '
    rango = False
    while eleccion.isdigit() == False or rango == False:
        eleccion = input('Ingresa un valor entre [1-9]: ')
        if eleccion.isdigit() == False:
            print('Por favor ingresa solamente digitos')
        if eleccion.isdigit() == True:
            if int(eleccion) in opciones:
                rango = True
            else:
                print('Eleccion fuera de rango, ingresa digitos entre [1-9]')
                rango = False
    return int(eleccion)

def remplazoCaracter(posicion, caracter):
    posicion = posicion -1
    tablero[posicion] = caracter.upper()
        
    return tablero

def seguirJugando():
    respuesta = ' '
    while respuesta not in ['S','s','N','n']:
        respuesta = input('Deseas seguir jugando? [S,N]')
    
        if respuesta not in ['S','s','N','n']:
            print('No entiendo, ingresa [S,N]')

    if respuesta in ['S','s']:
        # tablero = [elemento.replace(elemento, " ") for elemento in tablero] AQUI ME QUEDE!!!!!!!!
        borrarPantalla()

    else:
        sys.exit()


def jugador():
    jugadores = ['Uno', 'Dos']
    eleccion = ' '
    opciones = ['x','X','o','O']
    while eleccion not in opciones:
        eleccion = input('Jugador 1 que signo escoges? [X o O]')
        jugador1 = eleccion.upper()

        if eleccion not in opciones:
            print('Por favor escoge una opcion valida [X o O]')

    if jugador1 == 'X':
        jugador2 = 'O'
    else:
        jugador2 = 'X'
    # print('Jugador uno eligio {} y jugador dos {}'.format(jugadores[0], jugadores[1]))
    # print(jugador1, jugador2)
    return (jugador1 ,jugador2)

def verificar_ganador(tablero, jugador):
    verificador = False
    combinaciones_ganadoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
        [0, 4, 8], [2, 4, 6]              # Diagonales
    ]

    for combinacion in combinaciones_ganadoras:
        if all(tablero[i] == jugador for i in combinacion):
            verificador = True
        
    if verificador:
        print("¡El jugador {} ha ganado!".format(jugador))
        seguirJugando()
    else:
        pass

        
def empate(tablero):
    if ' ' not in tablero:
        print('Es un empate')
        seguirJugando()
 
def borrarPantalla(): 
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def juego():
    continuarJugando = True
    jugador1 , jugador2 = jugador()
    print(jugador1, jugador2)

    while continuarJugando:

        borrarPantalla()
        print ("Turno del jugador uno '{}'".format(jugador1))
        imprimir_tablero(tablero,tableroGuia)
        remplazoCaracter(inputUsuario(), jugador1)
        imprimir_tablero(tablero, tableroGuia)
        empate(tablero)
        verificar_ganador(tablero, jugador1)

        borrarPantalla()
        print ("Turno del jugador uno '{}'".format(jugador2))
        imprimir_tablero(tablero,tableroGuia)
        remplazoCaracter(inputUsuario(), jugador2)
        imprimir_tablero(tablero, tableroGuia)
        empate(tablero)
        verificar_ganador(tablero, jugador2)
    
juego()
# jugador()



# num = '8r'
# print(num.isdigit())
 
