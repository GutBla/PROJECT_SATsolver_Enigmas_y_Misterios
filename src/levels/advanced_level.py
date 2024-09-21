from colorama import init, Fore, Style
from pysat.solvers import Solver
from pysat.formula import CNF

init(autoreset=True)

def print_banner():
    """Imprime el banner principal del juego."""
    banner = r"""
█▄ █ █ █ █ █▀▀ █     ▄▀█ █ █ ▄▀█ █▄ █ ▀█ ▄▀█ █▀▄ █▀█
█ ▀█ █ ▀▄▀ ██▄ █▄▄   █▀█ ▀▄▀ █▀█ █ ▀█ █▄ █▀█ █▄▀ █▄█
    """
    print(Fore.RED + Style.BRIGHT + banner + Style.RESET_ALL)
    print(Fore.RED + "===== Alguien hizo trampa en el Examen =====")

def print_game_intro():
    """Imprime la introducción del juego."""
    intro_message = (
        "El examen ha terminado, pero algo no está bien. Un estudiante ha sido acusado de hacer trampa, y cada uno de los seis sospechosos tiene una versión distinta de los hechos. "
        "El detective debe escuchar cuidadosamente las declaraciones de todos y descubrir quién es el culpable, qué tipo de trampa utilizó y el método que empleó para llevarla a cabo. "
        "Dado que las declaraciones no siempre son veraces, el jugador deberá interpretar las pistas con astucia para resolver el caso."
    )
    print(Style.BRIGHT + intro_message + Style.RESET_ALL)
    print(Fore.RED + "="*80 + Style.RESET_ALL)

def show_clues():
    """Muestra las pistas sobre los sospechosos y las trampas."""
    suspect_clues = [
        "Según las pistas, si Brisa está involucrada, entonces Alondra también lo está. Esto sugiere que podrían haber trabajado juntas en la trampa, ya que sus respuestas eran similares.",
        "Daniel tiene una coartada sólida y no puede ser el responsable; además, dio el examen otro día porque estaba en la biblioteca.",
        "Alan no es culpable; su comportamiento durante el examen fue impecable y no tiene motivos para engañar.",
        "No puede ser Wilmar porque al momento del examen estaba en la enfermería.",
        "Si Andrea es culpable, entonces Brisa también lo es, ya que se encontraron mensajes de texto entre ellas que sugieren colaboración.",
        "Hay un culpable. Solo hay un culpable."
    ]

    trap_clues = [
        "Andrea menciona que no pudo ser con hojas ocultas, antes de ingresar al examen se revisó a todos los estudiantes.",
        "Brisa dice que si el culpable no copió de un compañero, entonces tuvo que usar otro medio de trampa.",
        "Melina dice que el culpable no pudo robar el examen un día antes porque el examen se cambió en la mañana.",
        "Alan dice que si el culpable no copió de un compañero, entonces tuvo que usar un audífono oculto o un celular.",
        "Brisa dice que el culpable debió copiarle a un compañero porque los pupitres estaban muy cerca y no había acceso a otros medios de trampa.",
        "Daniel dice que si alguien robó el examen un día antes, entonces esa persona no fue el culpable, ya que el examen se cambió y no fue útil. Por lo tanto, el culpable debe haber sido quien copió de un compañero.",
        "Wilmar dice que, debido a la dificultad del examen, el culpable debió copiarle a un compañero o usar un celular.",
        "Alan dice que no pudo ser por el celular, ya que en el lugar donde se hizo el examen no había señal ni conexión.",
        "Se hizo trampa de alguna forma. Solo hay opción de trampa que se hizo."
    ]

    print(Fore.YELLOW + Style.BRIGHT + "\nPistas sobre los sospechosos:" + Style.RESET_ALL)
    for clue in suspect_clues:
        print(f"- {clue}")
    print(Fore.RED + "="*80 + Style.RESET_ALL)

    print(Fore.YELLOW + Style.BRIGHT + "\nPistas sobre las trampas:" + Style.RESET_ALL)
    for clue in trap_clues:
        print(f"- {clue}")
    print(Fore.RED + "="*80 + Style.RESET_ALL)

