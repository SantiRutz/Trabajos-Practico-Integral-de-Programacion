import random

def paryimpar():
    print("=== JUEGO PAR O IMPAR ===")

    while True:
        numero = random.randint(1, 100)

        respuesta = input("¿Es par o impar? (par/impar, 0 para salir): ").lower()

        if respuesta == "0":
            print("Gracias por jugar.")
            break

        if numero % 2 == 0:
            correcto = "par"
        else:
            correcto = "impar"

        if respuesta == correcto:
            print(f"¡Correcto! El número era {numero}.")
        else:
            print(f"Incorrecto. El número era {numero} ({correcto}).")