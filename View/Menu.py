# Esteban Andres Ramirez Gonzalez
# Inacap Ingenieria en informatica - Vespertino
# Programación Orientada a Objeto Seguro (TI3V21/V-IEI-N2-P3-C1/V Puente Alto IEI)

from Controller.LibrosDAO import LibroDAO
from Controller.UserDAO import UsuarioDAO


def iniciarAplicacion():

    opcion = 0

    while opcion != 10:
        pass

# --- Funciones CRUD para Libros ---

def registrar_libro():
    print("Registrar libro")
    dao = LibroDAO()

    id = int(input("Ingrese el id: "))
    nombre = str(input("Ingrese el nombre del libro: "))
    precio = float(input("Ingrese el precio: $"))
    genero = str(input("Ingrese el genero del libro: "))
    tipo_tapa = str(input("Ingrese el tipo de tapa: "))
    paginas = int(input("Ingrese la cantidad de paginas: "))
    autor = str(input("Ingrese el nombre del autor: "))
    stock = int(input("Ingrese la cantidad: "))

    dao.agregarLibro(id, nombre, precio, genero, tipo_tapa, paginas, autor, stock)



def listar_libros():
    pass


def buscar_libro():
    pass


def actualizar_libro():
    pass
   
def eliminar_libro():
    pass

def registrar_usuario():
    print("Resgitar Usuario")
    dao = UsuarioDAO()
    id_u = ##tengo que hacer un autoincrement que revise si en la base de datos existe algun usuario y si existe cuente y agregue el utimo valor
    usuario = str(input("Ingrese un nombre de usuario: "))
    nombre_u = str(input("Ingrese su nombre: "))
    apellido_u = str(input("Ingrese su apellido: "))
    email = str(input("Ingrese su Email: "))
    contraseña = str(input("Ingrese una contraseña: "))
    estado = True

    dao.agregarUsuario(id_u, usuario, nombre_u, apellido_u, email, contraseña, estado)




def listar_usuarios():
    pass
   

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
    