from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
from models.user_model import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username', type=str,
        required=True,
        help='set your username'
    )
    parser.add_argument(
        'password', type=str,
        required=True,
        help='set your password',
    )

    @jwt_required()
    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {"message": f"username {data['username']} already exists"}, 400

        user = UserModel(**data)
        user.save_to_db()
        return {"message": "user craeted successfully"}, 201