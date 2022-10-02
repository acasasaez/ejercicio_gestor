class Cliente (): 

    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    def __str__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}, Dni {self.dni}'

print (Cliente('Juan', 'Perez', '12345678'))