from src.auth.db import Database, InvalidCredentialsException, DataBaseOperations
from dotenv import load_dotenv
import pytest
import os
from src.auth.models import User

load_dotenv()
def test_singleton():
    db1 = Database()
    db2 = Database()
    assert db1 is db2
    assert db1.connection is db2.connection
    assert db1.connection is not None

def test_getattr():
    db = Database()
    assert db.cursor() is not None

def test_db_operations():
    db = DataBaseOperations()

    with pytest.raises(InvalidCredentialsException):
        db.check_credentials('a', 'b')

    username = os.getenv('DBADMIN')
    password = os.getenv('DBPASS')
    user = db.check_credentials(username, password)

    assert user is not None
    assert isinstance(user, User)
    assert user.isAdmin == True
    assert user.email == 'jaimecrispi@email.com'
    assert user.id_ is not None
    assert user.id_ > 0