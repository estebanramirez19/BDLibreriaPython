# Esteban Andres Ramirez Gonzalez
# Inacap Ingenieria en informatica - Vespertino
# Programación Orientada a Objeto Seguro (TI3V21/V-IEI-N2-P3-C1/V Puente Alto IEI)

from Controller.LibrosDAO import LibroDAO
from Controller.UserDAO import UsuarioDAO


# --- Funciones CRUD para Libros ---

def registrar_libro(): 
    print("\n--- Registrar Nuevo Libro ---")
    dao = LibroDAO()

    # Funciones auxiliares para obtener entradas válidas (sin cambios)
    def get_int_input(prompt):
        while True:
            try:
                value = int(input(prompt))
                return value
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero.")

    def get_float_input(prompt):
        while True:
            try:
                value = float(input(prompt))
                return value
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número (decimal si es necesario).")

    # Recopilación de datos sin pedir el ID
    nombre = input("Ingrese el nombre del libro: ").strip().capitalize()
    precio = get_float_input("Ingrese el precio: $")
    genero = input("Ingrese el genero del libro: ").strip().capitalize()
    tipo_tapa = input("Ingrese el tipo de tapa (ej: Dura, Blanda): ").strip().capitalize()
    paginas = get_int_input("Ingrese la cantidad de páginas: ")
    autor = input("Ingrese el nombre del autor: ").strip().title()
    stock = get_int_input("Ingrese la cantidad en stock: ")

    # Llamar al método agregarLibro de tu DAO (sin pasar el ID)
    if dao.agregarLibro(nombre, precio, genero, tipo_tapa, paginas, autor, stock):
        print(f"Libro '{nombre}' registrado exitosamente con ID automático.")
    else:
        print(f"No se pudo registrar el libro '{nombre}'. Consulte los logs para más detalles.")


def listar_libros():
    dao = LibroDAO()
    dao.listarLibros()


def buscar_libro():
    print("\n--- Buscar Libros por Nombre ---")
    dao = LibroDAO()

    fragmento = input("Ingrese el nombre o fragmento del nombre del libro a buscar: ").strip()

    if not fragmento:
        print("No se ingresó ningún fragmento para buscar.")
        return

    libros = dao.buscarLibrosPorNombre(fragmento)

def actualizar_libro():
    print("\n--- Editar Libro Completo ---")
    dao = LibroDAO()

    # Funciones auxiliares para obtener entradas válidas (las mismas que en registrar_libro)
    def get_int_input(prompt):
        while True:
            try:
                value = int(input(prompt))
                return value
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero.")

    def get_float_input(prompt):
        while True:
            try:
                value = float(input(prompt))
                return value
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número (decimal si es necesario).")

    # 1. Pedir el ID del libro a editar
    id_a_editar = get_int_input("Ingrese el ID del libro que desea editar: ")


    print(f"\nIngrese los NUEVOS datos para el libro con ID '{id_a_editar}':")

    # 2. Recopilar todos los nuevos datos
    nuevo_nombre = input("Ingrese el nuevo nombre del libro: ").strip().capitalize()
    nuevo_precio = get_float_input("Ingrese el nuevo precio: $")
    nuevo_genero = input("Ingrese el nuevo genero del libro: ").strip().capitalize()
    nuevo_tipo_tapa = input("Ingrese el nuevo tipo de tapa (ej: Dura, Blanda): ").strip().capitalize()
    nuevas_paginas = get_int_input("Ingrese la nueva cantidad de páginas: ")
    nuevo_autor = input("Ingrese el nuevo nombre del autor: ").strip().title() # .title() para nombres compuestos
    nuevo_stock = get_int_input("Ingrese la nueva cantidad en stock: ")

    # 3. Crear el diccionario de nuevos datos
    nuevos_datos = {
        "NombreLibro": nuevo_nombre, 
        "Precio": nuevo_precio,
        "Genero": nuevo_genero,
        "TipoDeTapa": nuevo_tipo_tapa,
        "Paginas": nuevas_paginas,
        "Autor": nuevo_autor,
        "Stock": nuevo_stock
    }

    # 4. Llamar al método actualizarLibro del DAO
    if dao.actualizarLibro(id_a_editar, nuevos_datos):
        print(f"Edición del libro con ID '{id_a_editar}' completada.")
    else:
        print(f"No se pudo editar el libro con ID '{id_a_editar}'.")
   
