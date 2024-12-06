from colorama import init, Fore

class Mesa:
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad
        self.estado = 'libre'
    
    def reservar(self):
        if self.estado == 'libre':
            self.estado = 'ocupada'
            return True
        return False
    
    def liberar(self):
        if self.estado == 'ocupada':
            self.estado = 'libre'
            return True
        return False
    
    def verificar_estado(self):
        return self.estado
    
class Pedido:
    def __init__(self):
        self.items = []
        self.estado = 'en preparación'

    def agregar_item(self, item):
        self.items.append(item)
    
    def borrar_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def calc_total(self):
        return sum(item.precio for item in self.items)

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

class Menu:
    def __init__(self):
        self.items = []

    def agregar_item(self, nombre, descripcion, precio):
        self.items.append(ItemMenu(nombre, descripcion, precio))

    def borrar_item(self, nombre):
        self.items = [item for item in self.items if item.nombre.lower() != nombre]
    
    def mostrar_menu(self):
        for i in self.items:
            print(f'{i.nombre}:  {i.descripcion} - ${i.precio}')

class ItemMenu:
    def __init__(self, nombre, descripcion, precio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mesa_asignada = None
        self.pedido_actual = Pedido()
    
    def asignar_mesa(self, mesa):
        self.mesa_asignada = mesa
    
    def realizar_pedido(self, items):
        for i in items:
            self.pedido_actual.agregar_item(i)
    
    def ver_cuenta(self):
        total = self.pedido_actual.calc_total()
        print(f'Total a pagar: ${total}')
        return total
    
class Restaurante:
    def __init__(self):
        self.mesas = []
        self.menu = Menu()
        self.clientes = []

    def añadir_mesa(self, numero, capacidad):
        self.mesas.append(Mesa(numero, capacidad))
    
    def borrar_mesa(self, numero):
        self.mesas = [mesa for mesa in self.mesas if mesa.numero != numero]

    def mostrar_mesas_disponibles(self):
        hay_mesas_disponibles = False
        for mesa in self.mesas:
            if mesa.verificar_estado() == 'libre':
                print(Fore.LIGHTYELLOW_EX + f'Mesa: {mesa.numero} (Capacidad: {mesa.capacidad}) está disponible.' + Fore.RESET)
                print()
                hay_mesas_disponibles = True
        if not hay_mesas_disponibles:
            print(Fore.RED + 'No hay mesas disponibles...' + Fore.RESET)
            
    
    def hacer_reserva(self, cliente, numero_mesa):
        for mesa in self.mesas:
            if mesa.numero == numero_mesa and mesa.reservar():
                cliente.asignar_mesa(mesa)
                self.clientes.append(cliente)
                print(Fore.LIGHTYELLOW_EX + f'Mesa {numero_mesa} reservada para {cliente.nombre}.' + Fore.RESET)
                return True
        print(Fore.RED + f'La mesa {numero_mesa} no está disponible.' + Fore.RESET)
        return False

    def gestionar_pedido(self, cliente, items):
        if cliente in self.clientes:
            cliente.realizar_pedido(items)
            print(Fore.LIGHTYELLOW_EX + f'Pedido realizado para {cliente.nombre}' + Fore.RESET)
        else:
            print(Fore.RED + 'Cliente no registrado' + Fore.RESET)
    
    def mostrar_menu(self):
        self.menu.mostrar_menu()

    def escoger_items_del_menu(self, cliente):
        if cliente in self.clientes:
            self.mostrar_menu()
            items_seleccionados = []
            while True:
                item_nombre = input(Fore.GREEN + 'Ingrese el nombre del item que desea (o "fin" para terminar): ' + Fore.RESET)
                if item_nombre.lower() == 'fin':
                    break
                item_encontrado = next((item for item in self.menu.items if item.nombre.lower() == item_nombre.lower()), None)
                if item_encontrado:
                    items_seleccionados.append(item_encontrado)
                else:
                    print(Fore.RED + 'Item no encontrado. Intente de nuevo.' + Fore.RESET)
            self.gestionar_pedido(cliente, items_seleccionados)
        else:
            print(Fore.RED + 'Cliente no encontrado.' + Fore.RESET)
    def mostrar_cuenta(self, cliente):
        if cliente in self.clientes:
            cliente.ver_cuenta()
        else:
            print(Fore.RED + 'Cliente no registrado.' + Fore.RESET)