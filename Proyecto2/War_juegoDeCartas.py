import random

# Variables globales
cartasValores = {'Dos':2, 'Tres':3, 'Cuatro':4, 'Cinco':5, 'Seis':6, 'Siete':7, 'Ocho':8, 'Nueve':9, 'Diez':10, 'Jota':10, 'Reina':10, 'Rey':10, 'As':11}
palos = ('corazones', 'diamantes', 'picas', 'tréboles')
valores = ('As', 'Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis', 'Siete', 'Ocho', 'Nueve', 'Diez', 'Jota', 'Reina', 'Rey')
jugando = True

#Clase de la carta
class Carta():

    def __init__(self, palos, valores): #clase contructora
        self.palos = palos
        self.valor = valores
        # self.value = cartasValores[valores]

    def __str__(self): #Metodo string para devolver el valor de la carta y el palo
        return self.valor + ' de ' + self.palos
    
#Clase para el Mazo de cartas 
class Mazo():
     def __init__(self):
         self.todas_las_cartas = [] #Empiezo con una lista vacia
         for palo in palos: #Para cada unos de los palos
             for valor in valores: #Y para cada uno de los valores de cartas 
                 #creo el objeto carta
                 carta_creada = Carta(palo, valor)
                 self.todas_las_cartas.append(carta_creada) #a'ado la carta creada a la lista todas_las_cartas

     def __str__(self):
         mazo_armado = ''
         for carta in self.todas_las_cartas:
             mazo_armado += '\n' + carta.__str__() # al string de mazo armado le concateno un salto de linea y el metdo string de carta para que anada el nombre de la carta y su palo
         return "El mazo tiene: "+ mazo_armado

     def barajearMazo(self):
         random.shuffle(self.todas_las_cartas)
        
     def sacarCarta(self):
         return self.todas_las_cartas.pop()

class Mano:
    def __init__(self):
        self.cartas = [] #Inicio con un alista vacia como en la clase de mazo
        self.valor = 0 # Inicio con valor cero 
        self.ases = 0 #agrego un atributo para mantener los ases a la vista
    def add_carta (self, carta):
        #la carta que se pasara a este metodo sera de la clase Mazo.sacarCarta
        self.cartas.append(carta) #Agregamos una nueva cartas a nuestra mano
        self.valor += cartasValores[carta.valor]  #Suamos el valor de la nueva carta

        #trakeo de los ases
        if carta.valor == 'As':
            self.ases += 1

    def ajuste_para_as(self):
        #Minetras valor sea menor a 21 y contenga un AS
        #Cambia el as a 1 en lugar del valor 11 por defecto
        while self.valor <= 21 and self.ases > 0:
            self.valor -= 10
            self.ases -= 1

class Fichas:
    def __init__(self):
        self.total = 100 #Esto despues lo puede dejar como un input para el jugardor 
        self.apuesta = 0

    def apuestaGanada(self):
        self.total += self.apuesta
    
    def apuestaPerdida(self):
        self.total -= self.apuesta

def tomar_apuesta(fichas):
    while True:
        try:
            fichas.apuesta = int(input('Cuantas fichas desea apostar? '))
        except:
            print('Perdona, por favor ingresa un numero')
        else:
            if fichas.apuesta > fichas.total:
                print('Perdona, no tienes suficientes fichas. Tienes {}'.format(fichas.total))
            else:
                break

def tomar_carta(mazo, mano):
    carta = mazo.sacarCarta()
    mano.add_carta(carta)
    mano.ajuste_para_as()

def tomar_o_permanecer(mazo, mano):
    global jugando
    while jugando:
        x = input('Desea tomar otra carta o permanecer? Ingresa "t" o "p": ')

        if x[0].lower() =='t':
            tomar_carta(mazo,mano)
        elif x[0].lower() =='p':
            print('El jugador permanece, es turno del repartidor')
            jugando = False
        else:
            print('Por favor ingresa "t" o "p" solamente')
            continue
        break

def mostrar_algo(jugador, repartidor):
    #Mostrar solamente una carta de las cartes del repartidor
    print("\n La mano del repartidor es: ")
    print("La primera carta esta oculta!")
    print(repartidor.cartas[1])
    #Mostrar todas las cartas del jugador que tiene en su mano
    print("\n La mano del jugador es: ")
    for carta in jugador.cartas:
        print(carta)

def mostrar_todo(jugador, repartidor):
    #mostrar todas las cartas del repartidor
    print("\n La mano del repartidor es: ")
    for carta in repartidor.cartas:
        print(carta)
    #Calcular y mostrar el valor de la mano del repartidor
    print(f'El valor de la mano del repartidor es: {repartidor.valor}')
    #Mostrar todas las cartas del jugador
    print("\n La mano del jugador es: ")
    for carta in jugador.cartas:
        print(carta)

    print(f'El valor de la mano del jugador es: {jugador.valor}')

def juagador_pierde(jugador, repartidor, fichas):
    print('Jugador eliminado')
    fichas.apuestaPerdida()
def juagador_gana(jugador, repartidor, fichas):
    print('Jugador ha ganado!')
    fichas.apuestaGanada()
