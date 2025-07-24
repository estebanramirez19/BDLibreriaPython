# Esteban Andres Ramirez Gonzalez
# Inacap Ingenieria en informatica - Vespertino
# Base de datos no relacionales

from Database.Conexion import Conexion
from pymongo.errors import PyMongoError

# **Clase AutorDAO corregIda:**
class UsuarioDAO:
    def __init__(self):
        self.conn = Conexion() 
        self.collection = self.conn.obtenerConexion()["Usuarios"] 

    def obtener_siguiente_Id(self):
        """
        Obtiene el siguiente Id autoincremental buscando el Id más alto existente
        en la colección 'Usuarios' y sumándole 1. Si no hay libros, empieza en 1.
        """
        try:
            ultimo_usuario = self.collection.find_one(sort=[("Id_usuario", -1)])
            if ultimo_usuario and "Id_usuario" in ultimo_usuario:
                return ultimo_usuario["Id_usuario"] + 1
            else:
                return 1
        except Exception as e:
            print(f"Error al obtener el siguiente Id: {e}")
            return None
        
    def agregarUsuario(self, usuario, nombre_u, apellIdo_u, email, contraseña, estado):
        try:
            # 1. Obtener el siguiente Id autoincremental para el usuario
            nuevo_Id_usuario = self.obtener_siguiente_Id() 
            if nuevo_Id_usuario is None:
                print("No se pudo generar un Id para el nuevo usuario.")
                return False

            document = {
                "Id_usuario": nuevo_Id_usuario,
                "Usuario": usuario,
                "Nombre": nombre_u,
                "Apellido": apellIdo_u,
                "Email": email,
                "Contraseña": contraseña,
                "Estado" : estado
            }

            result = self.collection.insert_one(document)

            if result.inserted_Id:
                print(f"Usuario '{usuario}' con Id '{nuevo_Id_usuario}' agregado correctamente. MongoDB _Id: {result.inserted_Id}")
                return True
            else:
                print(f"Error desconocIdo al agregar el Usuario '{usuario}'.")
                return False
        except PyMongoError as ex:
            print(f"Error de base de datos (PyMongo) al agregar Usuario: {ex}")
            return False
        except Exception as ex:
            print(f"Ocurrió un error inesperado al agregar el Usuario: {ex}")
            return False

    def listarUsuarios(self):
        """
        Lista todos los Usuarios disponibles en la colección.
        Retorna una lista de diccionarios, donde cada diccionario es un usuario.
        """
        try:
            usuarios = list(self.collection.find({"Estado":True}))
            
            if usuarios:
                print("\n--- Listado de usuarios ---")
                for usuario in usuarios:
                    print(f"Id: {usuario.get('Id_usuario', 'N/A')}")
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
            usuarios = list(self.collection.find({"Estado":False}))
            
            if usuarios:
                print("\n--- Listado de usuarios ---")
                for usuario in usuarios:
                    print(f"Id: {usuario.get('Id_usuario', 'N/A')}")
                    print(f"  Usuario: {usuario.get('Usuario', 'N/A')}")
                    print(f"  Nombre: {usuario.get('Nombre', 'N/A')}")
                    print(f"  ApellIdo: ${usuario.get('ApellIdo', 'N/A')}")
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


        
    def eliminar_usuario(self,Id_usuario,interruptor):
        """
        Actualiza un libro existente en la colección.
        """
        try:
            filtro = {"Id": Id_usuario}
            actualizacion = {"$set": interruptor} # Aquí es donde se usan todos los nuevos_datos

            result = self.collection.update_one(filtro, actualizacion)

            if result.matched_count > 0:
                if result.modified_count > 0:
                    print(f"Usuario con Id '{Id_usuario}' actualizado correctamente.")
                    return True
                else:
                    print(f"Usuario con Id '{Id_usuario}' encontrado, pero no se realizaron cambios (los datos son los mismos).")
                    return True 
            else:
                print(f"No se encontró ningún libro con Id '{Id_usuario}'.")
                return False

        except Exception as e:
            print(f"Ocurrió un error al actualizar el libro con Id '{Id_usuario}': {e}")
            return False
        
    def actualizarUsuario(self, Id_usuario, nuevos_datos):
        """
        Actualiza un libro existente en la colección.
        """
        try:
            filtro = {"Id": Id_usuario}
            actualizacion = {"$set": nuevos_datos} # Aquí es donde se usan todos los nuevos_datos

            result = self.collection.update_one(filtro, actualizacion)

            if result.matched_count > 0:
                if result.modified_count > 0:
                    print(f"Usuario con Id '{Id_usuario}' actualizado correctamente.")
                    return True
                else:
                    print(f"Usuario con Id '{Id_usuario}' encontrado, pero no se realizaron cambios (los datos son los mismos).")
                    return True 
            else:
                print(f"No se encontró ningún usuario con Id '{Id_usuario}'.")
                return False

        except Exception as e:
            print(f"Ocurrió un error al actualizar el usuario con Id '{Id_usuario}': {e}")
            return False
