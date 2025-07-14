from pymongo import MongoClient
from pymongo.errors import PyMongoError # Importar la clase base de errores de PyMongo
# Asegúrate de importar tu clase Conexion desde donde la tengas definida
# from .conexion import Conexion # Si está en un archivo diferente, por ejemplo

# **Asumiendo que tu clase Conexion es similar a esta (con mejoras previas):**
class Conexion:
    def __init__(self, db_name="libreria_db"): # Nombre de tu base de datos
        self.client = None
        self.db = None
        self.db_name = db_name
        self.conectar()

    def conectar(self):
        try:
            # Asegúrate de que tu URI de conexión sea correcta y segura
            self.client = MongoClient("mongodb+srv://esteban:Earg241690@cluster0.8y7ebgm.mongodb.net/?retryWrites=true&w=majority")
            self.client.admin.command('ping') # Verifica la conexión al servidor
            self.db = self.client[self.db_name] # Selecciona la base de datos
            print(f"Conexión exitosa a la base de datos '{self.db_name}'")
        except PyMongoError as err: # Captura errores específicos de PyMongo
            print(f"Error de PyMongo al conectar: {err}")
            self.client = None
            self.db = None
        except Exception as err:
            print(f"Error inesperado al conectar: {err}")
            self.client = None
            self.db = None

    def obtenerConexion(self):
        # Devuelve el objeto de la base de datos (DB), no el cliente
        if self.db is None: # Si la DB no está disponible
            print("Error al obtener la conexión, intentando reconectar...")
            self.conectar() # Intenta reconectar
            if self.db is None: # Si la reconexión falló, es un problema grave
                raise Exception("No se pudo establecer la conexión a la base de datos.")
        return self.db

    def cerrarConexion(self):
        if self.client:
            self.client.close()
            self.client = None
            self.db = None
            print("La conexión se ha cerrado con éxito.")


# **Clase AutorDAO corregida:**
class AutorDAO:
    def __init__(self):
        self.conn = Conexion() # Instancia de tu clase de conexión
        self.collection = self.conn.obtenerConexion()["autores"] # Accede a la colección 'autores'

    def agregarAutor(self, id_autor, nombre_autor):
        try:
            # 1. Preparar el documento a insertar como un diccionario Python
            # Es buena práctica dejar que MongoDB genere el _id, o usar ObjectId para el id.
            # Si 'id_autor' es un ID que tú manejas y quieres usarlo como _id:
            # document = {"_id": id_autor, "nombre_autor": nombre_autor}
            # Si quieres un ID generado por ti y un _id autogenerado por MongoDB:
            document = {"id_autor": id_autor, "nombre_autor": nombre_autor}

            # 2. Insertar el documento en la colección
            result = self.collection.insert_one(document)

            # 3. Verificar el resultado de la inserción
            if result.inserted_id:
                print(f"Autor '{nombre_autor}' con ID '{id_autor}' agregado correctamente. MongoDB _id: {result.inserted_id}")
                return True # Indica éxito
            else:
                print(f"Error desconocido al agregar el autor '{nombre_autor}'.")
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


# --- Ejemplo de uso ---
if __name__ == "__main__":
    dao = AutorDAO()

    # Agregar un autor
    dao.agregarAutor(1, "Gabriel Garcia Marquez")
    dao.agregarAutor(2, "Isabel Allende")
    dao.agregarAutor(3, "Jorge Luis Borges")

    # Intentar agregar un autor con el mismo ID si "_id" se usa como clave primaria y es único
    # Si "id_autor" es solo un campo más, se puede duplicar.
    dao.agregarAutor(1, "Nuevo Gabriel Garcia Marquez")

    # Aquí puedes agregar métodos para consultar, actualizar, eliminar, etc.
    # Por ejemplo, para ver los autores:
    print("\n--- Autores en la base de datos ---")
    try:
        db = dao.conn.obtenerConexion()
        autores_collection = db.autores
        for autor in autores_collection.find():
            print(autor)
    except Exception as e:
        print(f"Error al listar autores: {e}")


    # Cuando la aplicación finaliza, deberías cerrar la conexión
    dao.conn.cerrarConexion()