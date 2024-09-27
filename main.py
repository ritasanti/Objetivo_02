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

#Eliminar Registro de la base de datos
@app.route("/persona/<int:id>", methods=["DELETE"])
def eliminar_persona(id):
    resultado=models.eliminarDato(id)
    if resultado:
        return jsonify({"message":"Persona eliminada"}),200
    else:
        return jsonify({"message":"Persona no encontrada"}),404
    
#Faltan la funcion de modificar e insertar, trabajando en eso


if __name__=='__main__':
    with app.app_context():
        app.run(host="localhost",port="5000",debug=True)

# Ruta para el SP_EliminarPersona
@app.route("/persona/eliminar/<int:id_persona>", methods=["UPDATE"])
def eliminar_persona(id_persona):
    try:
        models.sp_eliminarPersona(id_persona)
        return jsonify({"Mensaje": f"Persona con ID {id_persona} eliminada correctamente"}), 200
    except Exception as e:
        return jsonify({"Error": str(e)}), 500