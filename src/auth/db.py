from typing import Any
import mysql.connector, os
from abc import ABC, abstractmethod
from .models import User

class InvalidCredentialsException(Exception):
    pass

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances: 
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=Singleton):
    def __init__(self):
        self.make_connection()

    def make_connection(self):
        self.connection = mysql.connector.connect(
            host=os.environ.get('MYSQL_HOST'), 
            user=os.environ.get('MYSQL_USER'), 
            password=os.environ.get('MYSQL_PASSWORD'),
            database=os.environ.get('MYSQL_DB'),
            port=os.environ.get('MYSQL_PORT')
        )

    def __del__(self):
        self.connection.close()

    def cursor(self):
        try:
            return self.connection.cursor()
        except Exception as e:
            self.make_connection()
            return self.connection.cursor()

class IDataBaseOperations(ABC):
    @abstractmethod
    def __init__(self):
        """Init database connection"""
        raise NotImplementedError
    
    @abstractmethod
    def check_credentials(self, username: str, password: str) -> bool:
        """Check if a user in the database exists with the given credentials"""
        raise NotImplementedError

class DataBaseOperations(IDataBaseOperations):
    def __init__(self):

        self.db = Database()
    
    def check_credentials(self, username: str, password: str) -> bool:
        """Check if a user in the database exists with the given credentials"""

        cur = self.db.cursor()
        cur.execute(f'CALL CheckLoginCredentials(%s, %s);', (username, password))
        res = cur.fetchone()
        if res is None or (len(res) == 0):
            raise InvalidCredentialsException('The given user does not exist or the password is incorrect')
        return User(id_=res[0], email=username, isAdmin=res[2])
