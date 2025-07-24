# Esteban Andres Ramirez Gonzalez
# Inacap Ingenieria en informatica - Vespertino
# Base de datos no relacionales

class Usuario():
    def __init__(self, Id_u:int, usuario:str, nombre_u:str, apellIdo_u:int, email:str, contraseña:str, estado_u:bool):
        self.Id_u = Id_u
        self.usuario = usuario
        self.nombre = nombre_u
        self.apellIdo_u = apellIdo_u
        self.email = email
        self.contraseña = contraseña
        self.estado_u = estado_u
    
    def mostrarDatos(self):
        print(f"Id: {self.Id} - Usuario {self.usuario} - Nombre: {self.nombre} - ApellIdo: {self.apellIdo_u} - Email: {self.email} - Contraseña: {self.contraseña}")

    def __str__(self):
        return f"Nombre: {self.nombre}"
