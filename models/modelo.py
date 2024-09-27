from BD.db import conexion
import datetime




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

#Agregar un registro





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