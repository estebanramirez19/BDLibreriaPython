# Esteban Andres Ramirez Gonzalez
# Inacap Ingenieria en informatica - Vespertino
# Programación Orientada a Objeto Seguro (TI3V21/V-IEI-N2-P3-C1/V Puente Alto IEI)

from Controller.LibrosDAO import LibroDAO
from Controller.UserDAO import UsuarioDAO 

# --- Entrada de Datos ---

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


# --- Funciones CRUD para Libros ---

def registrar_libro():
    print("\n--- Registrar Nuevo Libro ---")
    dao = LibroDAO()

    nombre = input("Ingrese el nombre del libro: ").strip().capitalize()
    precio = get_float_input("Ingrese el precio: $")
    genero = input("Ingrese el genero del libro: ").strip().capitalize()
    tipo_tapa = input("Ingrese el tipo de tapa (ej: Dura, Blanda): ").strip().capitalize()
    paginas = get_int_input("Ingrese la cantidad de páginas: ")
    autor = input("Ingrese el nombre del autor: ").strip().title()
    stock = get_int_input("Ingrese la cantidad en stock: ")

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
    # El método buscarLibrosPorNombre ya imprime los resultados.

def actualizar_libro():
    print("\n--- Editar Libro Completo ---")
    dao = LibroDAO()

    id_a_editar = get_int_input("Ingrese el ID del libro que desea editar: ")

    print(f"\nIngrese los NUEVOS datos para el libro con ID '{id_a_editar}':")

    # Recopilar todos los nuevos datos
    nuevo_nombre = input("Ingrese el nuevo nombre del libro: ").strip().capitalize()
    nuevo_precio = get_float_input("Ingrese el nuevo precio: $")
    nuevo_genero = input("Ingrese el nuevo genero del libro: ").strip().capitalize()
    nuevo_tipo_tapa = input("Ingrese el nuevo tipo de tapa (ej: Dura, Blanda): ").strip().capitalize()
    nuevas_paginas = get_int_input("Ingrese la nueva cantidad de páginas: ")
    nuevo_autor = input("Ingrese el nuevo nombre del autor: ").strip().title()
    nuevo_stock = get_int_input("Ingrese la nueva cantidad en stock: ")

    # Asegúrate de que las claves del diccionario coincidan EXACTAMENTE con los nombres de tus campos en MongoDB
    nuevos_datos = {
        "Nombre libro": nuevo_nombre, # Corregido: "Nombre libro"
        "Precio": nuevo_precio,
        "Genero": nuevo_genero,
        "Tipo de tapa": nuevo_tipo_tapa, # Corregido: "Tipo de tapa"
        "Paginas": nuevas_paginas,
        "Autor": nuevo_autor,
        "Stock": nuevo_stock
    }

    if dao.actualizarLibro(id_a_editar, nuevos_datos):
        print(f"Edición del libro con ID '{id_a_editar}' completada.")
    else:
        print(f"No se pudo editar el libro con ID '{id_a_editar}'.")

# Se sacan estas funciones de eliminar_libro para poder llamarlas directamente desde el menú
def eliminar_libro_id():
    print("\n--- Eliminar Libro por ID ---")
    dao = LibroDAO()

    id_a_eliminar = get_int_input("Ingrese el ID del libro que desea eliminar: ")

    confirmacion = input(f"¿Está seguro que desea eliminar el libro con ID '{id_a_eliminar}'? (s/n): ").lower().strip()

    if confirmacion == 's':
        # Asumo que tu DAO tiene un método eliminarLibro o eliminarLibroById
        if dao.eliminarLibro(id_a_eliminar): # Usamos el nombre que ya se sugirió: eliminarLibro
            print(f"Operación de eliminación para el libro con ID '{id_a_eliminar}' completada.")
        else:
            print(f"No se pudo eliminar el libro con ID '{id_a_eliminar}'.")
    else:
        print("Eliminación de libro cancelada.")

def eliminar_libro_nombre():
    print("\n--- Eliminar Libro por Nombre ---")
    dao = LibroDAO()

    nombre_eliminar = input("Ingrese el nombre del libro que desea eliminar: ").strip().capitalize()

    confirmacion = input(f"¿Está seguro que desea eliminar el libro '{nombre_eliminar}'? (s/n): ").lower().strip()

    if confirmacion == 's':
        # Asumo que tu DAO tiene un método eliminarLibroNombre
        if dao.eliminarLibroNombre(nombre_eliminar): # Asegúrate de tener este método en LibroDAO
            print(f"Operación de eliminación para el libro '{nombre_eliminar}' completada.")
        else:
            print(f"No se pudo eliminar el libro '{nombre_eliminar}'.")
    else:
        print("Eliminación de libro cancelada.")

def eliminar_libro():
    """Función para elegir el método de eliminación de libros."""
    print("\n--- Eliminar Libro ---")
    while True:
        op = input("Seleccione \n1.- Eliminar libro por ID \n2.- Eliminar libro por nombre \n3.- Volver al menú principal\nSu opción: ")
        if op == '1':
            eliminar_libro_id()
            break
        elif op == '2':
            eliminar_libro_nombre()
            break
        elif op == '3':
            break
        else:
            print("Opción no válida. Por favor, seleccione 1, 2 o 3.")


# --- Funciones CRUD para Usuarios ---

