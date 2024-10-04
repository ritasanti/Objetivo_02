from BD.db import conexion
from mysql.connector import Error
from datetime import datetime
import mysql.connector


#Consulta get de todos las personas
def obtenerDatos():
    conecc=conexion()
    registros=[]
    with conecc.cursor() as cursor:
        cursor.execute("SELECT * FROM PERSONA")
        registros=cursor.fetchall()
        conecc.close()
    return registros

#Traer datos si se cumple la condicion
def obtenerDatos_Estado():
    con = conexion()
    sql_query = "SELECT * FROM PERSONA WHERE ID_ESTADO=%s"
    registros = []
    try:
        with con.cursor() as cursor:
            cursor.execute(sql_query, (1,))
            registros = cursor.fetchall()
    except Exception as e:
        print(f"Error al obtener datos: {e}")
    finally:
        con.close()
    return registros


#utilizacion de SP_AgeregarPersona
def sp_AgregarPersona(apellido, nombres, dni, domicilio, fecha_nac, telefono, fechora_registro, genero, email, id_reparticion, id_estado_registro):
    con = conexion()
    cursor = con.cursor()
    
    sql_quer = "CALL SP_AgregarPersona(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    
    try:
        cursor.execute(sql_quer, (apellido, nombres, dni, domicilio, fecha_nac, telefono, fechora_registro, genero, email, id_reparticion, id_estado_registro))
        con.commit()
    except Exception as e:
        print("Error al querer insertar un registro:", e)
        con.rollback()
    finally:
        cursor.close()
        con.close()

#Interaccion con la base para usar el procedimiento almacenado
def sp_updatePersona(id, apellido, nombres, dni, domicilio, telefono, edad, genero, antiguedad, email, id_reparticion, id_estado, fechora_registro):
    con = None  # Inicializamos con None
    cursor = None
    try:
        con = conexion()  # Creamos la conexión
        cursor = con.cursor()
        cursor.callproc('sp_updatepersona', (id, apellido, nombres, dni, domicilio, telefono, edad, genero, antiguedad, email, id_reparticion, id_estado, fechora_registro))
        con.commit()
        print("Datos actualizados ")
    except Exception as e:
        print("Error al querer actualizar los datos: ", e)
    finally:
        if cursor is not None:  # Cerramos solo si cursor fue creado
            cursor.close()
        if con is not None:  # Cerramos solo si con fue creado
            con.close()



# Función para conectarse a la base de datos y ejecutar SP_DeletePersona
import mysql.connector
from mysql.connector import Error

def sp_eliminarPersona(id_persona):
    con = None
    try:
        # Establecer la conexión a la base de datos
        con = mysql.connector.connect(
            host='localhost',
            database='persona-forbit',
            user='root',
            password=''
        )
        cursor = con.cursor()
        # Llamar al procedimiento almacenado SP_EliminarPersona
        sql_query = "CALL SP_EliminarPersona(%s)"
        cursor.execute(sql_query, (id_persona,))
        con.commit()
        print(f"Persona con ID {id_persona} eliminada (baja lógica) exitosamente.")
    except Error as e:
        print(f"Error al ejecutar SP_EliminarPersona: {e}")
        if con:  # Verifica si la conexión fue establecida
            con.rollback()  # Revertir en caso de error
    finally:
        if con:  # Cierra la conexión solo si fue establecida
            cursor.close()
            con.close()
