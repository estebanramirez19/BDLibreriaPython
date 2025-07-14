# Esteban Andres Ramirez Gonzalez
# Inacap Ingenieria en informatica - Vespertino
# Programación Orientada a Objeto Seguro (TI3V21/V-IEI-N2-P3-C1/V Puente Alto IEI)

from Controller.HabitacionDAO import HabitacionDAO
from Controller.libroDAO import libroDAO
from Controller.TipoHabitacionDAO import TipoHabitacionDAO


def iniciarAplicacion():

    opcion = 0

    while opcion != 16:

        try:  
                # --- Base de Datos (simulada con listas) ---
libros = []
usuarios = []
carrito = {} # Usaremos un diccionario para el carrito: {id_usuario: [lista_de_libros_en_carrito]}

# --- Funciones CRUD para Libros ---

def registrar_libro():
    """Permite registrar un nuevo libro con sus características."""
    print("\n--- REGISTRAR LIBRO ---")
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    genero = input("Género: ").strip()
    precio = float(input("Precio: "))
    stock = int(input("Stock: "))
    
    libro = {
        "id": len(libros) + 1, # ID autoincremental simple
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "precio": precio,
        "stock": stock
    }
    libros.append(libro)
    print(f"Libro '{titulo}' registrado con éxito. ID: {libro['id']}")

def listar_libros():
    """Muestra todos los libros disponibles."""
    print("\n--- LISTADO DE LIBROS ---")
    if not libros:
        print("No hay libros registrados.")
        return
    
    for libro in libros:
        print(f"ID: {libro['id']} | Título: {libro['titulo']} | Autor: {libro['autor']} | Género: {libro['genero']} | Precio: ${libro['precio']:.2f} | Stock: {libro['stock']}")

def buscar_libro():
    """Permite buscar libros por título o autor."""
    print("\n--- BUSCAR LIBRO ---")
    criterio = input("Buscar por (titulo/autor): ").lower().strip()
    valor = input(f"Ingrese el {criterio} a buscar: ").strip().lower()
    
    resultados = []
    for libro in libros:
        if criterio == "titulo" and valor in libro["titulo"].lower():
            resultados.append(libro)
        elif criterio == "autor" and valor in libro["autor"].lower():
            resultados.append(libro)
            
    if not resultados:
        print("No se encontraron libros con ese criterio.")
    else:
        print("\n--- RESULTADOS DE BÚSQUEDA ---")
        for libro in resultados:
            print(f"ID: {libro['id']} | Título: {libro['titulo']} | Autor: {libro['autor']} | Género: {libro['genero']} | Precio: ${libro['precio']:.2f} | Stock: {libro['stock']}")

def actualizar_libro():
    """Permite actualizar la información de un libro existente."""
    print("\n--- ACTUALIZAR LIBRO ---")
    libro_id = int(input("Ingrese el ID del libro a actualizar: "))
    
    for libro in libros:
        if libro["id"] == libro_id:
            print(f"Editando libro: {libro['titulo']}")
            libro["titulo"] = input(f"Nuevo título ({libro['titulo']}): ") or libro["titulo"]
            libro["autor"] = input(f"Nuevo autor ({libro['autor']}): ") or libro["autor"]
            libro["genero"] = input(f"Nuevo género ({libro['genero']}): ") or libro["genero"]
            
            nuevo_precio = input(f"Nuevo precio ({libro['precio']}): ")
            if nuevo_precio:
                libro["precio"] = float(nuevo_precio)
                
            nuevo_stock = input(f"Nuevo stock ({libro['stock']}): ")
            if nuevo_stock:
                libro["stock"] = int(nuevo_stock)
                
            print("Libro actualizado con éxito.")
            return
    print("Libro no encontrado.")

def eliminar_libro():
    """Permite eliminar un libro por su ID."""
    print("\n--- ELIMINAR LIBRO ---")
    libro_id = int(input("Ingrese el ID del libro a eliminar: "))
    
    for i, libro in enumerate(libros):
        if libro["id"] == libro_id:
            del libros[i]
            print(f"Libro con ID {libro_id} eliminado con éxito.")
            return
    print("Libro no encontrado.")

# --- Funciones CRUD para Usuarios ---

def registrar_usuario():
    """Permite registrar un nuevo usuario."""
    print("\n--- REGISTRAR USUARIO ---")
    nombre_usuario = input("Nombre de usuario: ").strip()
    contrasena = input("Contraseña: ").strip()
    
    usuario = {
        "id": len(usuarios) + 1, # ID autoincremental simple
        "nombre_usuario": nombre_usuario,
        "contrasena": contrasena # En un sistema real, la contraseña debería ser hasheada
    }
    usuarios.append(usuario)
    print(f"Usuario '{nombre_usuario}' registrado con éxito. ID: {usuario['id']}")

def listar_usuarios():
    """Muestra todos los usuarios registrados."""
    print("\n--- LISTADO DE USUARIOS ---")
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    
    for usuario in usuarios:
        print(f"ID: {usuario['id']} | Nombre de Usuario: {usuario['nombre_usuario']}")

# --- Funciones para el Carrito de Compras ---

def agregar_al_carrito():
    """Permite agregar un libro al carrito de un usuario."""
    print("\n--- AGREGAR AL CARRITO ---")
    if not usuarios:
        print("Primero debe registrar al menos un usuario.")
        return
    if not libros:
        print("No hay libros disponibles para agregar al carrito.")
        return

    listar_usuarios()
    usuario_id = int(input("Ingrese el ID del usuario: "))
    
    usuario_encontrado = None
    for u in usuarios:
        if u["id"] == usuario_id:
            usuario_encontrado = u
            break
            
    if not usuario_encontrado:
        print("Usuario no encontrado.")
        return
        
    listar_libros()
    libro_id = int(input("Ingrese el ID del libro que desea agregar al carrito: "))
    
    libro_encontrado = None
    for l in libros:
        if l["id"] == libro_id:
            libro_encontrado = l
            break
            
    if not libro_encontrado:
        print("Libro no encontrado.")
        return
        
    if libro_encontrado["stock"] <= 0:
        print("Lo siento, este libro no tiene stock disponible.")
        return

    # Inicializar carrito para el usuario si no existe
    if usuario_id not in carrito:
        carrito[usuario_id] = []
        
    carrito[usuario_id].append(libro_encontrado)
    libro_encontrado["stock"] -= 1 # Reducir el stock del libro
    print(f"'{libro_encontrado['titulo']}' agregado al carrito de {usuario_encontrado['nombre_usuario']}.")

def ver_carrito():
    """Permite ver el contenido del carrito de un usuario."""
    print("\n--- VER CARRITO ---")
    if not usuarios:
        print("Primero debe registrar al menos un usuario.")
        return

    listar_usuarios()
    usuario_id = int(input("Ingrese el ID del usuario cuyo carrito desea ver: "))

    usuario_encontrado = None
    for u in usuarios:
        if u["id"] == usuario_id:
            usuario_encontrado = u
            break
            
    if not usuario_encontrado:
        print("Usuario no encontrado.")
        return
            
    if usuario_id not in carrito or not carrito[usuario_id]:
        print(f"El carrito de {usuario_encontrado['nombre_usuario']} está vacío.")
        return
        
    print(f"\n--- CARRITO DE {usuario_encontrado['nombre_usuario'].upper()} ---")
    total_carrito = 0
    for libro in carrito[usuario_id]:
        print(f"ID: {libro['id']} | Título: {libro['titulo']} | Precio: ${libro['precio']:.2f}")
        total_carrito += libro['precio']
    print(f"Total del carrito: ${total_carrito:.2f}")

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
    