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
def SP_RegistroPersona(ID_persona,Apellido, Nombres,DNI, Domicilio, Fecha_Nac, Telefono, FecHora_Registros,FecHora_Modificacion,Edad, Genero,Antiguedad, Email, Id_Reparticion, Id_Estado_Registro):
    con = conexion()
    cursor = con.cursor()
    
    sql_quer = "CALL SP_RegistroPersona(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    
    try:
        cursor.execute(sql_quer, (ID_persona,Apellido, Nombres,DNI, Domicilio, Fecha_Nac, Telefono, FecHora_Registros,FecHora_Modificacion,Edad, Genero,Antiguedad, Email, Id_Reparticion, Id_Estado_Registro))
        con.commit()
    except Exception as e:
        print("Error al querer insertar un registro:", {e})
        con.rollback()
    finally:
        cursor.close()
        con.close()

#Interaccion con la base para usar el procedimiento almacenado
def SP_EditarPersona(ID_persona,Apellido, Nombres,DNI, Domicilio, Fecha_Nac, Telefono, FecHora_Registros,FecHora_Modificacion,Edad, Genero,Antiguedad, Email, Id_Reparticion, Id_Estado_Registro):
    con = None  # Inicializamos con None
    cursor = None
    try:
        con = conexion()  # Creamos la conexión
        cursor = con.cursor()
        cursor.callproc('SP_EditarPersona', (ID_persona,Apellido, Nombres,DNI, Domicilio, Fecha_Nac, Telefono, FecHora_Registros,FecHora_Modificacion,Edad, Genero,Antiguedad, Email, Id_Reparticion, Id_Estado_Registro))
        con.commit()
        print("Datos actualizados ")
    except Exception as e:
        print("Error al querer actualizar los datos: ", {e})
    finally:
        if cursor is not None:  # Cerramos solo si cursor fue creado
            cursor.close()
        if con is not None:  # Cerramos solo si con fue creado
            con.close()



# Función para conectarse a la base de datos y ejecutar SP_DeletePersona
import mysql.connector
from mysql.connector import Error

def SP_EliminarPersona(Id_persona):
    con = None
    cursor = None
    try:
        # Establecer la conexión a la base de datos
        con =conexion()
        cursor = con.cursor()
        # Llamar al procedimiento almacenado SP_EliminarPersona
        sql_query = "CALL SP_EliminarPersona(%s)"
        cursor.execute(sql_query, (Id_persona,))
        con.commit()
        print(f"Persona con ID {Id_persona} eliminada (baja lógica) exitosamente.")
    except Error as e:
        print(f"Error al ejecutar SP_EliminarPersona: {e}")
        if con:  # Verifica si la conexión fue establecida
            con.rollback()  # Revertir en caso de error
    finally:
        if con:  # Cierra la conexión solo si fue establecida
            cursor.close()
            con.close()


def SP_InsertarLicencia(p_Id_Persona, p_Nro_Art, p_Codigo, p_Diagnostico,p_Medico, p_Matricula, p_Establecimiento,p_Fecha_de_inicio, p_Fecha_de_fin, p_Cant_dias_licencias, p_Id_Estado_Licencia, p_Observaciones):
    con = None  # Inicializamos la conexión como None
    cursor = None
    try:
        # Establecer la conexión a la base de datos
        con = conexion()
        cursor = con.cursor()
        # Llamar al procedimiento almacenado SP_InsertarLicencia
        cursor.callproc('SP_InsertarLicencia', (
            p_Id_Persona, p_Nro_Art, p_Codigo, p_Diagnostico,
            p_Medico, p_Matricula, p_Establecimiento,
            p_Fecha_de_inicio, p_Fecha_de_fin,
            p_Cant_dias_licencias, p_Id_Estado_Licencia,
            p_Observaciones
        ))
        con.commit()  # Confirmar la transacción
        print("Licencia insertada exitosamente.")
    except Exception as e:
        print("Error al querer insertar la licencia: ", {e})
    finally:
        if cursor is not None:  # Cerramos solo si el cursor fue creado
            cursor.close()
        if con is not None:  # Cerramos solo si la conexión fue establecida
            con.close()

def SP_AgregarReparticion(p_Nombres, p_Descripcion):
    con = None  # Inicializamos la conexión como None
    cursor = None  # Inicializamos el cursor como None
    try:
        # Establecer la conexión a la base de datos
        con = conexion()
        cursor = con.cursor()
        # Llamar al procedimiento almacenado SP_AgregarReparticion
        cursor.callproc('SP_AgregarReparticion', (p_Nombres, p_Descripcion))
        con.commit()  # Confirmar la transacción
        print("Repartición agregada exitosamente.")
    except Exception as e:
        print("Error al querer agregar la repartición: ", {e})
    finally:
        if cursor is not None:  # Cerramos solo si el cursor fue creado
            cursor.close()
        if con is not None:  # Cerramos solo si la conexión fue establecida
            con.close()

def SP_ConsultaPersona():
    con = None  # Inicializamos la conexión como None
    cursor = None  # Inicializamos el cursor como None
    try:
        # Establecer la conexión a la base de datos
        con = conexion()
        cursor = con.cursor()
        # Llamar al procedimiento almacenado SP_ConsultaPersona
        cursor.callproc('SP_ConsultaPersona')
        # Recoger los resultados
        results = []
        for result in cursor.stored_results():
            results.extend(result.fetchall())  # Agregar resultados a la lista
        # Devolver resultados
        return results
    except Exception as e:
        print("Error al querer consultar personas: ", {e})
        return None
    finally:
        if cursor is not None:  # Cerramos solo si el cursor fue creado
            cursor.close()
        if con is not None:  # Cerramos solo si la conexión fue establecida
            con.close()

