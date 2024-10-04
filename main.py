from flask import Flask,jsonify,request
from BD.db import conexion
from models import modelo
import hashlib

app=Flask(__name__)


#Endpoint para mostrar todas las personas de la tabla
@app.route("/persona", methods=["GET"])
def get_Persona():
    resultado=[]
    result=modelo.obtenerDatos()
    for personas in result:
        resultado.append(personas)
    return jsonify(resultado)


#Endpoint muestra datos que cumplen condicion
@app.route("/persona/estado", methods=["GET"])
def get_Persona_Estado():
    return jsonify([persona for persona in modelo.obtenerDatos_Estado()])


#Ruta para el sp_RegistroPersona
@app.route("/persona/SP_Registro", methods=["POST"])
def inser_registro():
    apellido=request.form.get("apellido")
    nombres=request.form.get("nombres")
    dni=request.form.get("dni")
    domicilio=request.form.get("domicilio")
    telefono=request.form.get("telefono")
    id_estado=request.form.get("id_estado")
    fechora_registro=request.form.get("fechora_registro")
    try:
        modelo.sp_RegistroPersona(apellido,nombres,dni,domicilio,telefono,id_estado,fechora_registro)
        return jsonify({"Mensaje":"Registro realizado correctamente"})
    except Exception as e:
        return jsonify({"Mensaje":str (e)}), 500


#Ruta para el SP_UpdatePersona
@app.route("/persona/update/<int:id>", methods=["PUT"])
def updatePersona(id):
    try:
        apellido=request.form.get("apellido")
        nombres=request.form.get("nombres")
        dni=request.form.get("dni")
        domicilio=request.form.get("domicilio")
        telefono=request.form.get("telefono")
        id_estado=request.form.get("id_estado")
        modelo.sp_updatePersona(id,apellido,nombres,dni,domicilio,telefono,id_estado)
        return jsonify({"Mensaje":"Se actualizo correctamente"})
    except Exception as e:
        return jsonify({"Mensaje":str (e)}), 500


# Ruta para el SP_EliminarPersona
@app.route("/persona/eliminar/<int:id_persona>", methods=["DELETE"])
def eliminar_persona(id_persona):
    try:
        modelo.sp_eliminarPersona(id_persona)
        return jsonify({"Mensaje": f"Persona con ID {id_persona} eliminada correctamente"}), 200
    except Exception as e:
        return jsonify({"Error": str(e)}), 500
    



#funcion para comparar contraseñas
def verificar_claves(password_ingresada,hashed_password):
    hash_ingresada=hashlib.md5(password_ingresada.encode()).hexdigest()
    #comparar claves
    return hash_ingresada==hashed_password

#Api para comprobar que el usuario esta registrado en la base de datos
#Todavia en revision
@app.route('/api/login', methods=['POST'])
def login_api():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    con = conexion()
    cursor = con.cursor()
    try:
        cursor.execute("SELECT id, password FROM usuarios WHERE nombres = %s", (username,))
        user = cursor.fetchone()

        if user and verificar_claves(password, user[1]):
            return jsonify({'status': True, 'cod': user[0]})
        else:
            return jsonify({'status': False})
    finally:
        cursor.close()
        con.close()


#Prueba de api Tipo_usario


@app.route('/api/tipo_usuario', methods=['GET'])
def obtener_tipo_usuario():
    id_usuario = request.args.get('id_usuario')
    if not id_usuario:
        return jsonify({'status': False, 'error': 'Id_Usuario es requerido'}), 400

    con = conexion()
    cursor = con.cursor()
    try:
        query = """
        SELECT tu.descripcion 
        FROM usuarios u
        JOIN tipo_usuario tu ON u.id_tipo_usuario = tu.id_tipo_usuario
        WHERE u.id = %s
        """
        cursor.execute(query, (id_usuario,))
        user = cursor.fetchone()
        
        if user:
            return jsonify({'status': True, 'tipo_usuario': user[0]})
        else:
            return jsonify({'status': False, 'error': 'Usuario no encontrado'}), 404
    finally:
        cursor.close()
        con.close()



#Prueba api datosUsuario
#Ver de factorizar
@app.route('/api/datos_usuario', methods=['GET'])
def obtener_datos_usuario():
    id_usuario = request.args.get('id_usuario')
    if not id_usuario:
        return jsonify({'status': False, 'error': 'Id_Usuario es requerido'}), 400

    con = conexion()
    cursor = con.cursor()
    try:
        query = """
        SELECT u.id, u.Apellido, u.Nombres, u.Password, tu.descripcion AS tipo_usuario, u.fechora_registro, u.fechora_modificacion, u.id_estado_registro
        FROM usuarios u
        JOIN tipo_usuario tu ON u.id_tipo_usuario = tu.id_tipo_usuario
        WHERE u.id = %s
        """
        cursor.execute(query, (id_usuario,))
        user = cursor.fetchone()
        
        if user:
            user_data = {
                'id': user[0],
                'Apellido': user[1],
                'Nombres': user[2],
                'Password': user[3],
                'tipo_usuario': user[4],
                'fechora_registro': user[5],
                'fechora_modificacion': user[6],
                'id_estado_registro': user[7]
            }
            return jsonify({'status': True, 'datos_usuario': user_data})
        else:
            return jsonify({'status': False, 'error': 'Usuario no encontrado'}), 404
    finally:
        cursor.close()
        con.close()





# Ruta para SP_AgregarReparticion
@app.route("/reparticion/agregar", methods=["POST"])
def agregarReparticion():
    try:
        nombres = request.form.get("nombres")
        descripcion = request.form.get("descripcion")
        modelo.sp_agregarReparticion(nombres, descripcion)
        return jsonify({"Mensaje": "Repartición agregada correctamente"}), 201
    except Exception as e:
        return jsonify({"Error": str(e)}), 500

# Ruta para SP_ConsultaReparticionID
@app.route("/reparticion/consulta/<int:id_reparticion>", methods=["GET"])
def consultaReparticion(id_reparticion):
    try:
        reparticion = modelo.sp_consultaReparticionID(id_reparticion)
        if reparticion:
            return jsonify(reparticion), 200
        else:
            return jsonify({"Mensaje": "Repartición no encontrada"}), 404
    except Exception as e:
        return jsonify({"Error": str(e)}), 500

# Ruta para SP_EliminarReparticion
@app.route("/reparticion/eliminar/<int:id_reparticion>", methods=["DELETE"])
def eliminarReparticion(id_reparticion):
    try:
        modelo.sp_eliminarReparticion(id_reparticion)
        return jsonify({"Mensaje": f"Repartición con ID {id_reparticion} eliminada correctamente"}), 200
    except Exception as e:
        return jsonify({"Error": str(e)}), 500

# Ruta para SP_ModificarReparticion
@app.route("/reparticion/update/<int:id_reparticion>", methods=["PUT"])
def modificarReparticion(id_reparticion):
    try:
        nombres = request.form.get("nombres")
        descripcion = request.form.get("descripcion")
        modelo.sp_modificarReparticion(id_reparticion, nombres, descripcion)
        return jsonify({"Mensaje": "Repartición modificada correctamente"}), 200
    except Exception as e:
        return jsonify({"Error": str(e)}), 500
    
if __name__=='__main__':
    with app.app_context():
        app.run(host="localhost",port="5000",debug=True)