from BD.db import conexion
from mysql.connector import Error
import datetime
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

#Eliminar el registro
def eliminarDato(id):
    con=conexion()
    sql_queryy="DELETE FROM PERSONA WHERE ID=%s"
    with con.cursor() as cursor:
        cursor.execute(sql_queryy,id)
        con.commit()
        con.close()

        
#utilizacion de SP_RegistroPersona
def sp_RegistroPersona(apellido,nombres,dni,domicilio,telefono,id_estado,fechora_registro):
    con=conexion()
    cursor=con.cursor()
    sql_quer="call sp_registropersona(%s,%s,%s,%s,%s,%s,%s)"
    try:
        sql_quer="call sp_registropersona(%s,%s,%s,%s,%s,%s,%s)"
        fechora_registro=datetime.date.today()
        cursor.execute(sql_quer,(apellido,nombres,dni,domicilio,telefono,id_estado,fechora_registro))
        con.commit()
    except Exception as e:
        print("Error al quere insertar un registro: ",e)
        con.rollback()
    finally:
        cursor.close()
        con.close()

# Función para conectarse a la base de datos y ejecutar SP_DeletePersona
def sp_eliminarPersona(id_persona):
    try:
        # Establecer la conexión a la base de datos
        con = mysql.connector.connect(
            host='localhost',
            database='persona-forbit',
            user='root', #Completar cada uno con su Base de datos
            password='root' #Completar cada uno con su Base de datos
        )

        if con.is_connected():
            cursor = con.cursor()
            # Llamar al procedimiento almacenado SP_DeletePersona
            sql_query = "CALL SP_DeletePersona(%s)"
            cursor.execute(sql_query, (id_persona,))
            con.commit()
            print(f"Persona con ID {id_persona} eliminada (baja lógica) exitosamente.")
    
    except Error as e:
        print(f"Error al ejecutar SP_DeletePersona: {e}")
        con.rollback()  # Revertir en caso de error
    
    finally:

        cursor.close()
        con.close()

# Llamado al Stored Procedure SP_EliminarPersona
def sp_eliminarPersona(id_persona):
    con = conexion()
    cursor=con.cursor()
    sql_query = "UPDATE PERSONA SET ID_ESTADO = %s WHERE ID_PERSONA = %s"
    try:
        with con.cursor() as cursor:
            cursor.execute(sql_query, (2, id_persona))
            con.commit()
            print(f"Persona con ID {id_persona} eliminada exitosamente.")
    except Exception as e:
        print(f"Error al eliminar persona: {e}")
        con.rollback()
    finally:
        con.close()

        if con.is_connected():
            cursor.close()
            con.close()
