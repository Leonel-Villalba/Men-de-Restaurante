from clase import *
from globals import restaurante
from colorama import Fore

def menu_mesas():
    print(Fore.LIGHTWHITE_EX + '='*30 + ' Menú de mesas ' + '='*30)
    print('1- Añadir mesa')
    print('2- Mostrar mesas disponibles')
    print('3- Borrar mesa')
    print('4- Hacer una reserva' + Fore.RESET)

def cargar_mesas():
    while True:
        numero = int(input(Fore.GREEN + 'Ingrese el numero de la mesa: ' + Fore.RESET))
        if numero < 0: 
            numero = int(input(Fore.RED + 'Ingrese un numero de mesa valido: ' + Fore.RESET))
        capacidad = int(input(Fore.GREEN + f'Ingrese la capacidad de la mesa {numero} : ' + Fore.RESET))
        if capacidad <= 0:
            capacidad = int(input(Fore.RED + 'Por favor ingrese una capacidad valida: ' + Fore.RESET))
        
        mesa = restaurante.añadir_mesa(numero, capacidad)
        print(Fore.LIGHTYELLOW_EX + 'Mesa cargada exitosamente!!!' + Fore.RESET)
        print()
        return mesa

def sub_menu_mesas():
    global restaurante
    op = -1 
    while op != 0:
        menu_mesas()
        op = int(input(Fore.GREEN + 'Ingrese una opción (0 para volver atrás): ' + Fore.RESET))

        if op == 1:
            cargar_mesas()
        if op == 2:
            restaurante.mostrar_mesas_disponibles()
            
        if op == 3: 
            numero = int(input(Fore.GREEN + 'Ingrese numero de mesa que desea borrar: ' + Fore.RESET))
            restaurante.borrar_mesa(numero)
            print(Fore.LIGHTYELLOW_EX + 'La mesa fue borrada...' + Fore.RESET)
            print()
        if op == 4:
            nombre = input(Fore.GREEN + 'Ingrese nombre del cliente: ' + Fore.RESET)
            n_mesa = int(input(Fore.GREEN + 'Ingrese numero de mesa a reservar: ' + Fore.RESET))
            cliente = Cliente(nombre)
            restaurante.hacer_reserva(cliente, n_mesa)
