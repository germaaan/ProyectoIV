#!flask/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask,request
from flask_restful import Resource,Api,reqparse,request
from flask_pymongo import PyMongo,MongoClient
import json
from bson.json_util import loads
from bson.json_util import dumps


app = Flask(__name__)
api = Api(app)


uri = "mongodb://usuario:password@ds145370.mlab.com:45370/heroku_skjh356f"
client = MongoClient(uri)
db = client.heroku_skjh356f
colection = db['vuln']


#Manejador de insertar datos en la bbdd
class Insert(Resource):
    def post(self):

        data = request.data
        colection.insert(loads(data))

        return loads(data)


#Manejador de busqueda en BBDD
class Search(Resource):

    def post(self, servicio,version):
        query = colection.find({})
        return dumps(query)


#Manejador de actualizar la bbdd
class Update(Resource):
    def post(self):
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
