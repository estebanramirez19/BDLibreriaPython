# Esteban Andres Ramirez Gonzalez
# Inacap Ingenieria en informatica - Vespertino
# Base de datos no relacionales

from Database.Conexion import Conexion
from pymongo.errors import PyMongoError

# **Clase AutorDAO corregida:**
class LibroDAO:
    def __init__(self):
        self.conn = Conexion() # Instancia de tu clase de conexión
        self.collection = self.conn.obtenerConexion()["Libros"] # Accede a la colección 'libros'

    def agregarLibro(self, id, nombre, precio, genero, tipo_tapa, paginas, autor, stock):
        try:
            # Aquí es donde asignas las variables directamente a las claves del diccionario
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
            # En DAO's pequeños, no siempre necesitas cerrar la conexión aquí.
            # El pool de conexiones de PyMongo es eficiente.
            # Cierras la conexión cuando tu aplicación termina, no en cada operación.
            # self.conn.cerrarConexion() # Esto cerraría la conexión después de cada operación, lo cual es ineficiente.
            pass # No cerramos la conexión aquí. Se gestiona por la instancia de Conexion.

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
        
