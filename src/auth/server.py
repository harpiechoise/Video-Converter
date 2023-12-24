import dotenv
from flask import Flask, request
from db import InvalidCredentialsException, DataBaseOperations
from validators import create_strategy
from login import JWT

dotenv.load_dotenv()

email_validator = create_strategy('login', 'email')
password_validator = create_strategy('login', 'password')
jwt = JWT('HS256')

server = Flask(__name__)

#! Singleton DB
db = DataBaseOperations()

# Config MySQL connection
@server.route('/login', methods=['POST'])
def login():
    # Basic authorazation header
    auth = request.authorization
    email_validator.excecute(auth.username)
    password_validator.excecute(auth.password)
    
    if not auth:
        return {'message': 'Missing credentials'}, 401
    #! Check user and password in DB
    try:
        user = db.check_credentials(auth.username, auth.password)
    except InvalidCredentialsException as e:
        return {'message': str(e)}, 401

    else:
        #! Create a JWT token
        return jwt.jwt_operation('create', 
                                 username=auth.username, 
                                 authz=user.isAdmin)


@server.route('/me', methods=['GET'])
def validate():
    encoded_jwt = request.headers.get('Authorization')
    if encoded_jwt is None:
        return {'message': 'Missing credentials'}, 401
    else:
        return jwt.jwt_operation('decode', token=encoded_jwt)

if __name__ == '__main__':
    server.run(debug=True)