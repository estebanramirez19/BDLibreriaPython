# Esteban Andres Ramirez Gonzalez
# Inacap Ingenieria en informatica - Vespertino


from Controller.LibrosDAO import LibroDAO
from Controller.UserDAO import UsuarioDAO 

# --- Entrada de Datos ---

def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Entrada inválIda. Por favor, ingrese un número entero.")

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Entrada inválIda. Por favor, ingrese un número (decimal si es necesario).")


# --- Funciones CRUD para Libros ---

def registrar_libro():
    print("\n--- Registrar Nuevo Libro ---")
    dao = LibroDAO()

    nombre = input("Ingrese el nombre del libro: ").strip().title()
    precio = get_float_input("Ingrese el precio: $")
    genero = input("Ingrese el genero del libro: ").strip().title()
    tipo_tapa = input("Ingrese el tipo de tapa (ej: Dura, Blanda): ").strip().capitalize()
    paginas = get_int_input("Ingrese la cantIdad de páginas: ")
    autor = input("Ingrese el nombre del autor: ").strip().title()
    stock = get_int_input("Ingrese la cantIdad en stock: ")

    if dao.agregarLibro(nombre, precio, genero, tipo_tapa, paginas, autor, stock):
        print(f"Libro '{nombre}' registrado exitosamente con Id automático.")
    else:
        print("")

def listar_libros():
    dao = LibroDAO()
    dao.listarLibros()


def buscar_libro():
    print("\n--- Buscar Libros ---")
    dao = LibroDAO()
    print("Tipos de atributos:")
    print("Id")
    print("Nombre")
    print("Autor")
    print("Precio")
    print("Género")
    print("Tapa")
    print("Páginas")

    tipo = input("Ingrese el nombre o fragmento del atributo del libro a buscar: ").strip().capitalize()
    fragmento = input("Ingrese el nombre o fragmento del nombre del libro a buscar: ").strip().capitalize()

    if not fragmento:
        print("No se ingresó ningún fragmento para buscar.")
        return
    if not tipo:
        print("No se ingresó ningún tipo para buscar.")
        return

    libros = dao.buscarLibros(tipo,fragmento)


def actualizar_libro():
    print("\n--- Editar Libro Completo ---")
    dao = LibroDAO()

    Id_a_editar = get_int_input("Ingrese el Id del libro que desea editar: ")

    print(f"\nIngrese los NUEVOS datos para el libro con Id '{Id_a_editar}':")

    # Recopilar todos los nuevos datos
    nuevo_nombre = input("Ingrese el nuevo nombre del libro: ").strip().capitalize()
    nuevo_precio = get_float_input("Ingrese el nuevo precio: $")
    nuevo_genero = input("Ingrese el nuevo genero del libro: ").strip().capitalize()
    nuevo_tipo_tapa = input("Ingrese el nuevo tipo de tapa (ej: Dura, Blanda): ").strip().capitalize()
    nuevas_paginas = get_int_input("Ingrese la nueva cantIdad de páginas: ")
    nuevo_autor = input("Ingrese el nuevo nombre del autor: ").strip().title()
    nuevo_stock = get_int_input("Ingrese la nueva cantIdad en stock: ")

    nuevos_datos = {
        "Nombre": nuevo_nombre, 
        "Precio": nuevo_precio,
        "Genero": nuevo_genero,
        "Tapa": nuevo_tipo_tapa, 
        "Paginas": nuevas_paginas,
        "Autor": nuevo_autor,
        "Stock": nuevo_stock
    }

    if dao.actualizarLibro(Id_a_editar, nuevos_datos):
        print(f"Edición del libro con Id '{Id_a_editar}' completada.")
    else:
        print(f"No se pudo editar el libro con Id '{Id_a_editar}'.")


def eliminar_libro_Id():
    print("\n--- Eliminar Libro por Id ---")
    dao = LibroDAO()

    Id_a_eliminar = get_int_input("Ingrese el Id del libro que desea eliminar: ")

    confirmacion = input(f"¿Está seguro que desea eliminar el libro con Id '{Id_a_eliminar}'? (s/n): ").lower().strip()

    if confirmacion == 's':
 
        if dao.eliminarLibroId(Id_a_eliminar): 
            print(f"Operación de eliminación para el libro con Id '{Id_a_eliminar}' completada.")
        else:
            print(f"No se pudo eliminar el libro con Id '{Id_a_eliminar}'.")
    else:
        print("Eliminación de libro cancelada.")

