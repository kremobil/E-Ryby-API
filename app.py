from datetime import timedelta
from flask_cors import CORS

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from db import db
from models.user_model import UserModel
from resources.fish import Fish, Fishes, fishIMG
from security import authenticate, identity
from resources.user import UserRegister

app = Flask(__name__)
app.secret_key = 'wnikjuabniufrhiuawgh'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

api.add_resource(Fish, '/fish/<string:name>')
api.add_resource(Fishes, '/fishes')
api.add_resource(UserRegister, '/register')
api.add_resource(fishIMG, '/img/<string:name>')

app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)
app.config['JWT_AUTH_URL_RULE'] = '/login'
jwt = JWT(app, authenticate, identity)

cros = CORS(app)

@jwt.auth_response_handler
def customized_response_handler(access_token, identity):
    return {'access_token': access_token.decode('utf-8'), 'user': UserModel.find_by_id(identity.id).get_username()}
# if __name__ == '__main__':
app.run(port=2137, debug=True)