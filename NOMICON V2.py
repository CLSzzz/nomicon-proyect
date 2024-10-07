import subprocess
import os
import cpuinfo
import platform
import psutil
import random
import string
import hashlib
import msvcrt  # Para esperar la tecla presionada en Windows
from colorama import Fore, Style, init
from rich.console import Console
from rich.table import Table
import time
import tkinter as tk
from tkinter import filedialog
import GPUtil

init(autoreset=True)  # Inicializar colorama para restablecer los colores automáticamente
console = Console()

def print_menu():
    os.system('cls')  # Limpiar la pantalla
    print(Fore.MAGENTA + """
███╗   ██╗ ██████╗ ███╗   ███╗██╗ ██████╗ ██████╗ ███╗   ██╗
████╗  ██║██╔═══██╗████╗ ████║██║██╔════╝██╔═══██╗████╗  ██║
██╔██╗ ██║██║   ██║██╔████╔██║██║██║     ██║   ██║██╔██╗ ██║
██║╚██╗██║██║   ██║██║╚██╔╝██║██║██║     ██║   ██║██║╚██╗██║
██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║╚██████╗╚██████╔╝██║ ╚████║
╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝                                              
""")
    
    table = Table(title="", style="blue")
    table.add_column("[#00FFFF]Opción[/]", justify="right", style="bold cyan", no_wrap=True)
    table.add_column("[#00FFFF]Descripción[/]", style="bold cyan")

    table.add_row("[1]", "Mostrar IP")
    table.add_row("[2]", "Limpiar memoria caché DNS")
    table.add_row("[3]", "Información del sistema")
    table.add_row("[4]", "Revisor de firewall")
    table.add_row("[5]", "Generador de contraseñas")
    table.add_row("[6]", "Generador de hash")
    table.add_row("[7]", "Uso del sistema")
    table.add_row("[8]", "Uso de discos")
    table.add_row("[#FFFFFF][9][/]", "[#FFFFFF]Salir[/]")

    console.print(table)
    
def esperar_tecla():
    print(f"\n{Fore.WHITE}Presiona cualquier tecla para volver al menú...")
    msvcrt.getch()  # Espera a que el usuario presione una tecla

def mostrar_ip():
    print(f"{Fore.MAGENTA}{'=' * 40}")
    try:
        result = subprocess.run(['ipconfig'], capture_output=True, text=True, check=True)
        print(f"{Fore.CYAN}{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}Error al ejecutar el comando: {e}")
    print(f"{Fore.MAGENTA}{'=' * 40}")

def limpiar_cache():  
    print(f"{Fore.MAGENTA}{'=' * 40}")
    try:
        subprocess.run(['ipconfig', '/flushdns'], capture_output=True, text=True, check=True)
        print(f"{Fore.CYAN}Memoria caché de DNS limpiada.")
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}Error al ejecutar el comando: {e}")
    print(f"{Fore.MAGENTA}{'=' * 40}")

def mostrar_informacion_sistema():
    print(f"{Fore.MAGENTA}{'=' * 40}")
    print(f"{Fore.CYAN}Información del sistema:")
    print(f"{Fore.CYAN}Sistema operativo: {platform.system()} {platform.release()}")
    print(f"{Fore.CYAN}Arquitectura: {platform.architecture()[0]}")
    
    cpu_info = cpuinfo.get_cpu_info()
    print(f"{Fore.CYAN}Procesador: {cpu_info['brand_raw']}")
    print(f"{Fore.CYAN}RAM total: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB")

    try:
        result = subprocess.run(['wmic', 'path', 'win32_videocontroller', 'get', 'caption'], capture_output=True, text=True, check=True)
        output_lines = result.stdout.splitlines()
        print(f"{Fore.CYAN}Tarjeta gráfica:")
        for line in output_lines[1:]:
            if line.strip():
                print(f"{Fore.CYAN}  {line.strip()}")
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}Error al ejecutar el comando para obtener información de la tarjeta gráfica: {e}")
    print(f"{Fore.MAGENTA}{'=' * 40}")

def revisar_firewall():
    print(f"{Fore.MAGENTA}{'=' * 40}")
    try:
        result = subprocess.run(['netsh', 'advfirewall', 'show', 'allprofiles'], capture_output=True, text=True, check=True)
        print(f"{Fore.CYAN}{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}Error al ejecutar el comando: {e}")
    print(f"{Fore.MAGENTA}{'=' * 40}")

def generar_contrasena():
    print(f"{Fore.MAGENTA}{'=' * 40}")
    longitud = int(input(f"{Fore.CYAN}Introduce la longitud de la contraseña: "))  
    caracteres = string.ascii_letters + string.digits 
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
    print(f"{Fore.CYAN}Contraseña generada: {contrasena}")
    print(f"{Fore.MAGENTA}{'=' * 40}")

