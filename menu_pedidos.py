from clase import * 
from globals import restaurante
from colorama import  Fore

def menu_pedidos():
    print(Fore.LIGHTBLUE_EX + '='*30 + ' Menú de pedidos ' + '='*30)
    print('1- Hacer un pedido' + Fore.RESET)
    print('')

def sub_menu_pedidos():
    global restaurante
    op = -1 
    while op != 0:
        menu_pedidos()
        op = int(input(Fore.GREEN + 'Ingrese una opción (0 para volver atrás): ' + Fore.RESET))
        
        if op == 1:
            cliente = str(input(Fore.GREEN + 'Ingrese su nombre: ' + Fore.RESET))
            cliente_encontrado = next((c for c in restaurante.clientes if c.nombre.lower() == cliente.lower()), None)
            
            if cliente_encontrado:
                restaurante.escoger_items_del_menu(cliente_encontrado)
            
            restaurante.mostrar_cuenta(cliente_encontrado)
        else: 
            print(Fore.RED + 'Ingrese una opción válida...' + Fore.RESET)

        