from flask import Flask,jsonify,request
import models
app=Flask(__name__)

if __name__=='__main__':
    with app.app_context():
        app.run(host="localhost",port="5000",debug=True)