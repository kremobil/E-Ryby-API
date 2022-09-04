from flask_restful import Resource, reqparse
from models.image_model import ImageModel
from models.fishes_model import Fishes_Model
from flask_jwt import jwt_required
from flask import send_file
from io import BytesIO
import werkzeug

class image(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files', required=True)
    @jwt_required
    def post(self, fish_id):
        if not(Fishes_Model.find_by_id(fish_id)):
            return {'message': f'fish with id {fish_id} does not exists in database. check id before adding image'}
        if ImageModel.find_by_fishid(fish_id):
            return {'message': f'this fish already have image'}

        data = self.parser.parse_args()
        img = ImageModel(data['file'].read(), Fishes_Model.find_by_id(fish_id).name, fish_id)
        img.save_to_db()
        return img.json()

    def get(self, fish_id):
        img = ImageModel.find_by_fishid(fish_id)
        if img:
            return send_file(BytesIO(img.data), download_name=f"{img.filename}.png")

        return {'message': f'fish with id {fish_id} does not have image in database'}
    @jwt_required
    def delete(self, fish_id):
        img = ImageModel.find_by_fishid(fish_id)
        img.del_from_db()
        return {'message':f'image was successfully deleted'}
    @jwt_required
    def put(self, fish_id):
        if not(Fishes_Model.find_by_id(fish_id)):
            return {'message': f'fish with id {fish_id} does not exists in database. check id before adding image'}

        img = ImageModel.find_by_fishid(fish_id)
        data = self.parser.parse_args()
        if img:
            img.data = data['file'].read()
            img.save_to_db()
            return {'message': f'image for fish {img.fish_id} was successfully updated'}
        else:
            img = ImageModel(data['file'].read(), Fishes_Model.find_by_id(fish_id).name, fish_id)
            img.save_to_db()
            return {'message':f'image for fish {img.fish_id} successfully added to database'}



