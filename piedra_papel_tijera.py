# JUEGO 1: PIEDRA, PAPEL O TIJERA (Versión final)
import random

# Códigos ANSI para colorear la salida en la terminal.
VERDE = '\033[32m'
ROJO = '\033[31m'
AMARILLO = '\033[33m'
CYAN = '\033[36m'
RESET = '\033[0m'


def mostrar_menu():
    """Muestra el menú principal del juego."""
    print(f"\n{CYAN}=== Piedra, Papel o Tijera ==={RESET}")
    print("1. Jugar una serie")
    print("2. Salir")


def pedir_numero(mensaje):
    """Solicita un número entero positivo y valida la entrada."""
    while True:
        try:
            valor = int(input(mensaje).strip())
            if valor <= 0:
                print(f"{ROJO}Debes ingresar un número mayor que 0.{RESET}")
                continue
            return valor
        except ValueError:
            print(f"{ROJO}Entrada inválida. Escribe un número entero.{RESET}")
        except KeyboardInterrupt:
            raise


def jugar_serie():
    """
    Juega una serie completa contra la computadora.
    Permite configurar el número de juegos y los puntos por victoria.
    Los empates no cuentan como juego completado.
    Al finalizar muestra el resultado global y permite repetir la serie o volver al menú principal.
    """
    opciones = ['piedra', 'papel', 'tijera']

    print(f"\n{CYAN}=== Configuración de la serie ==={RESET}")
    num_juegos = pedir_numero("¿Cuántos juegos quieres jugar?: ")
    puntos_por_ganar = pedir_numero("¿Cuántos puntos se otorgan por cada victoria?: ")

    puntos_usuario = 0
    puntos_computadora = 0
    juegos_completados = 0

    print(f"\nVamos a jugar {num_juegos} juegos. Cada victoria vale {puntos_por_ganar} puntos.\n")

    while juegos_completados < num_juegos:
        try:
            computadora = random.choice(opciones)
            usuario = input("Elige piedra, papel o tijera: ").strip().lower()
        except KeyboardInterrupt:
            print(f"\n{AMARILLO}Interrupción detectada. Volviendo al menú principal.{RESET}")
            return "menu"

        if usuario not in opciones:
            print(f"{ROJO}Entrada no válida. Usa 'piedra', 'papel' o 'tijera'. Intenta de nuevo.{RESET}")
            continue

        print(f"\n{CYAN}Tú elegiste:{RESET} {usuario}")
        print(f"{CYAN}Computadora eligió:{RESET} {computadora}")

        if usuario == computadora:
            print(f"{AMARILLO}¡Empate! Este juego no cuenta.{RESET}\n")
            continue
        elif (usuario == 'piedra' and computadora == 'tijera') or \
             (usuario == 'papel' and computadora == 'piedra') or \
             (usuario == 'tijera' and computadora == 'papel'):
            puntos_usuario += puntos_por_ganar
            juegos_completados += 1
            print(f"{VERDE}¡Ganaste! + {puntos_por_ganar} puntos para ti.{RESET}")
        else:
            puntos_computadora += puntos_por_ganar
            juegos_completados += 1
            print(f"{ROJO}¡Perdiste! + {puntos_por_ganar} puntos para la computadora.{RESET}")

        print(f"\n{CYAN}Puntaje actual:{RESET} Tú {puntos_usuario} - Computadora {puntos_computadora}")
        print(f"{CYAN}Juegos completados:{RESET} {juegos_completados} / {num_juegos}\n")

    print(f"{CYAN}===== Resultado final ====={RESET}")
    print(f"{CYAN}Puntos totales:{RESET} Tú {puntos_usuario} - Computadora {puntos_computadora}")
    if puntos_usuario > puntos_computadora:
        print(f"{VERDE}¡Felicidades! Ganaste el partido general.{RESET}")
    elif puntos_usuario < puntos_computadora:
        print(f"{ROJO}La computadora ganó el partido general.{RESET}")
    else:
        print(f"{AMARILLO}El partido general terminó en empate.{RESET}")

    while True:
        try:
            accion = input("\n¿Quieres jugar otra serie? (s) Sí | (m) Menú principal | (n) Salir: ").strip().lower()
        except KeyboardInterrupt:
            print(f"\n{AMARILLO}Interrupción detectada. Volviendo al menú principal.{RESET}")
            return "menu"

        if accion in ('s', 'si', 'sí', 'y'):
            return "serie"
        elif accion in ('m', 'menu', 'principal'):
            return "menu"
        elif accion in ('n', 'no', 'q'):
            return "salir"
        else:
            print(f"{ROJO}Opción no válida. Intenta de nuevo.{RESET}")


def main():
    """Controla el menú principal y el flujo del juego."""
    while True:
        try:
            mostrar_menu()
            opcion = input("Elige una opción: ").strip()
        except KeyboardInterrupt:
            print(f"\n{AMARILLO}Interrupción detectada. Volviendo al menú principal.{RESET}")
            continue

        if opcion == '1':
            while True:
                resultado = jugar_serie()
                if resultado == 'serie':
                    continue
                if resultado == 'menu':
                    break
                if resultado == 'salir':
                    print(f"\n{CYAN}Gracias por jugar.{RESET}")
                    return
        elif opcion == '2':
            print(f"\n{CYAN}Gracias por jugar.{RESET}")
            break
        else:
            print(f"{ROJO}Opción no válida.{RESET}")


if __name__ == "__main__":
    main()