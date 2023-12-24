from src.auth.models import User

def test_user():
    user = User(1, 'jaime', True)
    assert user.id_ == 1
    assert user.email == 'jaime'
    assert user.isAdmin == True
    assert user.__repr__() == 'User(id_=1, email=\'jaime\', isAdmin=True)'
    assert user.__str__() == 'User(id_=1, email=\'jaime\', isAdmin=True)'