def show_characters_and_traps():
    """Muestra la lista de personajes y tipos de trampa."""
    characters = [
        "Alan",
        "Melina",
        "Andrea",
        "Brisa",
        "Daniel",
        "Wilmar"
    ]

    traps = [
        "Uso el celular (chat GPT)",
        "Tenía hojas ocultas (respuestas, apuntes)",
        "Se robó el examen un día antes",
        "Audífono oculto",
        "Se copió de un compañero/a"
    ]

    print(Fore.BLUE + Style.BRIGHT + "Personajes:" + Style.RESET_ALL)
    for character in characters:
        print(f"- {character}")
    print(Fore.RED + "="*80 + Style.RESET_ALL)

    print(Fore.BLUE + Style.BRIGHT + "\nTrampas:" + Style.RESET_ALL)
    for trap in traps:
        print(f"- {trap}")
    print(Fore.RED + "="*80 + Style.RESET_ALL)

def show_menu():
    """Muestra el menú principal."""
    print(Fore.CYAN + Style.BRIGHT + "1. Ver culpables y trampas" + Style.RESET_ALL)
    print(Fore.GREEN + "2. Ver declaraciones y pistas" + Style.RESET_ALL)
    print(Fore.YELLOW + "3. Ver resolución del caso" + Style.RESET_ALL)
    print(Fore.RED + "4. Salir" + Style.RESET_ALL)

def solve_case():
    """Resuelve el caso utilizando un solver SAT."""
    cnf = CNF()

    P_Al, P_M, P_An, P_B, P_D, P_W = 1, 2, 3, 4, 5, 6

    T_C, T_H, T_E, T_A, T_P = 7, 8, 9, 10, 11

    cnf.append([-P_B, P_Al])
    cnf.append([-P_D]) 
    cnf.append([-P_Al]) 
    cnf.append([-P_W])
    cnf.append([-P_An, P_B])
    cnf.append([P_Al, P_M, P_An, P_B, P_D, P_W])

    for i in range(1, 7):
        for j in range(i + 1, 7):
            cnf.append([-i, -j])

    cnf.append([-T_H])
    cnf.append([-T_C])
    cnf.append([T_P, T_C, T_H, T_E, T_A])
    cnf.append([-T_E])
    cnf.append([T_P, T_A, T_C])
    cnf.append([T_P])
    cnf.append([-T_E, T_P])
    cnf.append([T_P, T_C])


    solver = Solver()
    solver.append_formula(cnf)
    satisfiable = solver.solve()
    model = solver.get_model() if satisfiable else None
    return satisfiable, model

def interpret_solution(model):
    """Interpreta el resultado del solver y determina el culpable y la trampa."""
    if model:
        suspect_map = {
            1: "Alan",
            2: "Melina",
            3: "Andrea",
            4: "Brisa",
            5: "Daniel",
            6: "Wilmar"
        }
        trap_map = {
            7: "Uso el celular (chat GPT)",
            8: "Tenía hojas ocultas (respuestas, apuntes)",
            9: "Se robó el examen un día antes",
            10: "Audífono oculto",
            11: "Se copió de un compañero/a"
        }

        guilty_suspect = None
        for suspect in suspect_map.keys():
            if suspect in model:
                guilty_suspect = suspect_map[suspect]
                break

        trap_used = None
        for trap in trap_map.keys():
            if trap in model:
                trap_used = trap_map[trap]
                break

        if guilty_suspect and trap_used:
            print(Fore.RED + "-"*80 + Style.RESET_ALL)
            print(f"\nEl culpable es: {guilty_suspect}")
            print(f"La trampa utilizada es: {trap_used} \n")
            print(Fore.RED + "-"*80 + Style.RESET_ALL)
        else:
            print("No se pudo determinar el culpable o la trampa.")
    else:
        print("No hay solución válida para el caso.")

def play():
    """Función principal que maneja el flujo del juego."""
    print_banner()
    print_game_intro()
    while True:
        show_menu()
        choice = input("Selecciona una opción (1-4): ").strip()

        print("\n"+Fore.RED + "-"*80 + Style.RESET_ALL)

        if choice == '1':
            print(Fore.CYAN + "Has seleccionado: Ver culpables y trampas" + Style.RESET_ALL)
            show_characters_and_traps()
        elif choice == '2':
            print(Fore.CYAN + "Has seleccionado: Ver declaraciones y pistas" + Style.RESET_ALL)
            show_clues()
        elif choice == '3':
            print(Fore.CYAN + "Has seleccionado: Ver resolución del caso" + Style.RESET_ALL)
            satisfiable, model = solve_case()
            if satisfiable:
                print("El caso es resoluble.")
                interpret_solution(model)
            else:
                print("El caso no es resoluble.")
        elif choice == '4':
            print(Fore.RED + "Saliendo ..." + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Opción inválida. Por favor, elige 1, 2, 3 o 4." + Style.RESET_ALL)

if __name__ == "__main__":
    play()