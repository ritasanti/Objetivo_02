from flask import Flask,jsonify,request
import models
app=Flask(__name__)


#Endpoint para mostrar todas las personas de la tabla
@app.route("/persona", methods=["GET"])
def get_Persona():
    resultado=[]
    result=models.obtenerDatos()
    for personas in result:
        resultado.append(personas)
    return jsonify(resultado)


#Endpoint muestra datos que cumplen condicion
@app.route("/persona/estado", methods=["GET"])
def get_Persona_Estado():
    return jsonify([persona for persona in models.obtenerDatos_Estado()])


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
        models.sp_RegistroPersona(apellido,nombres,dni,domicilio,telefono,id_estado,fechora_registro)
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
        models.sp_updatePersona(id,apellido,nombres,dni,domicilio,telefono,id_estado)
        return jsonify({"Mensaje":"Se actualizo correctamente"})
    except Exception as e:
        return jsonify({"Mensaje":str (e)}), 500


# Ruta para el SP_EliminarPersona
@app.route("/persona/eliminar/<int:id_persona>", methods=["DELETE"])
def eliminar_persona(id_persona):
    try:
        models.sp_eliminarPersona(id_persona)
        return jsonify({"Mensaje": f"Persona con ID {id_persona} eliminada correctamente"}), 200
    except Exception as e:
        return jsonify({"Error": str(e)}), 500

if __name__=='__main__':
    with app.app_context():
        app.run(host="localhost",port="5000",debug=True)