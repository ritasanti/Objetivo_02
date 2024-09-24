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
#Revisar 
"""def agregarRegistro(apellido, nombres, dni, domicilio, telefono, id_estado, fecha_registro,fecha_modificacion):
    try:
        conex = conexion()
        with conex.cursor() as cursor:
            sql = "INSERT INTO PERSONA(APELLIDO, NOMBRE, DNI, DOMICILIO, TELEFONO, ID_ESTADO, FECHA_REGISTRO,FECHA_MODIFICACION) VALUES (%s, %s, %s, %s, %s, %s, %s,%s)"
            cursor.execute(sql, (apellido, nombres, dni, domicilio, telefono, id_estado, fecha_registro,fecha_modificacion))
            conex.commit()
    except Exception as e:
        print("Error al agregar el registro:", e)
    finally:
        conex.close()"""


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
  


#Llamado al Stored Procedure SP_ConsultarPersona
def sp_consultarPersona():
    con=conexion()
    cursor=con.cursor()
    sql_query="CALL SP_CONSULTARPERSONA"
    try:
        cursor.execute(sql_query)
        results=cursor.fetchall()
        return results
    except Exception as e:
        print("Error al llamar al procedimiento: ",e)
        return None
    finally:
        cursor.close()
        con.close()