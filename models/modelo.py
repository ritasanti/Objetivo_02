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