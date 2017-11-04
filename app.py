#!flask/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Resource,Api
from flask_pymongo import PyMongo,MongoClient


app = Flask(__name__)
api = Api(app)


uri = "mongodb://usuario:password@ds145370.mlab.com:45370/heroku_skjh356f"
client = MongoClient(uri)

#Manejador de insertar datos en la bbdd
class Insert(Resource):
    def post(self):

        return "Inserto_datos_en_bbdd"
    def get(self):
        client.vuln.insert({"name":"pepe"})
        return "Inserto_datos_en_bb"



#Manejador de busqueda en BBDD
class Search(Resource):

    def get(self, servicio,version):
        #Aqui buscar info  sobre el servicio y su version en BBDD
        #data = search(servicio,version)
        return "Buscando"




#Manejador de actualizar la bbdd
class Update(Resource):
    def post(self):
        return "Actualizo_toda_la_bbdd"
    def get(self):
        return "Actualizo_toda_la_bbdd"

#Manejador de actualizar la bbdd
class Test(Resource):
    def post(self):
        return {"Status":"OK"}
    def get(self):
        return {"Status":"OK"}





api.add_resource(Search, '/api/<string:servicio>/<string:version>')
api.add_resource(Insert, '/api/insert')
api.add_resource(Update, '/api/update')
api.add_resource(Test, '/')

if __name__ == '__main__':
    app.run(debug=True)
