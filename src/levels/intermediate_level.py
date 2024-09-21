import random
import os
from colorama import init, Fore, Style
from pysat.solvers import Solver

init(autoreset=True)

def clear_screen():
    """Limpia la pantalla dependiendo del sistema operativo."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def print_banner():
    """Imprime el banner principal del juego."""
    banner = r"""
█▄ █ █ █ █ █▀▀ █     █ █▄ █ ▀█▀ █▀▀ █▀█ █▀▄▀█ █▀▀ █▀▄ █ █▀█
█ ▀█ █ ▀▄▀ ██▄ █▄▄   █ █ ▀█  █  ██▄ █▀▄ █ ▀ █ ██▄ █▄▀ █ █▄█
    """
    print(Fore.CYAN + Style.BRIGHT + banner + Style.RESET_ALL)
    print(Fore.CYAN + "===== Asesinato en la Mansión Baker Street =====")

def print_statement(statement):
    """Imprime una declaración del caso."""
    print(Fore.CYAN + "="*80 + Style.RESET_ALL)
    print(Fore.GREEN + "\nPISTA:")
    print(statement + "\n")

def display_options():
    """Muestra las opciones que tiene el jugador."""
    print("\nOpciones:" + Style.RESET_ALL)
    print(Fore.CYAN + "1. Ver declaración siguiente:" + Style.RESET_ALL)
    print(Fore.GREEN + "2. Resolver caso" + Style.RESET_ALL)
    print(Fore.RED + "3. Salir" + Style.RESET_ALL)

def get_suspect_choice():
    """Solicita al jugador que elija un sospechoso."""
    print(Style.BRIGHT + "\n¿Quién crees que es el culpable?")
    suspects = {
        'CM': Fore.YELLOW + 'Coronel Mostaza' + Style.RESET_ALL,
        'SA': Fore.BLUE + 'Señora Azulino' + Style.RESET_ALL,
        'PM': Fore.MAGENTA + 'Profesor Moradillo' + Style.RESET_ALL,
        'SV': Fore.GREEN + 'Señor Verdi' + Style.RESET_ALL,
        'SE': Fore.RED + 'Señorita Escarlata' + Style.RESET_ALL,
        'CL': Fore.WHITE + 'Chef Leblang' + Style.RESET_ALL
    }
    for key, name in suspects.items():
        print(f"{key}: {name}")

    choice = input("Escribe el código del sospechoso (CM, SA, PM, SV, SE, CL): ").strip().upper()
    return choice

def translate_solution(sol):
    """Traduce la solución del SAT solver a nombres de sospechosos."""
    var_names = {
        1: 'SA',
        2: 'CL',
        3: 'PM',
        4: 'SV',
        5: 'SE',
        6: 'CM'
    }
    result = {}
    for var in sol:
        if var > 0:
            result[var_names[var]] = True
        else:
            result[var_names[-var]] = False
    return result

def solve_case():
    """Crea y resuelve el caso usando un SAT solver."""
    clauses = [
        [-1, 2],
        [-2],
        [3, -5],
        [-3, 5],
        [6, 4, 3],
        [-4, 1],
        [-5]
    ]

    solver = Solver()
    for clause in clauses:
        solver.add_clause(clause)

    if solver.solve():
        solution = solver.get_model()
        return translate_solution(solution)
    else:
        return None

def play():
    """Función principal que maneja el flujo del juego."""
    clear_screen()
    print_banner()
    print("\nDurante la fiesta de fin de año en la mansión Baker Street, el anfitrión ha sido asesinado.")
    print("\nEn el momento del crimen, solo seis invitados permanecían en la mansión:")
    print(Fore.YELLOW + "Coronel Mostaza" + Style.RESET_ALL + ", " +
          Fore.BLUE + "Señora Azulino" + Style.RESET_ALL + ", " +
          Fore.MAGENTA + "Profesor Moradillo" + Style.RESET_ALL + ", " +
          Fore.GREEN + "Señor Verdi" + Style.RESET_ALL + ", " +
          Fore.RED + "Señorita Escarlata" + Style.RESET_ALL + " y " +
          Fore.WHITE + "Chef Leblang" + Style.RESET_ALL + ".")
    print("\nExamina las declaraciones, elige a tu sospechoso y resuelve el caso.\n")

    statements = [
        f"Según los testimonios, si la {Fore.BLUE}Señora Azulino{Style.RESET_ALL} es culpable, entonces la {Fore.WHITE}Chef Leblang{Style.RESET_ALL} también lo es, lo que sugiere una posible complicidad entre ambas.",
        f"La {Fore.WHITE}Chef Leblang{Style.RESET_ALL} no es culpable; su coartada es sólida, ya que estaba en la cocina durante el crimen.",
        f"El {Fore.MAGENTA}Profesor Moradillo{Style.RESET_ALL} y la {Fore.RED}Señorita Escarlata{Style.RESET_ALL} están tan interrelacionados que si uno es culpable, el otro también lo es.",
        f"Uno de los sospechosos debe ser el {Fore.YELLOW}Coronel Mostaza{Style.RESET_ALL}, el {Fore.GREEN}Señor Verdi{Style.RESET_ALL} o el {Fore.MAGENTA}Profesor Moradillo{Style.RESET_ALL}.",
        f"Si el {Fore.GREEN}Señor Verdi{Style.RESET_ALL} es culpable, entonces la {Fore.BLUE}Señora Azulino{Style.RESET_ALL} también lo es.",
        f"La {Fore.RED}Señorita Escarlata{Style.RESET_ALL} no es culpable; es la menos beneficiada por la muerte del anfitrión."
    ]

    random.shuffle(statements)

    current_statement_index = 0
    total_statements = len(statements)

    while True:
        if current_statement_index < total_statements:
            print_statement(statements[current_statement_index])
            print(Fore.CYAN + "="*80 + Style.RESET_ALL)
            display_options()

        choice = input("\nSelecciona una opción (1-3): ").strip()

        if choice == '1':
            current_statement_index += 1
            if current_statement_index >= total_statements:
                current_statement_index = total_statements
                print("\nNo hay más declaraciones.")
        elif choice == '2':
            solution = solve_case()
            if solution:
                user_suspect_code = get_suspect_choice()
                var_names = {
                    'CM': 'Coronel Mostaza',
                    'SA': 'Señora Azulino',
                    'PM': 'Profesor Moradillo',
                    'SV': 'Señor Verdi',
                    'SE': 'Señorita Escarlata',
                    'CL': 'Chef Leblang'
                }
                if user_suspect_code in var_names:
                    if solution.get(user_suspect_code, False):
                        print(Fore.GREEN + f"\n¡Correcto! {var_names[user_suspect_code]} es el culpable.")
                    else:
                        print(Fore.RED + f"Lo siento, {var_names[user_suspect_code]} no es el culpable según la solución.")
                else:
                    print(Fore.RED + "Sospechoso inválido.")
            else:
                print(Fore.RED + "\nNo se pudo encontrar una solución.")
            break
        elif choice == '3':
            print(Fore.MAGENTA + "Saliendo del juego..." + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Opción inválida" + Style.RESET_ALL)

if __name__ == "__main__":
    play()