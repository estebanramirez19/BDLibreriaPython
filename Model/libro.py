# Esteban Andres Ramirez Gonzalez
# Inacap Ingenieria en informatica - Vespertino
# Base de datos no relacionales


class Libro():
    def __init__(self, id:int, nombre:str, precio:int, genero:str, tipo_tapa:str ,paginas:int, autor:str , stock:int):
        self.nombre = nombre
        self.id = id
        self.precio = precio
        self.genero = genero
        self.tipo_tapa = tipo_tapa
        self.paginas = paginas
        self.autor = autor
        self.stock = stock

    
    def mostrarDatos(self):
        print(f"ID: {self.id} - Nombre del libro: {self.nombre}  - precio: {self.precio} - Genero: {self.genero} - Tipo de tapa: {self.tipo_tapa} - Paginas: {self.paginas} - Autor: {self.autor} - Stock: {self.stock}")
    
    

    def __str__(self):
        return f"Nombre del libro: {self.nombre}"
