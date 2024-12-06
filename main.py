from clase import *
from menu_mesas import *
from menu_comidas import *
from menu_pedidos import *
from colorama import init, Fore

init()

def menu_opciones():
    print(Fore.CYAN + '='*30 + ' Menú de opciones ' + '='*30)
    print('1- Mesas')
    print('2- Menú de comida')
    print('3- Pedido' + Fore.RESET)
    print()



def main():

    op = -1

    while op != 0:
        menu_opciones()
        op = int(input(Fore.GREEN + 'Ingrese una opción (0 para salir): ' + Fore.RESET))

        if op == 1:
            sub_menu_mesas()
        if op == 2:
            sub_menu_comidas()
        if op == 3:
            sub_menu_pedidos()
    
    print(Fore.GREEN + 'Hasta pronto....' + Fore.RESET)






if __name__ == "__main__":
    main()