from pysat.solvers import Solver
from pysat.formula import CNF
from colorama import init, Fore, Style

init(autoreset=True)

def print_banner():
    """Imprime el banner del juego."""
    banner = r"""
  █▄ █ █ █ █ █▀▀ █     █▀▀ ▄▀█ █▀▀ █ █ 
  █ ▀█ █ ▀▄▀ ██▄ █▄▄   █▀  █▀█ █▄▄ █ █▄▄
    """
    print(Fore.YELLOW + Style.BRIGHT + banner + Style.RESET_ALL)
    print(Fore.YELLOW + "===== El Misterio del Museo =====")

def obtener_nombre_sospechoso(numero):
    """Devuelve el nombre del sospechoso basado en el número."""
    nombres = {1: "Alicia", 2: "Bruno", 3: "Carmen", 4: "Daniel", 5: "Elena"}
    return nombres.get(numero, "Desconocido")

def agregar_clausula(clausulas, numero_sospechoso, afirmacion):
    """Agrega una cláusula a la lista de cláusulas dependiendo de la afirmación."""
    if afirmacion:
        clausulas.append([numero_sospechoso])
    else:
        clausulas.append([-numero_sospechoso])

def solicitar_respuesta(nombre):
    """Solicita al jugador que afirme o niegue una declaración."""
    while True:
        respuesta = input(f"\n¿Desea afirmar (a) o negar (n) la declaración de {nombre}? (a/n): ").strip().lower()
        if respuesta in ['a', 'n']:
            return respuesta
        else:
            print(Fore.RED + "Entrada inválida. Escoger (a o n)" + Style.RESET_ALL)

def play():
    """Lógica principal del juego."""
    print_banner()
    print(Fore.RED + "¡Bienvenido al juego 'El Misterio del Museo'!")
    print(Fore.YELLOW + "=" * 80 + Style.RESET_ALL)
    print("\nDebes encontrar al ladrón que robó un retrato valioso en el museo.")
    print("\nSospechosos: Alicia, Bruno, Carmen, Daniel y Elena.")
    print("Afirmaciones:\n")
    
    print(Fore.GREEN + "1. Alicia:" + Fore.CYAN + " 'No soy la culpable.'")
    print(Fore.MAGENTA + "2. Bruno:" + Fore.CYAN + " 'Carmen no es la culpable.'")
    print(Fore.RED + "3. Carmen:" + Fore.CYAN + " 'El ladrón es uno de los visitantes frecuentes.'")
    print(Fore.BLUE + "4. Daniel:" + Fore.CYAN + " 'Alicia es la culpable.'")
    print(Fore.YELLOW + "5. Elena:" + Fore.CYAN + " 'Bruno no es el culpable.'\n")
    
    names = {
        1: Fore.GREEN + "Alicia" + Style.RESET_ALL,
        2: Fore.MAGENTA + "Bruno" + Style.RESET_ALL,
        3: Fore.RED + "Carmen" + Style.RESET_ALL,
        4: Fore.BLUE + "Daniel" + Style.RESET_ALL,
        5: Fore.YELLOW + "Elena" + Style.RESET_ALL
    }

    afirmaciones = {i: solicitar_respuesta(names[i]) for i in range(1, 6)}

    clauses = []

    agregar_clausula(clauses, 1, afirmaciones[1] == "n")
    agregar_clausula(clauses, 3, afirmaciones[2] == "n")
    
    if afirmaciones[3] == "n":
        agregar_clausula(clauses, 4, False)
        agregar_clausula(clauses, 5, False)
    else:
        agregar_clausula(clauses, 4, True)
        agregar_clausula(clauses, 5, True)
    
    agregar_clausula(clauses, 1, afirmaciones[4] == "a")
    agregar_clausula(clauses, 2, afirmaciones[5] == "n")
    
    clauses.append([1, 2, 3, 4, 5])
    clauses.append([-1, -2, -3, -4, -5])

    solver = Solver()
    solver.append_formula(clauses)

    if solver.solve():
        model = solver.get_model()
        culpable = next((i for i in range(1, 6) if i in model), None)

        if culpable:
            print(Fore.GREEN + f"\nEl ladrón es {obtener_nombre_sospechoso(culpable)}.")
        else:
            print(Fore.RED + "\nNo se pudo determinar el culpable con la información dada.")
    else:
        print(Fore.RED + "\nNo se pudo encontrar una solución con la información dada.")

if __name__ == "__main__":
    play()