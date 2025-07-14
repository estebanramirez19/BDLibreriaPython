# Esteban Andres Ramirez Gonzalez
# Inacap Ingenieria en informatica - Vespertino
# Base de datos no relacionales

from Database.Conexion import Conexion
from pymongo.errors import PyMongoError

# **Clase AutorDAO corregida:**
class AutorDAO:
    def __init__(self):
        self.conn = Conexion() # Instancia de tu clase de conexión
        self.collection = self.conn.obtenerConexion()["libros"] # Accede a la colección 'libros'

    def agregarAutor(self,id, nombre, precio, genero, tipo_tapa ,paginas, autor ):
        try:
            
            document = {"ID": %s, "Nombre libro": %s, "Precio": %s, "Genero":%s, "Tipo de tapa": %s, "Paginas": %s, "Autor": %s}

            #  Insertar el documento en la colección
            result = self.collection.insert_one(document)

            #  Verificar el resultado de la inserción
            if result.inserted_id:
                print(f"Libro '{nombre}' con ID '{id}' agregado correctamente. MongoDB _id: {result.inserted_id}")
                return True # Indica éxito
            else:
                print(f"Error desconocido al agregar el Libro '{nombre}'.")
                return False # Indica fallo
            
            

        except PyMongoError as ex:
            # Captura errores específicos de PyMongo (ej. duplicados si usas _id)
            print(f"Error de PyMongo al agregar autor: {ex}")
            return False
        except Exception as ex:
            # Captura cualquier otro error inesperado
            print(f"Error inesperado al agregar autor: {ex}")
            return False
        finally:
            # En DAO's pequeños, no siempre necesitas cerrar la conexión aquí.
            # El pool de conexiones de PyMongo es eficiente.
            # Cierras la conexión cuando tu aplicación termina, no en cada operación.
            # self.conn.cerrarConexion() # Esto cerraría la conexión después de cada operación, lo cual es ineficiente.
            pass # No cerramos la conexión aquí. Se gestiona por la instancia de Conexion.
