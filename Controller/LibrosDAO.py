# Esteban Andres Ramirez Gonzalez
# Inacap Ingenieria en informatica - Vespertino
# Base de datos no relacionales

from Database.Conexion import Conexion
from pymongo.errors import PyMongoError
import re 

# **Clase AutorDAO corregida:**
class LibroDAO:
    def __init__(self):
        self.conn = Conexion() # Instancia de tu clase de conexión
        self.collection = self.conn.obtenerConexion()["Libros"] # Accede a la colección 'libros'

    def obtener_siguiente_id(self):
        """
        Obtiene el siguiente ID autoincremental buscando el ID más alto existente
        en la colección 'libros' y sumándole 1. Si no hay libros, empieza en 1.
        """
        try:
            ultimo_libro = self.collection.find_one(sort=[("ID", -1)])
            if ultimo_libro and "ID" in ultimo_libro:
                return ultimo_libro["ID"] + 1
            else:
                return 1
        except Exception as e:
            print(f"Error al obtener el siguiente ID: {e}")
            return None

    def agregarLibro(self, id, nombre, precio, genero, tipo_tapa, paginas, autor, stock):
        try:
            document = {
                "ID": id,
                "NombreLibro": nombre,
                "Precio": precio,
                "Genero": genero,
                "TipoDeTapa": tipo_tapa,
                "Paginas": paginas,
                "Autor": autor,
                "Stock": stock
            }

            # Insertar el documento en la colección
            result = self.collection.insert_one(document)

            # Verificar el resultado de la inserción
            if result.inserted_id:
                print(f"Libro '{nombre}' con ID '{id}' agregado correctamente. MongoDB _id: {result.inserted_id}")
                return True # Indica éxito
            else:
                print(f"Error desconocido al agregar el Libro '{nombre}'.")
                return False # Indica fallo
        except Exception as e:
            print(f"Ocurrió un error al agregar el libro: {e}")
            return False

        except PyMongoError as ex:
            # Captura errores específicos de PyMongo (ej. duplicados si usas _id)
            print(f"Error de PyMongo al agregar libro: {ex}")
            return False
        except Exception as ex:
            # Captura cualquier otro error inesperado
            print(f"Error inesperado al agregar libro: {ex}")
            return False
        finally:
            pass

    def listarLibros(self):
        """
        Lista todos los libros disponibles en la colección.
        Retorna una lista de diccionarios, donde cada diccionario es un libro.
        """
        try:
            # El método find({}) sin argumentos recupera todos los documentos de la colección.
            # Convertimos el cursor a una lista para poder trabajar con los resultados.
            libros = list(self.collection.find({}))
            if libros:
                print("\n--- Listado de Libros ---")
                for libro in libros:
                    # Imprimimos los detalles de cada libro.
                    # Puedes formatear esto como prefieras.
                    print(f"ID: {libro.get('ID', 'N/A')}")
                    print(f"  Nombre: {libro.get('Nombre libro', 'N/A')}")
                    print(f"  Autor: {libro.get('Autor', 'N/A')}")
                    print(f"  Precio: ${libro.get('Precio', 'N/A')}")
                    print(f"  Género: {libro.get('Genero', 'N/A')}")
                    print(f"  Tipo de Tapa: {libro.get('Tipo de tapa', 'N/A')}")
                    print(f"  Páginas: {libro.get('Paginas', 'N/A')}")
                    print("-------------------------")
                return libros
            else:
                print("No se encontraron libros en la base de datos.")
                return []
        except Exception as e:
            print(f"Ocurrió un error al listar los libros: {e}")
            return []
        
    def eliminarLibroId(self, id_libro):
        """
        Elimina un libro de la colección por su ID.
        """
        try:
            # 1. Definir el filtro para encontrar el documento a eliminar
            filtro = {"NombreLibro": id_libro}

            # 2. Ejecutar la operación de eliminación
            # delete_one elimina el primer documento que coincide con el filtro
            result = self.collection.delete_one(filtro)

            # 3. Verificar el resultado de la eliminación
            if result.deleted_count > 0:
                print(f"Libro con ID '{id_libro}' eliminado correctamente.")
                return True
            else:
                print(f"No se encontró ningún libro con ID '{id_libro}' para eliminar.")
                return False

        except Exception as e:
            print(f"Ocurrió un error al eliminar el libro con ID '{id_libro}': {e}")
            return False
        
    def eliminarLibroNombre(self,nombre ):
        """
        Elimina un libro de la colección por su Nombre.
        """
        try:
            # 1. Definir el filtro para encontrar el documento a eliminar
            filtro = {"ID": nombre}

            # 2. Ejecutar la operación de eliminación
            # delete_one elimina el primer documento que coincide con el filtro
            result = self.collection.delete_one(filtro)

            # 3. Verificar el resultado de la eliminación
            if result.deleted_count > 0:
                print(f"Libro '{nombre}' eliminado correctamente.")
                return True
            else:
                print(f"No se encontró ningún libro con ID '{nombre}' para eliminar.")
                return False

        except Exception as e:
            print(f"Ocurrió un error al eliminar el libro con ID '{nombre}': {e}")
            return False

    def actualizarLibro(self, id_libro, nuevos_datos):
        """
        Actualiza un libro existente en la colección.
        """
        try:
            filtro = {"ID": id_libro}
            actualizacion = {"$set": nuevos_datos} # Aquí es donde se usan todos los nuevos_datos

            result = self.collection.update_one(filtro, actualizacion)

            if result.matched_count > 0:
                if result.modified_count > 0:
                    print(f"Libro con ID '{id_libro}' actualizado correctamente.")
                    return True
                else:
                    print(f"Libro con ID '{id_libro}' encontrado, pero no se realizaron cambios (los datos son los mismos).")
                    return True # Consideramos éxito si no hay cambios, pero se encontró
            else:
                print(f"No se encontró ningún libro con ID '{id_libro}'.")
                return False

        except Exception as e:
            print(f"Ocurrió un error al actualizar el libro con ID '{id_libro}': {e}")
            return False

    def buscarLibrosPorNombre(self, fragmento_nombre):
        """
        Busca libros en la colección que contengan el fragmento_nombre
        en su campo 'Nombre libro', ignorando mayúsculas y minúsculas.
        """
        try:
            query = {"Nombre libro": {"$regex": re.compile(fragmento_nombre, re.IGNORECASE)}}

            libros_encontrados = list(self.collection.find(query))

            if libros_encontrados:
                print(f"\n--- Libros encontrados con '{fragmento_nombre}' ---")
                for libro in libros_encontrados:
                    print(f"ID: {libro.get('ID', 'N/A')}")
                    print(f"  Nombre: {libro.get('Nombre libro', 'N/A')}")
                    print(f"  Autor: {libro.get('Autor', 'N/A')}")
                    print(f"  Precio: ${libro.get('Precio', 'N/A')}")
                    print(f"  Género: {libro.get('Genero', 'N/A')}")
                    print(f"  Tipo de Tapa: {libro.get('Tipo de tapa', 'N/A')}")
                    print(f"  Páginas: {libro.get('Paginas', 'N/A')}")
                    print(f"  Stock: {libro.get('Stock', 'N/A')}")
                    print("-------------------------")
                return libros_encontrados
            else:
                print(f"No se encontraron libros que contengan '{fragmento_nombre}' en su nombre.")
                return []
        except Exception as e:
            print(f"Ocurrió un error al buscar libros por nombre: {e}")
            return []        


