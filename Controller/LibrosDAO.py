# Esteban Andres Ramirez Gonzalez
# Inacap Ingenieria en informatica - Vespertino
# Base de datos no relacionales

from Database.Conexion import Conexion
from pymongo.errors import PyMongoError
import re 

class LibroDAO:
    def __init__(self):
        self.conn = Conexion() # Instancia de tu clase de conexión
        self.collection = self.conn.obtenerConexion()["Libros"] # Accede a la colección 'libros'

    def obtener_siguiente_Id(self):
        """
        Obtiene el siguiente Id autoincremental buscando el Id más alto existente
        en la colección 'libros' y sumándole 1. Si no hay libros, empieza en 1.
        """
        try:
            ultimo_libro = self.collection.find_one(sort=[("Id", -1)])
            if ultimo_libro and "Id" in ultimo_libro:
                return ultimo_libro["Id"] + 1
            else:
                return 1
        except Exception as e:
            print(f"Error al obtener el siguiente Id: {e}")
            return None

    def agregarLibro(self, nombre, precio, genero, tipo_tapa, paginas, autor, stock):
        """
        Agrega un nuevo libro a la colección con un Id autoincremental.
        """
        try:
            nuevo_Id = self.obtener_siguiente_Id()
            if nuevo_Id is None:
                print("No se pudo generar un Id para el nuevo libro.")
                return False

            document = {
                "Id": nuevo_Id,
                "Nombre": nombre,
                "Precio": precio,
                "Genero": genero,
                "Tapa": tipo_tapa,
                "Paginas": paginas,
                "Autor": autor,
                "Stock": stock
            }
            result = self.collection.insert_one(document)
            if result.inserted_Id:
                print(f"Libro '{nombre}' con Id '{nuevo_Id}' agregado correctamente. MongoDB _Id: {result.inserted_Id}")
                return True
            else:
                print(f"Error desconocIdo al agregar el Libro '{nombre}'.")
                return False
        except Exception as e:
            print(f"Ocurrió un error al agregar el libro: {e}")
            return False

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
                    print(f"Id: {libro.get('Id', 'N/A')}")
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
        
    def eliminarLibroId(self, Id_libro):
        """
        Elimina un libro de la colección por su Id.
        """
        try:
            # 1. Definir el filtro para encontrar el documento a eliminar
            filtro = {"Id": Id_libro}

            # 2. Ejecutar la operación de eliminación
            # delete_one elimina el primer documento que coincIde con el filtro
            result = self.collection.delete_one(filtro)

            # 3. Verificar el resultado de la eliminación
            if result.deleted_count > 0:
                print(f"Libro con Id '{Id_libro}' eliminado correctamente.")
                return True
            else:
                print(f"No se encontró ningún libro con Id '{Id_libro}' para eliminar.")
                return False

        except Exception as e:
            print(f"Ocurrió un error al eliminar el libro con Id '{Id_libro}': {e}")
            return False
        
    def eliminarLibroNombre(self,nombre):
        """
        Elimina un libro de la colección por su Nombre.
        """
        try:
            # 1. Definir el filtro para encontrar el documento a eliminar
            filtro = {"Nombre": nombre}

            # 2. Ejecutar la operación de eliminación
            # delete_one elimina el primer documento que coincIde con el filtro
            result = self.collection.delete_one(filtro)

            # 3. Verificar el resultado de la eliminación
            if result.deleted_count > 0:
                print(f"Libro '{nombre}' eliminado correctamente.")
                return True
            else:
                print(f"No se encontró ningún libro con Id '{nombre}' para eliminar.")
                return False

        except Exception as e:
            print(f"Ocurrió un error al eliminar el libro con Id '{nombre}': {e}")
            return False

    def actualizarLibro(self, Id_libro, nuevos_datos):
        """
        Actualiza un libro existente en la colección.
        """
        try:
            filtro = {"Id": Id_libro}
            actualizacion = {"$set": nuevos_datos} # Aquí es donde se usan todos los nuevos_datos

            result = self.collection.update_one(filtro, actualizacion)

            if result.matched_count > 0:
                if result.modified_count > 0:
                    print(f"Libro con Id '{Id_libro}' actualizado correctamente.")
                    return True
                else:
                    print(f"Libro con Id '{Id_libro}' encontrado, pero no se realizaron cambios (los datos son los mismos).")
                    return True # ConsIderamos éxito si no hay cambios, pero se encontró
            else:
                print(f"No se encontró ningún libro con Id '{Id_libro}'.")
                return False

        except Exception as e:
            print(f"Ocurrió un error al actualizar el libro con Id '{Id_libro}': {e}")
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
                    print(f"Id: {libro.get('Id', 'N/A')}")
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

    def buscarLibros(self, tipo, nombre):
        """
        Busca libros en la colección que contengan el fragmento_nombre
        en su campo 'Nombre libro', ignorando mayúsculas y minúsculas.
        """
        try:
            query = {tipo: {"$regex": re.compile(nombre, re.IGNORECASE)}}

            libros_encontrados = list(self.collection.find(query))

            if libros_encontrados:
                print(f"\n--- Libros encontrados con '{nombre}' ---")
                for libro in libros_encontrados:
                    print(f"Id: {libro.get('Id', 'N/A')}")
                    print(f"  Nombre: {libro.get('Nombre libro', 'N/A')}")
                    print(f"  Autor: {libro.get('Autor', 'N/A')}")
                    print(f"  Precio: ${libro.get('Precio', 'N/A')}")
                    print(f"  Género: {libro.get('Genero', 'N/A')}")
                    print(f"  Tapa: {libro.get('Tipo de tapa', 'N/A')}")
                    print(f"  Páginas: {libro.get('Paginas', 'N/A')}")
                    print(f"  Stock: {libro.get('Stock', 'N/A')}")
                    print("-------------------------")
                return libros_encontrados
            else:
                print(f"No se encontraron libros que contengan '{nombre}' en su nombre.")
                return []
        except Exception as e:
            print(f"Ocurrió un error al buscar libros por nombre: {e}")
            return []        