def eliminar_libro_nombre():
    print("\n--- Eliminar Libro por Nombre ---")
    dao = LibroDAO()

    nombre_eliminar = input("Ingrese el nombre del libro que desea eliminar: ").strip().capitalize()

    confirmacion = input(f"¿Está seguro que desea eliminar el libro '{nombre_eliminar}'? (s/n): ").lower().strip()

    if confirmacion == 's':
     
        if dao.eliminarLibroNombre(nombre_eliminar): 
            print(f"Operación de eliminación para el libro '{nombre_eliminar}' completada.")
        else:
            print(f"No se pudo eliminar el libro '{nombre_eliminar}'.")
    else:
        print("Eliminación de libro cancelada.")

def eliminar_libro():
    """Función para elegir el método de eliminación de libros."""
    print("\n--- Eliminar Libro ---")
    while True:
        op = input("Seleccione \n1.- Eliminar libro por Id \n2.- Eliminar libro por nombre \n3.- Volver al menú principal\nSu opción: ")
        if op == '1':
            eliminar_libro_Id()
            break
        elif op == '2':
            eliminar_libro_nombre()
            break
        elif op == '3':
            break
        else:
            print("Opción no válIda. Por favor, seleccione 1, 2 o 3.")


# --- Funciones CRUD para Usuarios ---

def registrar_usuario():
    print("\n--- Registrar Usuario ---")
    dao = UsuarioDAO()

    usuario = input("Ingrese un nombre de usuario: ").strip().lower()
    nombre_u = input("Ingrese su nombre: ").strip().title()
    apellIdo_u = input("Ingrese su apellIdo: ").strip().title()
    email = input("Ingrese su Email: ").strip().lower()
    contraseña = input("Ingrese una contraseña: ") # Contraseña como string
    estado = True # Por defecto, un nuevo usuario está activo

    # Asumo que tu DAO tiene un método agregarUsuario con los parámetros correctos
    if dao.agregarUsuario(usuario, nombre_u, apellIdo_u, email, contraseña, estado):
        print(f"Usuario '{usuario}' registrado exitosamente con Id automático.")
    else:
        print(f"No se pudo registrar el usuario '{usuario}'. Consulte los logs para más detalles.")

def actualizar_usuario():
    print("\n--- Editar Usuario ---")
    dao = UsuarioDAO()

    # Se corrige el prompt para que sea de usuario, no de libro
    Id_a_editar = get_int_input("Ingrese el Id del usuario que desea editar: ")

    print(f"\nIngrese los NUEVOS datos para el usuario con Id '{Id_a_editar}':")

    nuevo_usuario = input("Ingrese un nuevo nombre de usuario: ").strip().lower() 
    nuevo_nombre = input("Ingrese un nuevo nombre: ").strip().capitalize()
    nuevo_apellIdo = input("Ingrese un nuevo apellIdo: ").strip().capitalize()
    nuevo_email = input("Ingrese el nuevo Email: ").strip().lower()
    nueva_contraseña = input("Ingrese la nueva contraseña: ") 

    nuevos_datos = {
        "Usuario": nuevo_usuario,
        "Nombre": nuevo_nombre,
        "ApellIdo": nuevo_apellIdo,
        "Email": nuevo_email,
        "Contraseña": nueva_contraseña
    }


    if dao.actualizarUsuario(Id_a_editar, nuevos_datos):
        print(f"Edición del usuario con Id '{Id_a_editar}' completada.")
    else:
        print(f"No se pudo editar el usuario con Id '{Id_a_editar}'.")


def listar_usuarios():
    dao = UsuarioDAO()
  
    dao.listarUsuarios()

def listar_usuarios_eliminados():
    dao = UsuarioDAO()

    dao.usuariosEliminados()

def eliminar_usuario():
    print("\n--- Desactivar/Eliminar Usuario (Cambiar Estado) ---")
    dao = UsuarioDAO()

    Id_a_modificar = get_int_input("Ingrese el Id del usuario que desea desactivar/eliminar: ")

    confirmacion = input(f"¿Está seguro que desea DESACTIVAR el usuario con Id '{Id_a_modificar}'? (s/n): ").lower().strip()

    if confirmacion == "s":
        # Cambiar el estado a False (desactivar)
        cambio_estado = {
            "Estado": False
        }

        # Asumo que UsuarioDAO tiene un método actualizarUsuario
        if dao.actualizarUsuario(Id_a_modificar, cambio_estado): # Aquí usas actualizarUsuario
            print(f"La cuenta con Id '{Id_a_modificar}' ha sIdo desactivada correctamente.")
        else:
            print(f"No se pudo desactivar la cuenta con Id '{Id_a_modificar}'.")
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
    print(" 3.- Libros: Buscar")
    print(" 4.- Libros: Actualizar")
    print(" 5.- Libros: Eliminar") # Ahora te permite elegir Id o Nombre
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
            eliminar_libro() 
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
            print("Opción no válIda. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()