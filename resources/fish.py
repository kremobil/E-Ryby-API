import werkzeug
from flask_restful import Resource, reqparse
from models.fishes_model import Fishes_Model
from flask_jwt import jwt_required
from flask import send_file

class Fish(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'latin_name',
        type=str,
        required=True,
        help='add the fish name in latin'
    )
    parser.add_argument(
        'description',
        type=str,
        required=True,
        help='add the description about fish'
    )
    parser.add_argument(
        'bait',
        type=str,
        required=True,
        help='add the information about bait for this fish'
    )
    parser.add_argument(
        'attitude',
        type=str,
        required=False,
        help='add the fish attitude',
        default='Żeru spokojnego'
    )
    parser.add_argument(
        'protected',
        type=bool,
        required=False,
        help='is this fish protected?',
        default=False
    )
    def get(self, name):
        fish = Fishes_Model.find_by_name(name)
        if fish:
            return fish.json()
        return {'message': 'Fish not found'}

    @jwt_required()
    def post(self, name):
        if Fishes_Model.find_by_name(name):
            return {'message': f'Ryba ${name} already exists in database'}
        data = Fish.parser.parse_args()
        fish = Fishes_Model(name, data['latin_name'], data['description'], data['bait'], data['attitude'], data['protected'])
        fish.save_to_db()
        return fish.json()

    @jwt_required()
    def put(self, name):
        fish = Fishes_Model.find_by_name(name)
        data = Fish.parser.parse_args()
        if fish is None:
            fish = Fishes_Model(name, data['latin_name'], data['description'], data['bait'], data['attitude'], data['protected'])
        else:
            if data['latin_name'] != '':
                fish.latinName = data['latin_name']
            if data['description'] != '':
                fish.description = data['description']
            if data['bait'] != '':
                fish.bait = data['bait']
            fish.attitude = data['attitude']
            fish.protected = data['protected']

        fish.save_to_db()
        return fish.json()

    @jwt_required()
    def delete(self, name):
        fish = Fishes_Model.find_by_name(name)
        fish.del_from_db()
        return {'message': 'fish sucessfouly delete'}

class Fishes(Resource):
    def get(self):
        return {'fishes': [fish.json() for fish in Fishes_Model.query.all()]}

class fishIMG(Resource):
    def get(self, name):
        return send_file(f'images//{name}.png')

    def post(self, name):
        parse = reqparse.RequestParser()
        parse.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
        args = parse.parse_args()
        image_file = args['file']
        image_file.save(f"images/{name}.png")
        return send_file(f"images//{name}.png")

