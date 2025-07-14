# Esteban Andres Ramirez Gonzalez
# Inacap Ingenieria en informatica - Vespertino
# Base de datos no relacionales

class Usuario():
    def __init__(self, id:int, usuario:str, nombre_u:str, apellido_u:int, email:str, contraseña:str):
        self.id = id
        self.usuario = usuario
        self.nombre = nombre_u
        self.apellido_u = apellido_u
        self.email = email
        self.contraseña = contraseña
    
    def mostrarDatos(self):
        print(f"ID: {self.id} - Usuario {self.usuario} - Nombre: {self.nombre} - Apellido: {self.apellido_u} - Email: {self.email} - Contraseña: {self.contraseña}")

    def __str__(self):
        return f"Nombre: {self.nombre}"