def registrar_usuario():
    print("\n--- Registrar Usuario ---")
    dao = UsuarioDAO()

    usuario = input("Ingrese un nombre de usuario: ").strip().lower()
    nombre_u = input("Ingrese su nombre: ").strip().capitalize()
    apellido_u = input("Ingrese su apellido: ").strip().capitalize()
    email = input("Ingrese su Email: ").strip().lower()
    contraseña = input("Ingrese una contraseña: ") # Contraseña como string
    estado = True # Por defecto, un nuevo usuario está activo

    # Asumo que tu DAO tiene un método agregarUsuario con los parámetros correctos
    if dao.agregarUsuario(usuario, nombre_u, apellido_u, email, contraseña, estado):
        print(f"Usuario '{usuario}' registrado exitosamente con ID automático.")
    else:
        print(f"No se pudo registrar el usuario '{usuario}'. Consulte los logs para más detalles.")

def actualizar_usuario():
    print("\n--- Editar Usuario ---")
    dao = UsuarioDAO()

    # Se corrige el prompt para que sea de usuario, no de libro
    id_a_editar = get_int_input("Ingrese el ID del usuario que desea editar: ")

    print(f"\nIngrese los NUEVOS datos para el usuario con ID '{id_a_editar}':")

    nuevo_usuario = input("Ingrese un nuevo nombre de usuario: ").strip().lower() # Se usa .lower() para usuario
    nuevo_nombre = input("Ingrese un nuevo nombre: ").strip().capitalize()
    nuevo_apellido = input("Ingrese un nuevo apellido: ").strip().capitalize()
    nuevo_email = input("Ingrese el nuevo Email: ").strip().lower()
    nueva_contraseña = input("Ingrese la nueva contraseña: ") # Contraseña como string

    nuevos_datos = {
        "Usuario": nuevo_usuario,
        "Nombre": nuevo_nombre,
        "Apellido": nuevo_apellido,
        "Email": nuevo_email,
        "Contraseña": nueva_contraseña
    }

    # Asegúrate de que tu UsuarioDAO tenga un método 'actualizarUsuario'
    if dao.actualizarUsuario(id_a_editar, nuevos_datos):
        print(f"Edición del usuario con ID '{id_a_editar}' completada.")
    else:
        print(f"No se pudo editar el usuario con ID '{id_a_editar}'.")


def listar_usuarios():
    dao = UsuarioDAO()
    # Asumo que dao.listarUsuarios() ya filtra por estado True si es lo que deseas mostrar por defecto.
    dao.listarUsuarios()

def listar_usuarios_eliminados():
    dao = UsuarioDAO()
    # Asumo que tienes este método en UsuarioDAO para listar usuarios con Estado=False
    dao.usuariosEliminados()

def eliminar_usuario():
    print("\n--- Desactivar/Eliminar Usuario (Cambiar Estado) ---")
    dao = UsuarioDAO() # ¡Correcto, usar UsuarioDAO aquí!

    id_a_modificar = get_int_input("Ingrese el ID del usuario que desea desactivar/eliminar: ")

    confirmacion = input(f"¿Está seguro que desea DESACTIVAR el usuario con ID '{id_a_modificar}'? (s/n): ").lower().strip()

    if confirmacion == "s":
        # Cambiar el estado a False (desactivar)
        cambio_estado = {
            "Estado": False
        }

        # Asumo que UsuarioDAO tiene un método actualizarUsuario
        if dao.actualizarUsuario(id_a_modificar, cambio_estado): # Aquí usas actualizarUsuario
            print(f"La cuenta con ID '{id_a_modificar}' ha sido desactivada correctamente.")
        else:
            print(f"No se pudo desactivar la cuenta con ID '{id_a_modificar}'.")
    else:
        print("Operación de desactivación de cuenta cancelada.")

# La función editar_usuario estaba duplicada o vacía, la eliminamos si no se usa para algo específico
# o la renombramos si es para algo diferente a actualizar_usuario.
# def editar_usuario():
#     pass


# --- Menú Principal ---
def mostrar_menu_principal():
    """Muestra el menú principal de la aplicación."""
    print("\n--- MENU PRINCIPAL ---")
    print(" 1.- Libros: Registrar")
    print(" 2.- Libros: Listar")
    print(" 3.- Libros: Buscar por Nombre")
    print(" 4.- Libros: Actualizar")
    print(" 5.- Libros: Eliminar") # Ahora te permite elegir ID o Nombre
    print("-------------------------")
    print(" 6.- Usuarios: Registrar")
    print(" 7.- Usuarios: Listar Activos")
    print(" 8.- Usuarios: Listar Eliminados/Inactivos") # Nueva opción
    print(" 9.- Usuarios: Actualizar") # Nueva opción para editar usuario
    print("10.- Usuarios: Desactivar/Eliminar (cambiar estado)") # Nueva opción
    print("-------------------------")
    print("11.- Salir") # Opción Salir ajustada

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
            eliminar_libro() # Llama a la función que te da a elegir ID o Nombre
        elif opcion == '6':
            registrar_usuario()
        elif opcion == '7':
            listar_usuarios()
        elif opcion == '8': 
            listar_usuarios_eliminados()
        elif opcion == '9':
            actualizar_usuario()
        elif opcion == '10': 
            eliminar_usuario()
        elif opcion == '11':
            print("¡Gracias por usar la tienda de libros online! ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()