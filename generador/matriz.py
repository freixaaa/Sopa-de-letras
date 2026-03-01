import random
import string

def crear_matriz(tamano):
    # se crea la cuadricula base con letras aleatorias
    return [[random.choice(string.ascii_lowercase) for _ in range(tamano)] for _ in range(tamano)]

def insertar_palabra_horizontal(matriz, palabra):
    # se inserta una palabra de forma horizontal en la matriz
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

def generar_sopa(palabras, tam=15):
    # se coordina la creacion y la integración de la sopa de letras
    matriz = crear_matriz(tam)
    posiciones_palabras = []

    for palabra in palabras:
        posiciones = insertar_palabra_horizontal(matriz, palabra)
        posiciones_palabras.extend(posiciones)

    return matriz, posiciones_palabras
