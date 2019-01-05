from flask_restful import Resource
from flask import request


class Ping(Resource):
    def get(self):
        return {"/ping": "This service is up!"}
