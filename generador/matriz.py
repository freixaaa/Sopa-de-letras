import random
import string

"""
documentación: crea una matriz cuadrada de tamaño n rellena con letras aleatorias.
"""
def crear_matriz(tamano):
    return [[random.choice(string.ascii_lowercase) for _ in range(tamano)] for _ in range(tamano)]

"""
documentación: inserta una palabra de forma horizontal en una fila aleatoria.
"""
def insertar_palabra_horizontal(matriz, palabra):
    tam = len(matriz)
    palabra = palabra.lower()
    
    if len(palabra) > tam:
        return []

    fila = random.randint(0, tam - 1)
    col_inicio = random.randint(0, tam - len(palabra))
    posiciones = []

    for i, letra in enumerate(palabra):
        matriz[fila][col_inicio + i] = letra
        posiciones.append((fila, col_inicio + i))

    return posiciones

"""
documentación: coordina la creación de la matriz y la inserción de las palabras.
"""
def generar_sopa(palabras, tam=15):
    matriz = crear_matriz(tam)
    posiciones_palabras = []

    for palabra in palabras:
        posiciones = insertar_palabra_horizontal(matriz, palabra)
        posiciones_palabras.extend(posiciones)

    return matriz, posiciones_palabras
