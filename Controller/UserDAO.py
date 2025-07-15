# Esteban Andres Ramirez Gonzalez
# Inacap Ingenieria en informatica - Vespertino
# Base de datos no relacionales

from Database.Conexion import Conexion
from pymongo.errors import PyMongoError

# **Clase AutorDAO corregida:**
class UsuarioDAO:
    def __init__(self):
        self.conn = Conexion() # Instancia de tu clase de conexión
        self.collection = self.conn.obtenerConexion()["Usuarios"] # Accede a la colección 'libros'

    def agregarUsuario(self, id_u, usuario, nombre_u, apellido_u, email, contraseña, estado):
        try:
            # Aquí es donde asignas las variables directamente a las claves del diccionario
            document = {
                "ID_usuario": id_u,
                "Usuario": usuario,
                "Nombre": nombre_u,
                "Apellido": apellido_u,
                "Email": email,
                "Contraseña": contraseña,
                "Estado" : estado
            }

            # Insertar el documento en la colección
            result = self.collection.insert_one(document)

            # Verificar el resultado de la inserción
            if result.inserted_id:
                print(f"Usuario '{usuario}' con ID '{id_u}' agregado correctamente. MongoDB _id: {result.inserted_id}")
                return True # Indica éxito
            else:
                print(f"Error desconocido al agregar el Usuario '{usuario}'.")
                return False # Indica fallo
        except Exception as e:
            print(f"Ocurrió un error al agregar el Usuario: {e}")
            return False

        except PyMongoError as ex:
            # Captura errores específicos de PyMongo (ej. duplicados si usas _id)
            print(f"Error de PyMongo al agregar Usuario: {ex}")
            return False
        except Exception as ex:
            # Captura cualquier otro error inesperado
            print(f"Error inesperado al agregar Usuario: {ex}")
            return False
        finally:
            # En DAO's pequeños, no siempre necesitas cerrar la conexión aquí.
            # El pool de conexiones de PyMongo es eficiente.
            # Cierras la conexión cuando tu aplicación termina, no en cada operación.
            # self.conn.cerrarConexion() # Esto cerraría la conexión después de cada operación, lo cual es ineficiente.
            pass # No cerramos la conexión aquí. Se gestiona por la instancia de Conexion.
