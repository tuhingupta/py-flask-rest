from flask_restful import Resource
from flask import request
from notes_dict import notes
import json


class Notes(Resource):
    #GET http://127.0.0.1:5000/flaskapp/notes?q=c
    #GET http://127.0.0.1:5000/flaskapp/notes
    def get(self):
        ''' Get notes from the dictionary. Get all notes or provide q=<note key> in query param'''
        if 'q' in request.args:
            queryParam = request.args['q']
            val = notes.get(queryParam)
            if val is None:
                return json.dumps({'Not Found': str('No value found for query param - {}'.format(queryParam))})
            else:
                return {queryParam: val}
        else:
            return notes

    #POST http://127.0.0.1:5000/flaskapp/notes {"a": "This is body a"}
    def post(self):
        ''' Add notes into a dictionary by providing key/value pair'''
        #value = json.loads(request)
        data = json.loads(request.data)
        key = list(data.keys())[0]
        #val = data.get(key)
        notes.update(data)
        return {"message": "Note {} added!".format(key)}