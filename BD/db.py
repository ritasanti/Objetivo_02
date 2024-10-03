#importar paquetes
import os
import pymysql
from dotenv import load_dotenv


#cargar variables de entorno
load_dotenv()

#conexion a la base de datos
def conexion():
    return pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_DATABASE")
    )