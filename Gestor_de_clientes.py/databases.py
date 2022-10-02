class Cliente (): 

    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    def __str__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}, Dni {self.dni}'

#preguntar por qué no se me crea el picache

class Clientes ():

    def __init__(self):
        self.clientes = []

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def mostrar_clientes(self):
        for cliente in self.clientes:
            print(cliente)

    def buscar_cliente(self, dni):
        for cliente in self.clientes:
            if cliente.dni == dni:
                return cliente
        return None

    def eliminar_cliente(self, dni):
        cliente = self.buscar_cliente(dni)
        if cliente:
            self.clientes.remove(cliente)
            return True
        return False

    def modificar_cliente(self, dni, nombre, apellido):
        cliente = self.buscar_cliente(dni)
        if cliente:
            cliente.nombre = nombre
            cliente.apellido = apellido
            return True
        return False

    def guardar_clientes(self):
        with open('clientes.txt', 'w') as f:
            for cliente in self.clientes:
                f.write(f'{cliente.nombre},{cliente.apellido},{cliente.dni}

')

    def cargar_clientes(self):
        with open('clientes.txt', 'r') as f:
            for linea in f:
                datos = linea.strip().split(',')
                cliente = Cliente(datos[0], datos[1], datos[2])
                self.clientes.append(cliente)