def SP_ConsultaPersonaDNI(DNI_Persona):
    con = None  # Inicializamos la conexión como None
    cursor = None  # Inicializamos el cursor como None
    try:
        # Establecer la conexión a la base de datos
        con = conexion()
        cursor = con.cursor()
        # Llamar al procedimiento almacenado SP_ConsultaPersonaDNI
        cursor.callproc('SP_ConsultaPersonaDNI', (DNI_Persona,))

        # Recoger los resultados
        results = []
        for result in cursor.stored_results():
            results.extend(result.fetchall())  # Agregar resultados a la lista

        # Devolver resultados
        return results

    except Exception as e:
        print("Error al querer consultar persona por DNI: ", {e})
        return None
    finally:
        if cursor is not None:  # Cerramos solo si el cursor fue creado
            cursor.close()
        if con is not None:  # Cerramos solo si la conexión fue establecida
            con.close()

def SP_ConsultaPersonaID(Id_Persona):
    con = None  # Inicializamos la conexión como None
    cursor = None  # Inicializamos el cursor como None
    try:
        # Establecer la conexión a la base de datos
        con = conexion()
        cursor = con.cursor()
        # Llamar al procedimiento almacenado SP_ConsultaPersonaID
        cursor.callproc('SP_ConsultaPersonaID', (Id_Persona,))
        # Recoger los resultados
        results = []
        for result in cursor.stored_results():
            results.extend(result.fetchall())  # Agregar resultados a la lista
        # Devolver resultados
        return results

    except Exception as e:
        print("Error al querer consultar persona por ID: ", {e})
        return None
    finally:
        if cursor is not None:  # Cerramos solo si el cursor fue creado
            cursor.close()
        if con is not None:  # Cerramos solo si la conexión fue establecida
            con.close()

def SP_ConsultaPersonaLike(apellido):
    con = None  # Inicializamos la conexión como None
    cursor = None  # Inicializamos el cursor como None
    try:
        # Establecer la conexión a la base de datos
        con = conexion()
        cursor = con.cursor()
        # Llamar al procedimiento almacenado SP_ConsultaPersonaLike
        cursor.callproc('SP_ConsultaPersonaLike', (apellido,))
        # Recoger los resultados
        results = []
        for result in cursor.stored_results():
            results.extend(result.fetchall())  # Agregar resultados a la lista
        # Devolver resultados
        return results

    except Exception as e:
        print("Error al querer consultar persona por apellido: ", {e})
        return None
    finally:
        if cursor is not None:  # Cerramos solo si el cursor fue creado
            cursor.close()
        if con is not None:  # Cerramos solo si la conexión fue establecida
            con.close()

def SP_ConsultaReparticionID(Id_Reparticion):
    con = None  # Inicializamos la conexión como None
    cursor = None  # Inicializamos el cursor como None
    try:
        # Establecer la conexión a la base de datos
        con = conexion()
        cursor = con.cursor()
        # Llamar al procedimiento almacenado SP_ConsultaReparticionID
        cursor.callproc('SP_ConsultaReparticionID', (Id_Reparticion,))

        # Recoger los resultados
        results = []
        for result in cursor.stored_results():
            results.extend(result.fetchall())  # Agregar resultados a la lista

        # Devolver resultados
        return results

    except Exception as e:
        print("Error al querer consultar repartición por ID: ", {e})
        return None
    finally:
        if cursor is not None:  # Cerramos solo si el cursor fue creado
            cursor.close()
        if con is not None:  # Cerramos solo si la conexión fue establecida
            con.close()

def SP_EliminarReparticion(Id_Reparticion):
    con = None  # Inicializamos la conexión como None
    cursor = None  # Inicializamos el cursor como None
    try:
        # Establecer la conexión a la base de datos
        con = conexion()
        cursor = con.cursor()
        # Llamar al procedimiento almacenado SP_EliminarReparticion
        cursor.callproc('SP_EliminarReparticion', (Id_Reparticion,))

        con.commit()  # Confirmar los cambios
        print(f"Repartición con ID {Id_Reparticion} eliminada (baja lógica) exitosamente.")

    except Exception as e:
        print("Error al querer eliminar la repartición: ", {e})
        if con:  # Verifica si la conexión fue establecida
            con.rollback()  # Revertir en caso de error
    finally:
        if cursor is not None:  # Cerramos solo si el cursor fue creado
            cursor.close()
        if con is not None:  # Cerramos solo si la conexión fue establecida
            con.close()

def SP_ModificarReparticion(Id_Reparticion, Nombres, Descripcion):
    con = None  # Inicializamos la conexión como None
    cursor = None  # Inicializamos el cursor como None
    try:
        # Establecer la conexión a la base de datos
        con = conexion()
        cursor = con.cursor()
        # Llamar al procedimiento almacenado SP_ModificarReparticion
        cursor.callproc('SP_ModificarReparticion', (Id_Reparticion, Nombres, Descripcion))

        con.commit()  # Confirmar los cambios
        print(f"Repartición con ID {Id_Reparticion} actualizada exitosamente.")

    except Exception as e:
        print("Error al querer modificar la repartición: ", {e})
        if con:  # Verifica si la conexión fue establecida
            con.rollback()  # Revertir en caso de error
    finally:
        if cursor is not None:  # Cerramos solo si el cursor fue creado
            cursor.close()
        if con is not None:  # Cerramos solo si la conexión fue establecida
            con.close()