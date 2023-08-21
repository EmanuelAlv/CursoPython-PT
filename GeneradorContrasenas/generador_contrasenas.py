import random
def generar_contrasena():
    mayuscalas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    simbolos = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    caracteres = mayuscalas + minusculas + simbolos + numeros
    contrasena = []

    for i in range(15):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)
    
    contrasena = ''.join(contrasena) # Convierte una lista en un string uniendo cada dato con el caracter puesto entre comillas
    return contrasena

def run():
    contresena = generar_contrasena()
    print('Tu nueva contraseña es: ' + contresena)

if __name__ == '__main__':
    run()