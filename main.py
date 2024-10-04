from flask import Flask,jsonify,request
from models import modelo
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