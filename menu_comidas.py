from clase import * 
from globals import restaurante
from colorama import init, Fore

def menu_comida():
    print(Fore.MAGENTA + '='*30 + ' Menú de comidas ' + '='*30)
    print('1- Agregar platos')
    print('2- Mostrar menú')
    print('3- Borrar plato del menú' + Fore.RESET)
    print('')

def sub_menu_comidas():
    # menu = Menu()
    op = -1 
    while op != 0:
        menu_comida()
        op = int(input(Fore.GREEN + 'Ingrese una opción (0 para volver atrás): ' + Fore.RESET))

        if op == 1:
            nombre = str(input(Fore.GREEN + 'Ingrese nombre del plato: ' + Fore.RESET))
            descripcion = str(input(Fore.GREEN + 'Ingrese descripción: ' + Fore.RESET))
            precio = round(float(input(Fore.GREEN +'Ingrese precio del plato: ' + Fore.RESET)), 2)
            restaurante.menu.agregar_item(nombre, descripcion, precio)
            print(Fore.LIGHTYELLOW_EX + 'Agregado!!!' + Fore.RESET)
            print()
        
        if op == 2: 
            restaurante.menu.mostrar_menu()
        if op == 3:
            nombre = str(input(Fore.GREEN + 'Ingrese nombre del plato a borrar: ' + Fore.RESET))
            restaurante.menu.borrar_item(nombre)
            print(Fore.LIGHTYELLOW_EX + 'Borrado exitosamente...' + Fore.RESET)
            print()