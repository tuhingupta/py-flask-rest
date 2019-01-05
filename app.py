from flask import Blueprint
from flask_restful import Api
from resources.Ping import Ping
from resources.Notes import Notes

api_bp = Blueprint('root', __name__)
#notes_bp = Blueprint('notes', __name__)

api = Api(api_bp)
#notes_api = Api(notes_bp)

## Routes

#"GET /flaskapp/ping HTTP/1.1"
api.add_resource(Ping, '/ping')

#"GET /flaskapp/notes HTTP/1.1"
#"GET /flaskapp/notes?q=a HTTP/1.1"
#"POST /flaskapp/notes HTTP/1.1" 
api.add_resource(Notes, '/notes')
#notes_api.add_resource(Notes, '')
