import jwt
import datetime
import os

class JWT:
    def __init__(self, algorithm):
        self.algorithm = algorithm
        self.jwt_kwargs = {
            'key': os.getenv('SECRET', ''),
            'algorithm': algorithm
        }
    
    def jwt_operation(self, operation: str, **kwargs):
        if operation == 'create':
            return jwt.encode(
                {
                    'user': kwargs['username'], 
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30),
                    'iat': datetime.datetime.utcnow(),
                    'admin': kwargs['authz']
                },
                **self.jwt_kwargs
            )
        if operation == 'decode':
            local_kwargs = self.jwt_kwargs.copy(); local_kwargs.pop('algorithm')
            try:
                return jwt.decode(
                    kwargs['token'].split(' ')[1], 
                    **local_kwargs,
                    algorithms=self.algorithm
                )
            except jwt.InvalidTokenError:
                return {'message': 'Invalid token'}, 401
            except jwt.ExpiredSignatureError:
                return {'message': 'Token expired'}, 401