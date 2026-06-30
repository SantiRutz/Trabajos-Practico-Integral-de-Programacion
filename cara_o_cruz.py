# JUEGO 4: CARA O CRUZ
import random

def cara_o_cruz():
    """
    Juego de Cara o Cruz.
    El jugador elige 'cara' o 'cruz' y se lanza una moneda virtual.
    Se acumulan puntos por acierto (10 puntos), se sigue la racha y se guarda la mejor.
    Permite terminar la partida con '0' y al finalizar pregunta si jugar otra, volver al menú o salir.
    """
    print("\n" + "═" * 50)
    print("║" + " BIENVENIDO A CARA O CRUZ ".center(48) + "║")
    print("╚" + "═" * 48 + "╝\n")

    try:
        # Variables para el registro global de partidas.
        puntos_totales = 0
        partidas_ganadas = 0
        partidas_perdidas = 0
        mejor_racha_general = 0

        # Bucle externo: cada iteración es una partida completa.
        while True:
            # Reinicio de variables para la nueva partida.
            puntos = 0
            racha = 0
            mejor_racha = 0
            ronda = 1

            print("\n" + "─" * 50)
            print(f"🎮 Nueva partida | ✅ Ganadas: {partidas_ganadas} | ❌ Perdidas: {partidas_perdidas}")
            print("─" * 50)

            partida_activa = True
            # Bucle interno: rondas de la partida.
            while partida_activa:
                try:
                    print(f"\n🔹 Ronda {ronda} | 💰 Puntos: {puntos} | 🔥 Racha: {racha} | ✨ Mejor: {mejor_racha}")
                    eleccion = input("   Elige cara, cruz o 0 para terminar: ").lower().strip()

                    if not eleccion:
                        print("❌ Por favor ingresa algo.\n")
                        continue

                    if eleccion == "0":
                        # El jugador decide terminar la partida.
                        print("\n" + "═" * 50)
                        print(f"🛑 Partida terminada | Puntos: {puntos} | Mejor racha: {mejor_racha}")
                        print("═" * 50)
                        # Actualiza estadísticas globales.
                        if puntos > 0:
                            partidas_ganadas += 1
                            puntos_totales += puntos
                            mejor_racha_general = max(mejor_racha_general, mejor_racha)
                        else:
                            partidas_perdidas += 1
                        partida_activa = False
                        break

                    if eleccion not in ['cara', 'cruz']:
                        raise ValueError(f"Entrada inválida '{eleccion}'. Usa 'cara', 'cruz' o '0'.")

                    # Lanzamiento de la moneda.
                    resultado = random.choice(['cara', 'cruz'])
                    print(f"🪙 Resultado: {resultado.upper()}")

                    if eleccion == resultado:
                        # Acierto: suma puntos y aumenta racha.
                        puntos += 10
                        racha += 1
                        mejor_racha = max(mejor_racha, racha)
                        print(f"✅ ¡Acertaste! +10 puntos | Racha actual: {racha}\n")
                    else:
                        # Fallo: resetea racha y pregunta si continuar.
                        print(f"❌ Fallaste. Esperabas '{eleccion}' pero salió '{resultado}'.")
                        print(f"🔥 Racha perdida: {racha}")
                        racha = 0

                        continuar = input("   ¿Continuar? (s/n): ").lower().strip()
                        if continuar != 's':
                            # Termina la partida.
                            print("\n" + "═" * 50)
                            print(f"🛑 Partida terminada | Puntos: {puntos} | Mejor racha: {mejor_racha}")
                            print("═" * 50)
                            if puntos > 0:
                                partidas_ganadas += 1
                                puntos_totales += puntos
                                mejor_racha_general = max(mejor_racha_general, mejor_racha)
                            else:
                                partidas_perdidas += 1
                            partida_activa = False
                            break
                        print()

                    ronda += 1

                except ValueError as e:
                    print(f"❌ Error: {str(e)}\n")
                except EOFError:
                    print("\n❌ Error: fin del archivo.")
                    return "salir"
                except Exception as e:
                    print(f"❌ Error inesperado: {type(e)._name_}: {str(e)}\n")

            # ---- Fin de la partida ----
            # Pregunta si quiere jugar otra partida.
            while True:
                repetir = input("\n¿Quieres jugar otra partida? (s/n): ").strip().lower()
                if repetir in ['s', 'n']:
                    break
                print("Responde 's' o 'n'.")
            if repetir == 's':
                continue  # Reinicia el bucle externo (nueva partida).

            # Si no, pregunta si volver al menú principal.
            while True:
                volver = input("¿Volver al menú principal? (s/n): ").strip().lower()
                if volver in ['s', 'n']:
                    break
                print("Responde 's' o 'n'.")
            if volver == 's':
                return "menu"
            else:
                # Muestra el resumen final de todas las partidas jugadas en esta sesión.
                total = partidas_ganadas + partidas_perdidas
                tasa = (partidas_ganadas / total * 100) if total > 0 else 0
                print("\n" + "═" * 50)
                print("🏆 RESUMEN FINAL")
                print("═" * 50)
                print(f"   ✅ Ganadas      : {partidas_ganadas}")
                print(f"   ❌ Perdidas     : {partidas_perdidas}")
                print(f"   💰 Puntos total : {puntos_totales}")
                print(f"   ✨ Mejor racha  : {mejor_racha_general}")
                print(f"   📈 Tasa éxito   : {tasa:.1f}%")
                print("\n¡Gracias por jugar!")
                print("═" * 50)
                return "salir"

    except KeyboardInterrupt:
        print("\n\n⛔ Juego interrumpido.")
        return "menu"
    except Exception as e:
        print(f"\n\n❌ Error crítico: {type(e)._name_}: {str(e)}")
        return "salir"