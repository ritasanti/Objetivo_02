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


if __name__=='__main__':
    with app.app_context():
        app.run(host="localhost",port="5000",debug=True)