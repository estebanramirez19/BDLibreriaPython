# Esteban Andres Ramirez Gonzalez
# Inacap Ingenieria en informatica - Vespertino
# Base de datos no relacionales

# Clases responsables de realizar las operaciones sobre la base de datos:
# HabitacionDAO: Gestiona las consultas relacionadas con las habitaciones.

from Database.Conexion import Conexion
from Model.autor import Habitacion
from Model.TipoHabitacion import TipoHabitacion 

class HabitacionDAO():
    def __init__(self):
        self.client = Conexion()


    def agregarHabitacion(self,numero_habitacion, tipo_id, precio):  
        try:    
            conexion = self.conn.obtenerConexion() 
            cursor = conexion.cursor()

            query = """INSERT INTO habitacion (numero_habitacion, tipo_id, precio) VALUES (%s,%s,%s)"""
            
            values = (numero_habitacion, tipo_id, precio)

            cursor.execute(query, values)

            conexion.commit()

            if cursor.rowcount > 0:
                print(f"Habitación con número {numero_habitacion} agregada correctamente.")
            else:
                print(f"Error al agregar la habitacion {numero_habitacion}.")

            cursor.close()

        except Exception as ex:
            print(f"Error al agregar habitación {ex}")
        finally:
            if conexion is not None:
                conexion.close()
	

    def eliminarHabitacion(self, id): #opcion 11 - no encuentra la habitacion ## falta revisar
        #requisito 5
        try:
            conexion = self.conn.obtenerConexion() 
            cursor = conexion.cursor()

            query = "DELETE FROM habitacion WHERE id = %s"
            values = [id]

            cursor.execute(query, values)

            conexion.commit()

            if cursor.rowcount > 0:
                print(f"Habitación con número {id} eliminada correctamente.")
            else:
                print(f"No se encontró la habitación con número {id}.")

            cursor.close()

        except Exception as ex:
            print(f"Error al eliminar habitación {ex}")	
        finally:
            if conexion is not None:
                conexion.close()	
  

    def actualizarHabitacion(self, numero_habitacion, precio, tipo_id,id): #opcion 7 funciona al 100%
        try:
            conexion = self.conn.obtenerConexion()
            cursor = conexion.cursor()

            query = """update habitacion set numero_habitacion = %s, precio = %s, tipo_id = %s WHERE Id = %s"""
            values = (numero_habitacion, precio, tipo_id,id)

            cursor.execute(query, values)

            conexion.commit()

            print(f"Habitación con número {numero_habitacion} actualizada correctamente")

            cursor.close()

        except Exception as ex:
            print(f"Error al actualizar habitación {ex}")
        finally:
            if conexion is not None:
                conexion.close()


    def listarHabitacionesYTipos(self):  #falta reparar el precio - sin opcion
        try:
            conexion = self.conn.obtenerConexion()
            cursor = conexion.cursor()

            cursor.execute("""SELECT habitacion.Id, habitacion.numero_habitacion, habitacion.tipo_id, 
                           habitacion.precio,tipo_habitacion.Id,  tipo_habitacion.descripcion,
                           tipo_habitacion.libro_id
                           from habitacion
                           INNER join tipo_habitacion
                           on habitacion.tipo_id = tipo_habitacion.Id""")

            lista = cursor.fetchall()

            habitaciones = []

            for habitacion in lista:
                tipo = TipoHabitacion(habitacion[4], habitacion[5], habitacion[6])
                habitacion = Habitacion(habitacion[0], habitacion[1], habitacion[2],habitacion[3],tipo)
                habitaciones.append(habitacion)
            return habitaciones
                
          
            cursor.close()

        except Exception as ex:
            print(f"Error al listar habitaciones {ex}")

        finally:
            if conexion is not None:
                conexion.close()
    
    
    def listarHabitaciones(self):
        try:
            conexion = self.conn.obtenerConexion()
            cursor = conexion.cursor()

            cursor.execute("SELECT * FROM habitacion")

            for (id, numero_habitacion, tipo_id, precio) in cursor:
                print(f"ID: {id} - Número de habitación: {numero_habitacion} - Tipo ID: {tipo_id} - Precio: {precio}")

            cursor.close()

        except TypeError as ex:
            print(f"Error al listar {ex}")

        finally:
            if conexion is not None:
                conexion.close()