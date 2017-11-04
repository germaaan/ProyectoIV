#!flask/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask,request
from flask_restful import Resource,Api,reqparse
from flask_pymongo import PyMongo,MongoClient
import json


app = Flask(__name__)
api = Api(app)


uri = "mongodb://usuario:password@ds145370.mlab.com:45370/heroku_skjh356f"
client = MongoClient(uri)
db = client.heroku_skjh356f
colection = db['vuln']


#Manejador de insertar datos en la bbdd
class Insert(Resource):
    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument('data')
        args = parser.parse_args()
        data = args.get('data')

        try:
            json_line = json.loads(data)
            #id = colection.insert(json_line)
        except ValueError:
            json_line = "error"

        return {"id":json_line}

    def get(self):
        #col.insert({"prueba":"ok"})

        parser = reqparse.RequestParser()
        parser.add_argument('data')
        args = parser.parse_args()
        data = args.get('data')

        try:
            json_line = json.loads(data)
            id = colection.insert(json_line)
        except ValueError:
            id = "error"

        return {"id":id}



#Manejador de busqueda en BBDD
class Search(Resource):

    def get(self, servicio,version):
        #Aqui buscar info  sobre el servicio y su version en BBDD
        #data = search(servicio,version)
        return "datos buscados"




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





api.add_resource(Search, '/api/search/<string:servicio>/<string:version>')
api.add_resource(Insert, '/api/insert')
api.add_resource(Update, '/api/update')
api.add_resource(Test, '/')

if __name__ == '__main__':
    app.run(debug=True)