def eliminar_libro_id():
    print("\n--- Eliminar Libro ---")
    dao = LibroDAO()

    # Función auxiliar para obtener un ID válido
    def get_int_input(prompt):
        while True:
            try:
                value = int(input(prompt))
                return value
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero para el ID.")

    id_a_eliminar = get_int_input("Ingrese el ID del libro que desea eliminar: ")

    # Confirmación opcional (buena práctica para eliminaciones)
    confirmacion = input(f"¿Está seguro que desea eliminar el libro con ID '{id_a_eliminar}'? (s/n): ").lower().strip()

    if confirmacion == 's':
        if dao.eliminarLibroId(id_a_eliminar):
            print(f"Operación de eliminación para el libro con ID '{id_a_eliminar}' completada.")
        else:
            print(f"No se pudo eliminar el libro con ID '{id_a_eliminar}'.")
    else:
        print("Eliminación cancelada.")

def eliminar_libro_nombre():
    print("\n--- Eliminar Libro ---")
    dao = LibroDAO()

    nombre_eliminar = str(input("Ingrese el nombre del libro que desea eliminar: ")).strip().capitalize()

    # Confirmación opcional (buena práctica para eliminaciones)
    confirmacion = input(f"¿Está seguro que desea eliminar el libro '{nombre_eliminar}'? (s/n): ").lower().strip()

    if confirmacion == 's':
        if dao.eliminarLibroNombre(nombre_eliminar):
            print(f"Operación de eliminación para el libro '{nombre_eliminar}' completada.")
        else:
            print(f"No se pudo eliminar el libro '{nombre_eliminar}'.")
    else:
        print("Eliminación cancelada.")

def registrar_usuario():
    print("Resgitar Usuario")
    dao = UsuarioDAO()

    usuario = str(input("Ingrese un nombre de usuario: ")).strip().lower()
    nombre_u = str(input("Ingrese su nombre: ")).strip().capitalize()
    apellido_u = str(input("Ingrese su apellido: ")).strip().capitalize()
    email = str(input("Ingrese su Email: ")).strip().lower()
    contraseña = str(input("Ingrese una contraseña: "))
    estado = True

    dao.agregarUsuario(usuario, nombre_u, apellido_u, email, contraseña, estado)




def listar_usuarios():
    print("Listando usuarios")
    dao = UsuarioDAO()
    dao.listarUsuarios()
   

# --- Funciones para el Carrito de Compras ---

def agregar_al_carrito():
    pass
   
        
    listar_libros()
    pass
    

def ver_carrito():
    pass

# --- Menú Principal ---
def mostrar_menu_principal():
    """Muestra el menú principal de la aplicación."""
    print("\n--- MENU PRINCIPAL ---")
    print(" 1.- Registrar libro")
    print(" 2.- Listar libros")
    print(" 3.- Buscar libro")
    print(" 4.- Actualizar libro")
    print(" 5.- Eliminar libro")
    print(" 6.- Registrar usuario")
    print(" 7.- Listar usuarios")
    print(" 8.- Agregar libro al carrito")
    print(" 9.- Ver carrito de usuario")
    print("10.- Salir")

def main():
    """Función principal que ejecuta el programa."""
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_libro()
        elif opcion == '2':
            listar_libros()
        elif opcion == '3':
            buscar_libro()
        elif opcion == '4':
            actualizar_libro()
        elif opcion == '5':
            eliminar_libro()
        elif opcion == '6':
            registrar_usuario()
        elif opcion == '7':
            listar_usuarios()
        elif opcion == '8':
            agregar_al_carrito()
        elif opcion == '9':
            ver_carrito()
        elif opcion == '10':
            print("¡Gracias por usar la tienda de libros online! ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
    