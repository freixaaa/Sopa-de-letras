from generador.matriz import generar_sopa

def imprimir_sopa(matriz):
    print("\nsopa de letras\n")
    for fila in matriz:
        print(" ".join(fila))
    print()

def imprimir_sopa_resuelta(matriz, posiciones):
    print("\nsopa de letras resuelta\n")
    for i, fila in enumerate(matriz):
        for j, letra in enumerate(fila):
            if (i, j) in posiciones:
                print(f"\033[91m{letra}\033[0m", end=" ")
            else:
                print(letra, end=" ")
        print()
    print()

def main():
    palabras = []

    print("SOPA DE LETRAS")
    print("puede ingresar un máximo de 15 palabras o escribir 'terminar' cuando haya culminado")

    while len(palabras) < 15:
        print(f"\ningrese una palabra ({len(palabras)}/15):")
        palabra = input().strip().lower()

        if palabra == "terminar":
            break

        if not palabra.isalpha():
            print("solo se permiten letras")
            continue

        palabras.append(palabra)

    if len(palabras) == 0:
        print("no ingresó palabras")
        return

    matriz, posiciones = generar_sopa(palabras)

    while True:
        print("\n1. mostrar sopa")
        print("2. resolver sopa")
        print("3. finalizar")
        print("seleccione una opción:")

        opcion = input()

        if opcion == "1":
            imprimir_sopa(matriz)
        elif opcion == "2":
            imprimir_sopa_resuelta(matriz, posiciones)
        elif opcion == "3":
            # el programa finaliza sin mensajes adicionales
            break
        else:
            print("opción inválida")

if __name__ == "__main__":
    main()
