"""
SCRIPT DE UN GENERADOR DE CONTRASEÑAS
"""
# @author fide.dev

# Importamos random y string para una seleccion aleatoria de caractéres
import random
import string

def new_password(n):
    # Creamos una lista de posibles caractéres para la contraseña
    characters = list(string.ascii_letters + string.digits + string.punctuation)

    # Creamos otra lista con n caractéres seleccionados aleatoriamente
    password = [random.choice(characters) for i in range(n)]

    # Regresamos los caractéres de la lista unidos en un string
    return "".join(password)

# Si es el script principal ejecuta una prueba
if __name__ == '__main__':
    # Deberá seleccionar un rango entre 6 y 18 caractéres
    n = 0
    while n not in range(6, 19):
        try:
            n = int(input("Number of characters for the password (6-18): "))
        except Exception as e:
            print("Enter a valid number...")

    new_pass = new_password(n)
    print(new_pass)
