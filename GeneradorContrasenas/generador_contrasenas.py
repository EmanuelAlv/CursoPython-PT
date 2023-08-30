import random  # Importa el módulo random para generar números aleatorios y selecciones aleatorias

def generar_contrasena():
    # Define listas de caracteres posibles para la contraseña
    mayuscalas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    simbolos = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    # Combina las listas de caracteres en una sola lista
    caracteres = mayuscalas + minusculas + simbolos + numeros
    contrasena = []  # Lista para almacenar los caracteres de la contraseña

    # Genera 15 caracteres aleatorios para la contraseña
    for i in range(15):
        caracter_random = random.choice(caracteres)  # Selecciona un carácter aleatorio de la lista de caracteres
        contrasena.append(caracter_random)  # Agrega el carácter aleatorio a la lista de contraseña
    
    contrasena = ''.join(contrasena)  # Convierte la lista de caracteres en una cadena
    return contrasena  # Devuelve la contraseña generada

def run():
    contrasena = generar_contrasena()  # Genera una contraseña llamando a la función
    print('Tu nueva contraseña es: ' + contrasena)  # Imprime la contraseña generada

if __name__ == '__main__':
    run()  # Llama a la función run() si el script se ejecuta directamente