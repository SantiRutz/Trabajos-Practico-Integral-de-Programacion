# JUEGO 1: PIEDRA, PAPEL O TIJERA (Versión 1)
def jugar_piedra_papel_tijera():
    """
    Juego de Piedra, Papel o Tijera contra la computadora.
    Versión básica: se juega una única ronda.
    """
    import random
    opciones = ['piedra', 'papel', 'tijera']

    # La computadora elige aleatoriamente.
    computadora = random.choice(opciones)
    usuario = input("Elige piedra, papel o tijera: ").strip().lower()

    # Validación de la entrada del usuario.
    if usuario not in opciones:
        print("Entrada no válida. Usa 'piedra', 'papel' o 'tijera'.")
        return

    # Muestra las elecciones.
    print(f"\nTú elegiste: {usuario}")
    print(f"Computadora eligió: {computadora}")

    # Evaluación del resultado.
    if usuario == computadora:
        print("¡Empate!")
    elif (usuario == 'piedra' and computadora == 'tijera') or \
         (usuario == 'papel' and computadora == 'piedra') or \
         (usuario == 'tijera' and computadora == 'papel'):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")