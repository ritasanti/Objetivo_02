from flask import Flask, jsonify, request
from BD.db import conexion
from models import modelo
import hashlib
from datetime import datetime

app = Flask(__name__)

# Endpoint para mostrar todas las personas de la tabla
@app.route("/persona", methods=["GET"])
def get_persona():
    resultado = []
    result = modelo.obtenerDatos()
    for persona in result:
        resultado.append(persona)
    return jsonify(resultado)

# Endpoint para mostrar datos que cumplen condición
@app.route("/persona/estado", methods=["GET"])
def get_persona_estado():
    return jsonify([persona for persona in modelo.obtenerDatos_Estado()])

# API para agregar persona
@app.route("/persona/agregar", methods=["POST"])
def agregar_persona():
    apellido = request.form.get("apellido")
    nombres = request.form.get("nombres")
    dni = request.form.get("dni")
    domicilio = request.form.get("domicilio")
    telefono = request.form.get("telefono")
    fechora_registros = request.form.get("fechora_registros", datetime.today())
    fecha_nac = request.form.get("fecha_nac")
    genero = request.form.get("genero")
    email = request.form.get("email")
    id_reparticion = request.form.get("id_reparticion")
    id_estado_registro = request.form.get("id_estado")

    try:
        modelo.sp_AgregarPersona(apellido, nombres, dni, domicilio, fecha_nac, telefono, fechora_registros, genero, email, id_reparticion, id_estado_registro)
        return jsonify({"Mensaje": "Registro realizado correctamente"}), 201
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 500

# API para modificar persona
@app.route("/persona/modificar/<int:id>", methods=["PUT"])
def modificar_persona(id):
    try:
        apellido = request.form.get("apellido")
        nombres = request.form.get("nombres")
        dni = request.form.get("dni")
        domicilio = request.form.get("domicilio")
        telefono = request.form.get("telefono")
        edad = request.form.get("edad")
        genero = request.form.get("genero")
        antiguedad = request.form.get("antiguedad")
        email = request.form.get("email")
        id_reparticion = request.form.get("id_reparticion")
        id_estado = request.form.get("id_estado")
        fechora_registro = datetime.now()
        modelo.sp_updatePersona(id, apellido, nombres, dni, domicilio, telefono, edad, genero, antiguedad, email, id_reparticion, id_estado, fechora_registro)
        return jsonify({"Mensaje": "Se actualizó correctamente"})
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 500

# API para eliminar persona
@app.route("/persona/eliminar/<int:id_persona>", methods=["DELETE"])
def eliminar_persona(id_persona):
    try:
        modelo.sp_eliminarPersona(id_persona)
        return jsonify({"Mensaje": f"Persona con ID {id_persona} eliminada correctamente"}), 200
    except Exception as e:
        return jsonify({"Error": str(e)}), 500

# Función para comparar contraseñas
def verificar_claves(password_ingresada, hashed_password):
    hash_ingresada = hashlib.md5(password_ingresada.encode()).hexdigest()
    # Comparar claves
    return hash_ingresada == hashed_password

# API para comprobar que el usuario está registrado en la base de datos
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

# API para obtener tipo de usuario
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

# API para obtener datos del usuario
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

# API para consultar persona por ID
@app.route("/persona/consulta/<int:id_persona>", methods=["GET"])
def consulta_persona(id_persona):
    try:
        persona = modelo.sp_consultaPersonaID(id_persona)
        if persona:
            return jsonify(persona), 200
        else:
            return jsonify({"Mensaje": "Persona no encontrada"}), 404
    except Exception as e:
        return jsonify({"Error": str(e)}), 500

# API para listar personas (limitadas a 30)
@app.route("/persona/listado", methods=["GET"])
def listado_persona():
    num_personas = request.args.get('take', default=30, type=int)
    result = modelo.obtenerDatos()
    resultado = result[:num_personas]
    return jsonify(resultado)

# Ruta para agregar repartición
@app.route("/reparticion/agregar", methods=["POST"])
def agregar_reparticion():
    try:
        nombres = request.form.get("nombres")
        descripcion = request.form.get("descripcion")
        modelo.sp_agregarReparticion(nombres, descripcion)
        return jsonify({"Mensaje": "Repartición agregada correctamente"}), 201
    except Exception as e:
        return jsonify({"Error": str(e)}), 500

# Ruta para consultar repartición por ID
@app.route("/reparticion/consulta/<int:id_reparticion>", methods=["GET"])
def consulta_reparticion(id_reparticion):
    try:
        reparticion = modelo.sp_consultaReparticionID(id_reparticion)
        if reparticion:
            return jsonify(reparticion), 200
        else:
            return jsonify({"Mensaje": "Repartición no encontrada"}), 404
    except Exception as e:
        return jsonify({"Error": str(e)}), 500

# Ruta para eliminar repartición
@app.route("/reparticion/eliminar/<int:id_reparticion>", methods=["DELETE"])
def eliminar_reparticion(id_reparticion):
    try:
        modelo.sp_eliminarReparticion(id_reparticion)
        return jsonify({"Mensaje": f"Repartición con ID {id_reparticion} eliminada correctamente"}), 200
    except Exception as e:
        return jsonify({"Error": str(e)}), 500

# Ruta para modificar repartición
@app.route("/reparticion/update/<int:id_reparticion>", methods=["PUT"])
def modificar_reparticion(id_reparticion):
    try:
        nombres = request.form.get("nombres")
        descripcion = request.form.get("descripcion")
        modelo.sp_modificarReparticion(id_reparticion, nombres, descripcion)
        return jsonify({"Mensaje": "Repartición modificada correctamente"}), 200
    except Exception as e:
        return jsonify({"Error": str(e)}), 500

@app.route("/licencia/agregar", methods=["POST"])
def agregar_licencia():
    try:
        # Extraer datos del formulario
        p_Id_Persona = request.form.get("id_persona")
        p_Nro_Art = request.form.get("nro_art")
        p_Codigo = request.form.get("codigo")
        p_Diagnostico = request.form.get("diagnostico")
        p_Medico = request.form.get("medico")
        p_Matricula = request.form.get("matricula")
        p_Establecimiento = request.form.get("establecimiento")
        p_Fecha_de_inicio = request.form.get("fecha_de_inicio")
        p_Fecha_de_fin = request.form.get("fecha_de_fin")
        p_Cant_dias_licencias = request.form.get("cant_dias_licencias")
        p_Id_Estado_Licencia = request.form.get("id_estado_licencia")
        p_Observaciones = request.form.get("observaciones")

        # Llamar al modelo para insertar la licencia
        mensaje = modelo.SP_InsertarLicencia(
            p_Id_Persona, p_Nro_Art, p_Codigo, p_Diagnostico,
            p_Medico, p_Matricula, p_Establecimiento,
            p_Fecha_de_inicio, p_Fecha_de_fin,
            p_Cant_dias_licencias, p_Id_Estado_Licencia,
            p_Observaciones
        )
        return jsonify({"Mensaje": mensaje}), 201
    except Exception as e:
        return jsonify({"Error": str(e)}), 500


if __name__ == '__main__':
    with app.app_context():
        app.run(host="localhost", port="5000", debug=True)