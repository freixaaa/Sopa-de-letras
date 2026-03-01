import random
import string

# ==============================
# FUNCIONES PRINCIPALES
# ==============================

def crear_matriz(tamano):
    """
    Crea una matriz cuadrada llena de letras aleatorias.
    """
    return [[random.choice(string.ascii_uppercase) for _ in range(tamano)] for _ in range(tamano)]


def insertar_palabra_horizontal(matriz, palabra):
    """
    Inserta una palabra horizontalmente en una fila aleatoria.
    Retorna las posiciones ocupadas por la palabra.
    """
    tam = len(matriz)
    palabra = palabra.upper()

    fila = random.randint(0, tam - 1)
    col_inicio = random.randint(0, tam - len(palabra))

    posiciones = []

    for i, letra in enumerate(palabra):
        matriz[fila][col_inicio + i] = letra
        posiciones.append((fila, col_inicio + i))

    return posiciones


def generar_sopa(palabras, tam=15):
    """
    Genera la sopa de letras e inserta las palabras.
    Retorna la matriz y las posiciones de las palabras.
    """
    matriz = crear_matriz(tam)
    posiciones_palabras = []

    for palabra in palabras:
        posiciones = insertar_palabra_horizontal(matriz, palabra)
        posiciones_palabras.extend(posiciones)

    return matriz, posiciones_palabras


def imprimir_sopa(matriz):
    """
    Imprime la sopa de letras normal.
    """
    print("\n--- SOPA DE LETRAS ---\n")
    for fila in matriz:
        print(" ".join(fila))
    print()


def imprimir_sopa_resuelta(matriz, posiciones):
    """
    Imprime la sopa resaltando las palabras encontradas en color rojo.
    """
    print("\n--- SOPA RESUELTA ---\n")

    for i, fila in enumerate(matriz):
        for j, letra in enumerate(fila):
            if (i, j) in posiciones:
                # Código ANSI para color rojo
                print(f"\033[91m{letra}\033[0m", end=" ")
            else:
                print(letra, end=" ")
        print()
    print()


def main():
    palabras = []

    print("===== GENERADOR DE SOPA DE LETRAS =====")
    print("Puede ingresar hasta 15 palabras.\n")

    # Ingreso de palabras
    while len(palabras) < 15:
        palabra = input("Ingrese una palabra (o escriba 'fin' para terminar): ").strip()

        if palabra.lower() == "fin":
            break

        if not palabra.isalpha():
            print("Solo se permiten letras.\n")
            continue

        palabras.append(palabra.upper())
        print(f"Palabra agregada ({len(palabras)}/15)\n")

    if len(palabras) == 0:
        print("No ingresó palabras. Saliendo...")
        return

    # Generar sopa
    matriz, posiciones = generar_sopa(palabras)

    # Menú
    while True:
        print("1. Mostrar sopa")
        print("2. Resolver sopa")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            imprimir_sopa(matriz)
        elif opcion == "2":
            imprimir_sopa_resuelta(matriz, posiciones)
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.\n")


# Ejecutar
if __name__ == "__main__":
    main().
