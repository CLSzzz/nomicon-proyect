import subprocess

def print_menu():
    print("1. Mostrar IP")
    print("2. Limpiar memoria caché DNS")
    print("3. Sistema operativo")
    print("4. Revisor de firewall")
    print("5. Generador de contraseñas")
    print("6. Generador de hash")
    print("7. Uso del sistema ")
    print("8. Uso de discos")
    print("9. Salir")

def mostrar_ip():
    try:
        result = subprocess.run(['ipconfig'], capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando: {e}")

def limpiar_cache():  
    try:
        subprocess.run(['ipconfig', '/flushdns'], check=True)
        print("Memoria caché de DNS limpiada.")
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando: {e}")

import subprocess

def abrir_winver():
    try:
        subprocess.run(['winver'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando 'winver': {e}")

def revisar_firewall():
    try:
        result = subprocess.run(['netsh', 'advfirewall', 'show', 'allprofiles'], capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando: {e}")

import random
import string

def generar_contrasena():
    longitud = int(input("Introduce la longitud de la contraseña: "))
    caracteres = string.ascii_letters + string.digits 
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
    print(f"Contraseña generada: {contrasena}")

import hashlib

def revisor_hash_archivo():
    archivo = input("Introduce la ruta del archivo: ")
    
    print("Selecciona el tipo de hash:")
    print("1. MD5")
    print("2. SHA-1")
    print("3. SHA-256")
    tipo_hash = input("Selecciona una opción (1/2/3): ")

    try:
        if tipo_hash == '1':
            hash_obj = hashlib.md5()
            print("Calculando MD5...")
        elif tipo_hash == '2':
            hash_obj = hashlib.sha1()
            print("Calculando SHA-1...")
        elif tipo_hash == '3':
            hash_obj = hashlib.sha256()
            print("Calculando SHA-256...")
        else:
            print("Opción no válida.")
            return

        with open(archivo, "rb") as f:
            for bloque in iter(lambda: f.read(4096), b""):
                hash_obj.update(bloque)

        print(f"El hash del archivo es: {hash_obj.hexdigest()}")

    except FileNotFoundError:
        print("Archivo no encontrado.")
    except Exception as e:
        print(f"Error: {e}")

import psutil

def monitoreo_sistema():
    uso_cpu = psutil.cpu_percent(interval=1)
    memoria = psutil.virtual_memory()
    print(f"Uso de CPU: {uso_cpu}%")
    print(f"Memoria RAM disponible: {memoria.available / (1024 ** 2):.2f} MB")
    print(f"Memoria RAM en uso: {memoria.percent}%")

def mostrar_espacio_disco():
    particiones = psutil.disk_partitions()

    for particion in particiones:
        uso_disco = psutil.disk_usage(particion.mountpoint)
        
        print(f"Partición: {particion.device}")
        print(f"  Punto de montaje: {particion.mountpoint}")
        print(f"  Sistema de archivos: {particion.fstype}")
        print(f"  Espacio total: {uso_disco.total / (1024 ** 3):.2f} GB")
        print(f"  Espacio utilizado: {uso_disco.used / (1024 ** 3):.2f} GB")
        print(f"  Espacio disponible: {uso_disco.free / (1024 ** 3):.2f} GB")
        print(f"  Porcentaje utilizado: {uso_disco.percent}%")
        print()

def main():
    while True:
        print_menu()
        try:
            seleccion = int(input("Selecciona una opción: "))
            if seleccion == 1:
                mostrar_ip()
            elif seleccion == 2:
                limpiar_cache()
            elif seleccion == 3:
                abrir_winver()
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
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Por favor, selecciona una opción del menú.")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")


if __name__ == "__main__":
    main()