def repartidor_pierde(jugador, repartidor, fichas):
    print('Jugador ha ganado! el repartidor ha perdido')
    fichas.apuestaGanada()
def repartidor_gana(jugador, repartidor, fichas):
    print('Repartidor haganado jugador eliminado')
    fichas.apuestaPerdida()
def push(jugador, repartidor):
    print('El jugador y el repartidor han quedado en empate!')

# Logica del juego 
print('¡BIENVENIDO AL BLACKJACK!')
mazo = Mazo() #Creo un nuevo mazo
mazo.barajearMazo() #Mezclo la baraja de cartas

mano_jugador = Mano() # Creo la mano del jugador
mano_jugador.add_carta(mazo.sacarCarta()) #Anado una carta a la mano del jugdr dos veces
mano_jugador.add_carta(mazo.sacarCarta())

mano_repartidor = Mano() # Creo la mano del repartidor
mano_repartidor.add_carta(mazo.sacarCarta())#Anado una carta a la mano del repartidor dos veces
mano_repartidor.add_carta(mazo.sacarCarta())

#Fichas del jugardor
fichas_jugador = Fichas()

#Mostras al jugador su apuesta
tomar_apuesta(fichas_jugador)

#Mostrar cartas
mostrar_algo(mano_jugador, mano_repartidor)

while jugando: #llamar esta variable desde la funcion tomar_o_permanecer
    # Mostrar al jugardor opciones de tomar_o_permanecer
    tomar_o_permanecer(mazo, mano_jugador)
    #Mostrar cartas pero manteniendo las del repartidor ocultas
    mostrar_algo(mano_jugador, mano_repartidor)
    #Si la mano del jugador pasa los 21 correr la funcion de jugador_pierde y romper el loop
    if mano_jugador.valor > 21:
        juagador_pierde(mano_jugador, mano_repartidor, fichas_jugador)
        break

    #Si el jugador no ha sido elimiado, se jugara la mano del reaprtidor hasta alcanzar 17
    if mano_jugador.valor <= 21:
        while mano_repartidor.valor < mano_jugador.valor:
            tomar_carta(mazo, mano_jugador)

        #mostrar todas las cartas del reaprtidor
        mostrar_todo(mano_jugador, mano_repartidor)

        # Correr los distintos escenarios donde el jugador puede ganar
        if mano_repartidor.valor > 21:
            repartidor_pierde(mano_jugador, mano_repartidor, fichas_jugador)
        elif mano_repartidor.valor > mano_jugador.valor:
            repartidor_gana(mano_jugador, mano_repartidor, fichas_jugador)
        elif mano_repartidor.valor < mano_jugador.valor:
            juagador_gana(mano_jugador, mano_repartidor, fichas_jugador)
        else:
            push(mano_jugador, mano_repartidor)

    # Mostrar al jugador 
    print('El total de las ficjas del jugador es de: {}'.format(fichas_jugador.total))

    nuevo_juego = input('Quire jugar de nuevo? S/N')

    if nuevo_juego[0].lower() == 's':
        jugando = True
        continue
    else:
        print('Gracias por jugar ')
        break



# class Jugador():
#     def __init__(self, nombre):
#         self.nombre = nombre
#         self.todas_las_cartas = []
    
#     def quitarCarta(self):
#         return self.todas_las_cartas.pop(0) #Se hace el pop 0 para quitar la carta del principio de la lista (Mazo)

#     def agregarCartas(self, cartasNuevas):
#         if type(cartasNuevas) == type([]): # en caso de que se vallan a agrgar varias cartas
#             self.todas_las_cartas.extend(cartasNuevas)
#         else:
#             self.todas_las_cartas.append(cartasNuevas) #En caso de agregar solo una carta 
#         return self.todas_las_cartas

#     def __str__(self):
#         return 'Al Jugador {} le quedan {} cartas'.format(self.nombre, len(self.todas_las_cartas))
        
        
        
   

# nuevoMazo = Mazo()
# nuevoMazo.barajearMazo()
# #juegador de prueba
# print('------------------Pruebas sacar carta de mazo y asignar a mano de jugador--------------------')
# juegador_prueba = Mano()
# sacar_carta = nuevoMazo.sacarCarta()
# print(sacar_carta)
# juegador_prueba.add_carta(sacar_carta)
# print(juegador_prueba.valor)
# print('------------------Pruebas sacar carta de mazo y asignar a mano de jugador--------------------')

# print(len(nuevoMazo.todas_las_cartas))
# cartas = nuevoMazo.sacarCarta()
# print(cartas)
# print(len(nuevoMazo.todas_las_cartas))
# print(nuevoMazo)
# # for carta in cartas:
# #     print(carta)
# print('-------------------------------------------------')
# nuevoJugador = Jugador("Emanuel")
# print(nuevoJugador)
# nuevoJugador.agregarCartas(nuevoMazo.todas_las_cartas)
# print(nuevoJugador)
# print(nuevoJugador.quitarCarta())
# print(nuevoJugador.quitarCarta())
# print(nuevoJugador)