def revisor_hash_archivo():
    # Inicializa la ventana de tkinter (no se mostrará)
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal

    print(f"{Fore.MAGENTA}{'=' * 40}")
    
    # Abre un cuadro de diálogo para seleccionar el archivo
    archivo = filedialog.askopenfilename(title="Selecciona el archivo", 
                                          filetypes=(("Archivos de todos los tipos", "*.*"),))
    
    if not archivo:  # Si no se seleccionó ningún archivo
        print(f"{Fore.RED}No se seleccionó ningún archivo.")
        return

    print(f"{Fore.CYAN}Seleccionaste el archivo: {archivo}")
    
    print(f"{Fore.CYAN}Selecciona el tipo de hash:")
    print(f"{Fore.GREEN}1. MD5")
    print(f"{Fore.GREEN}2. SHA-1")
    print(f"{Fore.GREEN}3. SHA-256")
    tipo_hash = input("Selecciona una opción (1/2/3): ")

    try:
        if tipo_hash == '1':
            hash_obj = hashlib.md5()
            print(f"{Fore.CYAN}Calculando MD5...")
        elif tipo_hash == '2':
            hash_obj = hashlib.sha1()
            print(f"{Fore.CYAN}Calculando SHA-1...")
        elif tipo_hash == '3':
            hash_obj = hashlib.sha256()
            print(f"{Fore.CYAN}Calculando SHA-256...")
        else:
            print(f"{Fore.RED}Opción no válida.")
            return

        with open(archivo, "rb") as f:
            for bloque in iter(lambda: f.read(4096), b""):
                hash_obj.update(bloque)

        print(f"{Fore.CYAN}El hash del archivo es: {hash_obj.hexdigest()}")

    except FileNotFoundError:
        print(f"{Fore.RED}Archivo no encontrado.")
    except Exception as e:
        print(f"{Fore.RED}Error: {e}")
    print(f"{Fore.MAGENTA}{'=' * 40}")


def monitoreo_sistema():
    print(f"{Fore.MAGENTA}{'=' * 40}")
    uso_cpu = psutil.cpu_percent(interval=1)
    memoria = psutil.virtual_memory()
    print(f"{Fore.CYAN}Uso de CPU: {uso_cpu}%")
    print(f"{Fore.CYAN}Memoria RAM en uso: {memoria.percent}%")
    gpus = GPUtil.getGPUs() 
    for gpu in gpus:
        print(f"{Fore.CYAN}Uso GPU: {gpu.load * 100:.1f}%")
    print(f"{Fore.MAGENTA}{'=' * 40}")

def mostrar_espacio_disco():
    print(f"{Fore.MAGENTA}{'=' * 40}")
    particiones = psutil.disk_partitions()

    for particion in particiones:
        uso_disco = psutil.disk_usage(particion.mountpoint)
        
        print(f"{Fore.CYAN}Partición: {particion.device}")
        print(f"  Punto de montaje: {particion.mountpoint}")
        print(f"  Sistema de archivos: {particion.fstype}")
        print(f"  Espacio total: {uso_disco.total / (1024 ** 3):.2f} GB")
        print(f"  Espacio utilizado: {uso_disco.used / (1024 ** 3):.2f} GB")
        print(f"  Espacio disponible: {uso_disco.free / (1024 ** 3):.2f} GB")
        print(f"  Porcentaje utilizado: {uso_disco.percent}%")
        print()
    print(f"{Fore.MAGENTA}{'=' * 40}")

def main():
    while True:
        print_menu()
        try:
            seleccion = int(input(Fore.CYAN + "Seleccione una opción: " + Style.RESET_ALL))
            os.system('cls')  # Limpiar la pantalla
            if seleccion == 1:
                mostrar_ip()
            elif seleccion == 2:
                limpiar_cache()
            elif seleccion == 3:
                mostrar_informacion_sistema()
            elif seleccion == 4:
                revisar_firewall()
            elif seleccion == 5:
                generar_contrasena()
            elif seleccion == 6:
                revisor_hash_archivo()
            elif seleccion == 7:
                monitoreo_sistema()
            elif seleccion == 8:
                mostrar_espacio_disco()
            elif seleccion == 9:
                print(f"{Fore.RED}Saliendo del programa...")
                break
            else:
                print(f"{Fore.RED}Opción no válida. Por favor, selecciona una opción del menú.")
        except ValueError:
            print(f"{Fore.RED}Entrada no válida. Por favor, ingresa un número entero.")

        esperar_tecla()

if __name__ == "__main__":
    main()
