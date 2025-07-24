# Esteban Andres Ramirez Gonzalez
# Inacap Ingenieria en informatica - Vespertino
# Base de datos no relacionales

from pymongo import MongoClient
from pymongo.errors import PyMongoError

class Conexion():
    def __init__(self, db_name="Libreria"): # Nombre de la BD
        self.client = None # Uso de client para ir de acorde con pymongo
        self.db = None # Almacenar la base de datos
        self.db_name = db_name
        self.conectar()

    def conectar(self):
        try:
            self.client = MongoClient("mongodb+srv://esteban:Earg241690@cluster0.8y7ebgm.mongodb.net/?retryWrites=true&w=majority")
            
            self.client.admin.command('ping') # Verificar la conexión al servIdor

            self.db = self.client[self.db_name] # Selecciona la base de datos
            print(f"Conexión exitosa a la base de datos '{self.db_name}'") #imprimir que se conecto a la BD
       
        except Exception as err:
            print(f"Error al conectar: {err}")
            self.client = None                     # Si el cliente esta None significa que falla la conexión

    def obtenerConexion(self):
        # Aquí deberías devolver la base de datos, no el cliente,
        # si tu intención es interactuar con colecciones.
        # O puedes tener obtenerCliente() y obtenerDB()
        if self.db is None: # Si la DB no está disponible
            print("Error al iniciar la conexion, Intentando reconectar..")
            self.conectar() # Intenta reconectar

        return self.db # Devuelve el objeto de base de datos

    def cerrarConexion(self):
        if self.client: # Verifica si el cliente existe
            self.client.close()
            self.client = None # Establecer a None después de cerrar
            self.db = None # También la base de datos
            print("La conexión se ha cerrado con éxito")
