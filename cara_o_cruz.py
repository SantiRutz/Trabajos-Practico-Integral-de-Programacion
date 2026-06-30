import random

def cara_o_cruz():
    print("=== CARA O CRUZ ===")

    eleccion = input("Elige cara o cruz: ").lower()

    resultado = random.choice(["cara", "cruz"])

    print("Salió:", resultado)

    if eleccion == resultado:
        print("¡Ganaste!")
    else:
        print("Perdiste.")