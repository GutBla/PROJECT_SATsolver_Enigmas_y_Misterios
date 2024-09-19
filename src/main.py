import os
from colorama import init, Fore, Style

try:
    import levels.easy_level as easy_level
    import levels.intermediate_level as intermediate_level
    import levels.advanced_level as advanced_level
except ImportError as e:
    print(Fore.RED + f"Error al importar los módulos: {e}" + Style.RESET_ALL)
    exit(1)

init(autoreset=True)

def clear_screen():
    """Limpia la pantalla de la consola según el sistema operativo."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def print_banner():
    """Imprime el banner principal del juego."""
    banner = r"""
    ███╗   ███╗███████╗███╗   ██╗██╗   ██╗ 
    ████╗ ████║██╔════╝████╗  ██║██║   ██║ 
    ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
    ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║
    ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
    ╚═╝     ╚═╝╚══════╝╚═╝    ╚═╝ ╚═════╝


    █▀▀ █▄ █ █ █▀▀ █▀▄▀█ ▄▀█ █▀   █▄█   █▀▄▀█ █ █▀ ▀█▀ █▀▀ █▀█ █ █▀█ █▀
    ██▄ █ ▀█ █ █▄█ █ ▀ █ █▀█ ▄█    █    █ ▀ █ █ ▄█  █  ██▄ █▀▄ █ █▄█ ▄█

    """
    print(Fore.MAGENTA + Style.BRIGHT + banner + Style.RESET_ALL)

def continue_prompt():
    """Pregunta al usuario si quiere volver al menú principal o salir."""
    while True:
        user_input = input(Fore.GREEN + "\n¿Quieres volver al menú principal? (s/n): " + Style.RESET_ALL).strip().lower()
        if user_input in ['s', 'n']:
            return user_input == 's'
        else:
            print(Fore.RED + "Opción no válida. Por favor, ingresa 's' o 'n'." + Style.RESET_ALL)

def jugar_nivel_facil():
    """Ejecuta el nivel fácil."""
    clear_screen()
    easy_level.play()
    if not continue_prompt():
        exit()

def jugar_nivel_intermedio():
    """Ejecuta el nivel intermedio."""
    clear_screen()
    intermediate_level.play()
    if not continue_prompt():
        exit()

def jugar_nivel_avanzado():
    """Ejecuta el nivel avanzado."""
    clear_screen()
    advanced_level.play()
    if not continue_prompt():
        exit()

def main_menu():
    """Muestra el menú principal y maneja las opciones del usuario."""
    while True:
        clear_screen()
        print_banner()
        print(Fore.MAGENTA + "="*80 + Style.RESET_ALL)
        print("\nEn este fascinante juego de misterio, te pondrás en los zapatos del famoso detective Hércules Poirot, "
              "un maestro en el arte de resolver crímenes y desentrañar enigmas. Tu misión es adentrarte en uno de los tres intrigantes casos "
              "que desafiarán tus habilidades de deducción. Cada caso tiene un nivel de dificultad distinto, y es tu oportunidad para demostrar "
              "que nada escapa a tu aguda percepción. ¿Podrás descubrir la verdad oculta tras cada uno de estos misterios?\n" + Style.RESET_ALL)
        print(Fore.MAGENTA + "="*80 + Style.RESET_ALL)

        print(Style.BRIGHT + "\nOPCIONES DE CASOS A RESOLVER : \n")
        print(Fore.YELLOW + "1. El Misterio del Museo (Fácil)" + Style.RESET_ALL)
        print(Fore.CYAN + "2. Asesinato en la Mansión Baker Street (Intermedio)" + Style.RESET_ALL)
        print(Fore.RED + "3. Alguien hizo trampa en el Examen (Avanzado)" + Style.RESET_ALL)
        print("4. Salir\n" + Style.RESET_ALL)

        print(Fore.MAGENTA + "="*80 + Style.RESET_ALL)
        opcion = input("\nIngresa tu opción (1-4): ").strip()

        if opcion == '1':
            jugar_nivel_facil()
        elif opcion == '2':
            jugar_nivel_intermedio()
        elif opcion == '3':
            jugar_nivel_avanzado()
        elif opcion == '4':
            print(Fore.MAGENTA + "Gracias por jugar, Saliendo ..." + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Opción no válida. Por favor, ingresa un número entre 1 y 4." + Style.RESET_ALL)

if __name__ == "__main__":
    main_menu()