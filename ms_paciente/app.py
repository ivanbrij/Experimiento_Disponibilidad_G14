import random

from ms_paciente import create_app
from flask_restful import Resource, Api
from flask import Flask, request
from faker import Faker
from datetime import datetime
import requests
import json

fake = Faker()

app = create_app('default')
app_context = app.app_context()
app_context.push()

api = Api(app)


class VistaPaciente(Resource):

    def get(self):
        idPaciente = fake.uuid4()
        nombrePaciente = fake.unique.name()
        fechaNacimiento=str(fake.date())
        direccion=fake.address()
        return {"id": idPaciente, "nombre": nombrePaciente, "fechaNacimiento": fechaNacimiento, "direccion": direccion}

class VistaPing(Resource):

    def get(self):
        return "echo", 200

api.add_resource(VistaPaciente, '/')
api.add_resource(VistaPing, '/ping')
