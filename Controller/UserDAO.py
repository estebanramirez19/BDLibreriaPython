# Esteban Andres Ramirez Gonzalez
# Inacap Ingenieria en informatica - Vespertino
# Base de datos no relacionales

from Database.Conexion import Conexion
from pymongo.errors import PyMongoError

# **Clase AutorDAO corregida:**
class UsuarioDAO:
    def __init__(self):
        self.conn = Conexion() # Instancia de tu clase de conexión
        self.collection = self.conn.obtenerConexion()["Usuarios"] # Accede a la colección 'Usuarios'

    def obtener_siguiente_id(self):
        """
        Obtiene el siguiente ID autoincremental buscando el ID más alto existente
        en la colección 'Usuarios' y sumándole 1. Si no hay libros, empieza en 1.
        """
        try:
            ultimo_usuario = self.collection.find_one(sort=[("ID_usuario", -1)])
            if ultimo_usuario and "ID_usuario" in ultimo_usuario:
                return ultimo_usuario["ID_usuario"] + 1
            else:
                return 1
        except Exception as e:
            print(f"Error al obtener el siguiente ID: {e}")
            return None
        
    def agregarUsuario(self, usuario, nombre_u, apellido_u, email, contraseña, estado):
        try:
            # 1. Obtener el siguiente ID autoincremental para el usuario
            nuevo_id_usuario = self.obtener_siguiente_id() # Asegúrate de que este método existe y es correcto
            if nuevo_id_usuario is None:
                print("No se pudo generar un ID para el nuevo usuario.")
                return False

            document = {
                "ID_usuario": nuevo_id_usuario, # Usamos el ID generado
                "Usuario": usuario,
                "Nombre": nombre_u,
                "Apellido": apellido_u,
                "Email": email,
                "Contraseña": contraseña,
                "Estado" : estado
            }

            result = self.collection.insert_one(document)

            if result.inserted_id:
                print(f"Usuario '{usuario}' con ID '{nuevo_id_usuario}' agregado correctamente. MongoDB _id: {result.inserted_id}")
                return True
            else:
                print(f"Error desconocido al agregar el Usuario '{usuario}'.")
                return False
        except PyMongoError as ex:
            # Primero captura los errores específicos de PyMongo
            print(f"Error de base de datos (PyMongo) al agregar Usuario: {ex}")
            return False
        except Exception as ex:
            # Luego captura cualquier otro error general
            print(f"Ocurrió un error inesperado al agregar el Usuario: {ex}")
            return False

    def listarUsuarios(self):
        """
        Lista todos los Usuarios disponibles en la colección.
        Retorna una lista de diccionarios, donde cada diccionario es un usuario.
        """
        try:
            # El método find({}) sin argumentos recupera todos los documentos de la colección.
            # Convertimos el cursor a una lista para poder trabajar con los resultados.
            usuarios = list(self.collection.find({"Estado":True}))
            
            if usuarios:
                print("\n--- Listado de usuarios ---")
                for usuario in usuarios:
                    # Imprimimos los detalles de cada usuario.
                    # Puedes formatear esto como prefieras.
                    print(f"ID: {usuario.get('ID_usuario', 'N/A')}")
                    print(f"  Usuario: {usuario.get('Usuario', 'N/A')}")
                    print(f"  Nombre: {usuario.get('Nombre', 'N/A')}")
                    print(f"  Apellido: ${usuario.get('Apellido', 'N/A')}")
                    print(f"  Email: {usuario.get('Email', 'N/A')}")
                    print(f"  Contraseña: {usuario.get('Contraseña', 'N/A')}")
                    print("-------------------------")
                return usuarios
            else:
                print("No se encontraron Usuarios en la base de datos.")
                return []
        except Exception as e:
            print(f"Ocurrió un error al listar los Usuarios: {e}")
            return []
        
    def usuariosEliminados(self):
        """
        Lista todos los Usuarios eliminados en la colección.
        Retorna una lista de diccionarios, donde cada diccionario es un usuario.
        """
        try:
            # El método find({}) sin argumentos recupera todos los documentos de la colección.
            # Convertimos el cursor a una lista para poder trabajar con los resultados.
            usuarios = list(self.collection.find({"Estado":False}))
            
            if usuarios:
                print("\n--- Listado de usuarios ---")
                for usuario in usuarios:
                    # Imprimimos los detalles de cada usuario.
                    # Puedes formatear esto como prefieras.
                    print(f"ID: {usuario.get('ID_usuario', 'N/A')}")
                    print(f"  Usuario: {usuario.get('Usuario', 'N/A')}")
                    print(f"  Nombre: {usuario.get('Nombre', 'N/A')}")
                    print(f"  Apellido: ${usuario.get('Apellido', 'N/A')}")
                    print(f"  Email: {usuario.get('Email', 'N/A')}")
                    print(f"  Contraseña: {usuario.get('Contraseña', 'N/A')}")
                    print("-------------------------")
                return usuarios
            else:
                print("No se encontraron Usuarios en la base de datos.")
                return []
        except Exception as e:
            print(f"Ocurrió un error al listar los Usuarios: {e}")
            return []


        
    def eliminar_usuario(self,id_usuario,interruptor):
        """
        Actualiza un libro existente en la colección.
        """
        try:
            filtro = {"ID": id_usuario}
            actualizacion = {"$set": interruptor} # Aquí es donde se usan todos los nuevos_datos

            result = self.collection.update_one(filtro, actualizacion)

            if result.matched_count > 0:
                if result.modified_count > 0:
                    print(f"Usuario con ID '{id_usuario}' actualizado correctamente.")
                    return True
                else:
                    print(f"Usuario con ID '{id_usuario}' encontrado, pero no se realizaron cambios (los datos son los mismos).")
                    return True # Consideramos éxito si no hay cambios, pero se encontró
            else:
                print(f"No se encontró ningún libro con ID '{id_usuario}'.")
                return False

        except Exception as e:
            print(f"Ocurrió un error al actualizar el libro con ID '{id_usuario}': {e}")
            return False
        
    def actualizarUsuario(self, id_usuario, nuevos_datos):
        """
        Actualiza un libro existente en la colección.
        """
        try:
            filtro = {"ID": id_usuario}
            actualizacion = {"$set": nuevos_datos} # Aquí es donde se usan todos los nuevos_datos

            result = self.collection.update_one(filtro, actualizacion)

            if result.matched_count > 0:
                if result.modified_count > 0:
                    print(f"Usuario con ID '{id_usuario}' actualizado correctamente.")
                    return True
                else:
                    print(f"Usuario con ID '{id_usuario}' encontrado, pero no se realizaron cambios (los datos son los mismos).")
                    return True # Consideramos éxito si no hay cambios, pero se encontró
            else:
                print(f"No se encontró ningún usuario con ID '{id_usuario}'.")
                return False

        except Exception as e:
            print(f"Ocurrió un error al actualizar el usuario con ID '{id_usuario}': {e}")
            return False
